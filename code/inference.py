import subprocess
import os

ROOT = os.path.dirname(os.path.dirname(__file__))
LLAMA_BIN = os.path.join(ROOT, "llama.cpp", "build", "bin", "llama-cli")


def run_model(model_path, prompt, max_tokens=600, timeout=45):
    command = [
        LLAMA_BIN,
        "-m", model_path,
        "-p", prompt,
        "-n", str(max_tokens),
        "--temp", "0.2",
        "--ctx-size", "4096",
        "-no-cnv",
        "-st",
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

    output = (stdout or "") + "\n" + (stderr or "")

    # Keep only the text after the prompt, if present
    if prompt in output:
        output = output.split(prompt, 1)[1]

    # Remove timing/footer info
    if "[ Prompt:" in output:
        output = output.split("[ Prompt:", 1)[0]

    # Remove interactive markers if they appear
    lines = []
    for line in output.splitlines():
        stripped = line.strip()

        # skip llama.cpp banner / logs / prompt markers
        if not stripped:
            continue
        if stripped.startswith("Loading model"):
            continue
        if stripped.startswith("build"):
            continue
        if stripped.startswith("model"):
            continue
        if stripped.startswith("modalities"):
            continue
        if stripped.startswith("available commands"):
            continue
        if stripped.startswith("/exit"):
            continue
        if stripped.startswith("/regen"):
            continue
        if stripped.startswith("/clear"):
            continue
        if stripped.startswith("/read"):
            continue
        if stripped == ">":
            continue
        if "ggml_" in stripped:
            continue
        if "MTLGPUFamily" in stripped:
            continue
        if "recommendedMaxWorkingSetSize" in stripped:
            continue

        lines.append(line)

    return "\n".join(lines).strip()