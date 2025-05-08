# Low-Resource Hindi Language Modeling with Custom Tokenizers

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A comparative study of BPE vs. morpheme-based tokenizers for GPT-2 models on Hindi text, achieving **23% lower perplexity** with linguistically-informed tokenization.

## 📌 Key Features

- **Two Tokenizer Implementations**:
  - Standard BPE tokenizer
  - Morphological tokenizer (prefix/root/suffix decomposition)
  
- **Optimized GPT-2 Architecture**:
  - 8-layer model with 384-dim embeddings
  - Trained on 100MB Hindi corpus

- **Evaluation Framework**:
  - Perplexity (PPL) metrics
  - Output coherence analysis

## 📊 Results Summary

| Metric          | BPE    | Morpheme (Ours) |
|-----------------|--------|-----------------|
| Perplexity      | 24.3   | **18.7**        |
| Training Loss   | 5.07   | **3.39**        |
| OOV Rate       | 4.7%   | **2.1%**        |

## 🛠️ Setup

### Requirements
```bash
pip install -r requirements.txt  # Includes:
# transformers==4.30.0
# tokenizers==0.13.3
# torch==2.0.1
```



---

## 📚 Corpus

- **Source**: Hindi Wikipedia dump (~1 GB)
- **Cleaned corpus sizes**: 10MB, 20MB, 50MB, 100MB
- **Tokenization**:
  - `BPE`: Trained using standard byte-pair merging (12k vocab)
  - `Morpheme`: Custom-built using Hindi prefixes, suffixes, and roots

---

## 🧠 Tokenizer Design

### Morpheme-Based Tokenizer
- 80+ prefixes
- 200+ suffixes
- 5,000+ root words
- Recursive segmentation algorithm
- Preserves meaning better than BPE

---

## 🏗️ GPT-2 Architecture

| Component        | Value            |
|------------------|------------------|
| Layers           | 8                |
| Embedding Dim    | 384              |
| Attention Heads  | 6                |
| FFN Hidden Dim   | 1536             |
| Vocab Size       | 12,000           |
| Optimizer        | AdamW            |
| Learning Rate    | 5e-4             |

---

## 📈 Evaluation

- **Metric**: Perplexity (PPL)
- **Result**:
  - **BPE Model**: 24.3
  - **Morpheme Model**: **18.7** ✅

Morpheme-based tokenizer reduced perplexity by **23%**, proving its effectiveness in low-resource settings.

---

## 💻 Demo Interface

A simple web interface is included under `gpt2_web_demo/` to compare BPE and Morpheme outputs interactively.

---

## 🚧 Challenges & Solutions

| Challenge              | Solution              |
|------------------------|-----------------------|
| Rare morphemes         | Fallback to characters|
| Training instability   | Gradient clipping     |
| Compute limitations    | Mixed precision (fp16)|

---

## 🚀 Applications

- Hindi Chatbots (education, support)
- Story and article generation
- Indian-language translation pipelines

---

## 🛑 Limitations

- Hindi-only support (for now)
- Morpheme dictionary has ~85% coverage

---

## 🌱 Future Work

- Expand to other Indian languages
- Combine morpheme and subword tokenization (hybrid)
- Scale to larger GPT models

---

## 📜 References

1. Jabbar, Haris. “MorphPiece: A Linguistic Tokenizer for Large Language Models.” arXiv:2307.07262
2. Vaswani et al. “Attention Is All You Need.” NeurIPS 2017

---

## 🤝 Authors

- **Chandan Kumar** (2024PCS0022)  : chandan4eu@gmail.com
- **Rohit Tiwari** (2024PCS0036) : rohitkrtiwari2002@gmail.com
- Under the guidance of **Dr. B. N. Subudhi** (IIT)

---
