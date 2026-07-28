#!/bin/bash

#$ -M ccervera@nd.edu
#$ -m abe
#$ -pe smp 4
#$ -q gpu
#$ -l gpu=1
#$ -N thesis_experiment

module load python
module load cuda/12.1
module load cmake
source ~/thesis_env_new/bin/activate

source ~/offline-llm-math-tutor/.env

cd ~/offline-llm-math-tutor

# Build llama.cpp if not already built
if [ ! -f "llama.cpp/build/bin/llama-cli" ]; then
    echo "Building llama.cpp..."
    cd llama.cpp
    cmake -B build -DGGML_CUDA=ON
    cmake --build build --config Release -j4
    cd ..
fi

# Download models if not already downloaded
python code/download_models.py

# Build FAISS index if not already built
if [ ! -f "index/faiss_index.bin" ]; then
    echo "Building FAISS index..."
    python code/rag/build_index.py
fi

# Run experiments
python code/experiment.py