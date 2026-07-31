#!/bin/bash

#$ -M ccervera@nd.edu
#$ -m abe
#$ -pe smp 4
#$ -q gpu
#$ -l gpu=1
#$ -N thesis_experiment

module load python
module load cuda/12.1
export LD_LIBRARY_PATH=/afs/crc.nd.edu/x86_64_linux/c/cuda/12.1/lib64:$LD_LIBRARY_PATH
source ~/thesis_env_new/bin/activate

source ~/offline-llm-math-tutor/.env

cd ~/offline-llm-math-tutor

# Build FAISS index if not already built
if [ ! -f "index/faiss_index.bin" ]; then
    echo "Building FAISS index..."
    python code/rag/build_index.py
fi

# Run experiments
python code/experiment.py