import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(__file__))
MODELS_DIR = os.path.join(ROOT, "models")
os.makedirs(MODELS_DIR, exist_ok=True)

MODELS = [
    ("TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF", "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"),
    ("Qwen/Qwen2.5-1.5B-Instruct-GGUF", "qwen2.5-1.5b-instruct-q4_k_m.gguf"),
    ("bartowski/gemma-2-2b-it-GGUF", "gemma-2-2b-it-Q4_K_M.gguf"),
    ("TheBloke/phi-2-GGUF", "phi-2.Q4_K_M.gguf"),
    ("Qwen/Qwen2.5-3B-Instruct-GGUF", "qwen2.5-3b-instruct-q4_k_m.gguf"),
    ("microsoft/Phi-3-mini-4k-instruct-gguf", "Phi-3-mini-4k-instruct-q4.gguf"),
    ("bartowski/Qwen_Qwen3-4B-GGUF", "Qwen_Qwen3-4B-Q4_K_M.gguf"),
    ("TheBloke/Mistral-7B-Instruct-v0.3-GGUF", "mistral-7b-instruct-v0.3.Q4_K_M.gguf"),
]

for repo, filename in MODELS:
    output_path = os.path.join(MODELS_DIR, filename)
    if os.path.exists(output_path):
        print(f"Already exists: {filename}")
        continue
    print(f"Downloading {filename}...")
    subprocess.run([
        "huggingface-cli", "download",
        repo, filename,
        "--local-dir", MODELS_DIR,
        "--local-dir-use-symlinks", "False"
    ])
    print(f"Done: {filename}")

print("\nAll models downloaded.")