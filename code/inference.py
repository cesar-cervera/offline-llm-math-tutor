import subprocess
import os

ROOT = os.path.dirname(os.path.dirname(__file__))
LLAMA_BIN = os.path.join(ROOT, "llama.cpp", "build", "bin", "llama-cli")

MODELS = {
    "TinyLlama": os.path.join(ROOT, "models", "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"),
    "Qwen1.5B": os.path.join(ROOT, "models", "qwen2.5-1.5b-instruct-q4_k_m.gguf"),
    "Gemma2B": os.path.join(ROOT, "models", "gemma-2-2b-it-Q4_K_M.gguf"),
    "Phi2": os.path.join(ROOT, "models", "phi-2.Q4_K_M.gguf"),
    "Qwen3B": os.path.join(ROOT, "models", "qwen2.5-3b-instruct-q4_k_m.gguf"),
    "Phi3Mini": os.path.join(ROOT, "models", "Phi-3-mini-4k-instruct-q4.gguf"),
    "Qwen3_4B": os.path.join(ROOT, "models", "Qwen_Qwen3-4B-Q4_K_M.gguf"),
    "Mistral7B": os.path.join(ROOT, "models", "mistral-7b-instruct-v0.3.Q4_K_M.gguf"),
}


def run_model(model_path, prompt, max_tokens=512, n_gpu_layers=35, timeout=120):
    command = [
        LLAMA_BIN,
        "-m", model_path,
        "-p", prompt,
        "-n", str(max_tokens),
        "--temp", "0.2",
        "--ctx-size", "4096",
        "-ngl", str(n_gpu_layers),
        "-no-cnv",
        "--simple-io",
    ]

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()

    # DEBUG: print raw output for first few calls
    import os
    debug_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "debug_output.txt")
    if not os.path.exists(debug_file):
        with open(debug_file, "w") as f:
            f.write("STDOUT:\n")
            f.write(stdout or "EMPTY")
            f.write("\n\nSTDERR:\n")
            f.write(stderr or "EMPTY")

    output = stdout or ""

    if prompt in output:
        output = output.split(prompt, 1)[1]

    if "[ Prompt:" in output:
        output = output.split("[ Prompt:", 1)[0]

    lines = []
    for line in output.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if any(stripped.startswith(x) for x in [
            "llama_", "ggml_", "build", "model", "system_info",
            "sampling", "generate", "Loading", "main:"
        ]):
            continue
        lines.append(line)

    return "\n".join(lines).strip()