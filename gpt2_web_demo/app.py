from flask import Flask, render_template, request, jsonify
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import torch
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
executor = ThreadPoolExecutor(2)  # For parallel model execution

# Model paths mapping
MODELS = {
    # 'bpe_10MB': '../gpt2_bpe_manual_10MB',
    'bpe_100MB': '../gpt2_bpe_manual_100MB',
    # 'morph_10MB': '../gpt2_morph_manual_10MB',
    'morph_100MB': '../gpt2_morph_manual_100MB'
}


# Load models at startup
morph_model = GPT2LMHeadModel.from_pretrained(MODELS['morph_100MB'])
morph_tokenizer = GPT2TokenizerFast.from_pretrained(MODELS['morph_100MB'])

bpe_model = GPT2LMHeadModel.from_pretrained(MODELS['bpe_100MB'])
bpe_tokenizer = GPT2TokenizerFast.from_pretrained(MODELS['bpe_100MB'])

def generate_response(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=100,
        do_sample=True,
        top_p=0.9,
        temperature=0.9,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=1
    )
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    if generated_text.startswith(prompt):
        generated_text = generated_text[len(prompt):].lstrip()
    return generated_text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.json['prompt']
    
    # Submit both model generations to thread pool
    morph_future = executor.submit(generate_response, morph_model, morph_tokenizer, prompt)
    bpe_future = executor.submit(generate_response, bpe_model, bpe_tokenizer, prompt)
    
    # Wait for both to complete
    morph_response = morph_future.result()
    bpe_response = bpe_future.result()
    
    return jsonify({
        'morph': morph_response,
        'bpe': bpe_response
    })

if __name__ == '__main__':
    app.run(debug=True)