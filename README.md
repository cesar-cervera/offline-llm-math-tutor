# Offline LLM Math Tutor

Evaluating RAG-augmented quantized LLMs for offline math tutoring on consumer hardware.

## Overview

This project investigates whether small, open-source quantized language models running entirely offline can provide reliable math tutoring to low-resource learners. It evaluates two models across two conditions (base and RAG) on the MathDial-Bridge dataset, measuring exact-match final answer accuracy across easy and hard problem difficulty levels.

**Research question:** Can retrieval-based grounding compensate for the parametric knowledge lost to quantization, making offline deployment a viable alternative to cloud-hosted tutoring systems?

## Models

| Model | Size | Format |
|-------|------|--------|
| Phi-3-mini-4k-instruct | 3.8B | Q4 GGUF |
| TinyLlama-1.1B-Chat-v1.0 | 1.1B | Q4_K_M GGUF |

## Results

Preliminary evaluation on 5 problems per condition from each difficulty tier, run locally on consumer hardware.

| Model | Easy Base | Easy RAG | Hard Base | Hard RAG |
|-------|-----------|----------|-----------|----------|
| Phi-3 Mini | 1.00 | 0.80 | 0.20 | 0.80 |
| TinyLlama | 0.00 | 0.00 | 0.00 | 0.00 |

**Key findings:**
- RAG has a difficulty-dependent effect on capable models: it introduces noise on easy problems but improves hard problem accuracy fourfold
- Below a minimum capability threshold (~1.1B parameters), RAG provides no benefit
- The capability threshold lies somewhere between 1.1B and 3.8B parameters

## Project Structure

```
.
├── code/
│   ├── inference.py       # Model inference via llama.cpp
│   ├── experiment.py      # Experiment runner (base and RAG conditions)
│   └── prompts.py         # Prompt templates for base and RAG conditions
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

- Python 3.9+
- [llama.cpp](https://github.com/ggerganov/llama.cpp) built locally
- GGUF model files (downloaded separately)

### Install dependencies

```bash
pip install -r requirements.txt
```

### Download models

Download the following GGUF models and place them in a `models/` directory:

- [Phi-3-mini-4k-instruct-q4.gguf](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf)
- [tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)

### Run the experiment

```bash
python code/experiment.py
```

## Dataset

Uses [MathDial-Bridge](https://huggingface.co/datasets/MathDial), a dialogue tutoring dataset constructed from GSM8K math problems with step-by-step tutoring exchanges across difficulty levels.

## RAG Implementation

The RAG condition provides the reference solution as retrieved context, establishing an upper bound on grounding effectiveness. Future work will evaluate retrieval from a general mathematical knowledge corpus to assess whether benefits hold under realistic offline deployment conditions.

## Tech Stack

- Python
- llama.cpp (local inference)
- HuggingFace Transformers
- PyTorch

## Status

Active research — part of masters thesis at the University of Notre Dame, advised by Prof. Meng Jiang.

## Overview

This project investigates whether small, open-source quantized language models running entirely offline can provide reliable math tutoring to low-resource learners. It evaluates two models across two conditions (base and RAG) on the MathDial-Bridge dataset, measuring exact-match final answer accuracy across easy and hard problem difficulty levels.

**Research question:** Can retrieval-based grounding compensate for the parametric knowledge lost to quantization, making offline deployment a viable alternative to cloud-hosted tutoring systems?

## Models

| Model | Size | Format |
|-------|------|--------|
| Phi-3-mini-4k-instruct | 3.8B | Q4 GGUF |
| TinyLlama-1.1B-Chat-v1.0 | 1.1B | Q4_K_M GGUF |

## Results

Preliminary evaluation on 5 problems per condition from each difficulty tier, run locally on consumer hardware.

| Model | Easy Base | Easy RAG | Hard Base | Hard RAG |
|-------|-----------|----------|-----------|----------|
| Phi-3 Mini | 1.00 | 0.80 | 0.20 | 0.80 |
| TinyLlama | 0.00 | 0.00 | 0.00 | 0.00 |

**Key findings:**
- RAG has a difficulty-dependent effect on capable models: it introduces noise on easy problems but improves hard problem accuracy fourfold
- Below a minimum capability threshold (~1.1B parameters), RAG provides no benefit
- The capability threshold lies somewhere between 1.1B and 3.8B parameters

## Project Structure

```
.
├── code/
│   ├── inference.py       # Model inference via llama.cpp
│   ├── experiment.py      # Experiment runner (base and RAG conditions)
│   └── prompts.py         # Prompt templates for base and RAG conditions
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

- Python 3.9+
- [llama.cpp](https://github.com/ggerganov/llama.cpp) built locally
- GGUF model files (downloaded separately)

### Install dependencies

```bash
pip install -r requirements.txt
```

### Download models

Download the following GGUF models and place them in a `models/` directory:

- [Phi-3-mini-4k-instruct-q4.gguf](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf)
- [tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)

### Run the experiment

```bash
python code/experiment.py
```

## Dataset

Uses [MathDial-Bridge](https://huggingface.co/datasets/MathDial), a dialogue tutoring dataset constructed from GSM8K math problems with step-by-step tutoring exchanges across difficulty levels.

## RAG Implementation

The RAG condition provides the reference solution as retrieved context, establishing an upper bound on grounding effectiveness. Future work will evaluate retrieval from a general mathematical knowledge corpus to assess whether benefits hold under realistic offline deployment conditions.

## Tech Stack

- Python
- llama.cpp (local inference)
- HuggingFace Transformers
- PyTorch

## Status

Active research — part of masters thesis at the University of Notre Dame, advised by Prof. Meng Jiang.