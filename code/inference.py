import torch
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

MODELS = {
    "TinyLlama": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    "Qwen1.5B": "Qwen/Qwen2.5-1.5B-Instruct",
    "Gemma2B": "google/gemma-2-2b-it",
    "Phi2": "microsoft/phi-2",
    "Qwen3B": "Qwen/Qwen2.5-3B-Instruct",
    "Phi3Mini": "microsoft/Phi-3-mini-4k-instruct",
    "Qwen3_4B": "Qwen/Qwen3-4B",
    "Mistral7B": "mistralai/Mistral-7B-Instruct-v0.3"
}


def load_model(model_name):
    print(f"Loading {model_name}...")
    token = os.environ.get("HF_TOKEN", None)

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name, token=token)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
        device_map="auto",
        token=token
    )
    model.eval()
    return model, tokenizer


def run_model(model, tokenizer, prompt, max_new_tokens=512):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=0.2,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

    generated = outputs[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(generated, skip_special_tokens=True)