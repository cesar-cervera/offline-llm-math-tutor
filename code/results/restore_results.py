import json

results = {
    "TinyLlama": {
        "easy": {
            "base": {"answer_accuracy": 0.008695652173913044, "explanation_accuracy": 0.5052173913043478, "both_correct": 0.0052173913043478265, "answer_only": 0.0034782608695652175, "total": 1150},
            "rag": {"answer_accuracy": 0.5469565217391305, "explanation_accuracy": 0.871304347826087, "both_correct": 0.5469565217391305, "answer_only": 0.0, "total": 1150}
        },
        "hard": {
            "base": {"answer_accuracy": 0.009174311926605505, "explanation_accuracy": 0.44954128440366975, "both_correct": 0.009174311926605505, "answer_only": 0.0, "total": 327},
            "rag": {"answer_accuracy": 0.4648318042813456, "explanation_accuracy": 0.691131498470948, "both_correct": 0.45871559633027525, "answer_only": 0.0061162079510703364, "total": 327}
        }
    },
    "Qwen1.5B": {
        "easy": {
            "base": {"answer_accuracy": 0.32956521739130434, "explanation_accuracy": 0.8121739130434783, "both_correct": 0.32869565217391306, "answer_only": 0.0008695652173913044, "total": 1150},
            "rag": {"answer_accuracy": 0.5034782608695653, "explanation_accuracy": 0.8321739130434782, "both_correct": 0.5, "answer_only": 0.0034782608695652175, "total": 1150}
        },
        "hard": {
            "base": {"answer_accuracy": 0.27217125382262997, "explanation_accuracy": 0.7247706422018348, "both_correct": 0.27217125382262997, "answer_only": 0.0, "total": 327},
            "rag": {"answer_accuracy": 0.43730886850152906, "explanation_accuracy": 0.7553516819571865, "both_correct": 0.42813455657492355, "answer_only": 0.009174311926605505, "total": 327}
        }
    },
    "Gemma2B": {
        "easy": {
            "base": {"answer_accuracy": 0.28956521739130436, "explanation_accuracy": 0.7843478260869565, "both_correct": 0.28956521739130436, "answer_only": 0.0, "total": 1150},
            "rag": {"answer_accuracy": 0.7052173913043478, "explanation_accuracy": 0.8556521739130435, "both_correct": 0.7034782608695652, "answer_only": 0.0017391304347826088, "total": 1150}
        },
        "hard": {
            "base": {"answer_accuracy": 0.2599388379204893, "explanation_accuracy": 0.7155963302752294, "both_correct": 0.2599388379204893, "answer_only": 0.0, "total": 327},
            "rag": {"answer_accuracy": 0.5443425076452599, "explanation_accuracy": 0.7859327217125383, "both_correct": 0.5412844036697247, "answer_only": 0.0030581039755351682, "total": 327}
        }
    },
    "Phi2": {
        "easy": {
            "base": {"answer_accuracy": 0.18434782608695652, "explanation_accuracy": 0.7817391304347826, "both_correct": 0.1826086956521739, "answer_only": 0.0017391304347826088, "total": 1150},
            "rag": {"answer_accuracy": 0.37217391304347824, "explanation_accuracy": 0.8539130434782609, "both_correct": 0.37043478260869567, "answer_only": 0.0017391304347826088, "total": 1150}
        },
        "hard": {
            "base": {"answer_accuracy": 0.1651376146788991, "explanation_accuracy": 0.7186544342507645, "both_correct": 0.1651376146788991, "answer_only": 0.0, "total": 327},
            "rag": {"answer_accuracy": 0.290519877675841, "explanation_accuracy": 0.7675840978593272, "both_correct": 0.290519877675841, "answer_only": 0.0, "total": 327}
        }
    },
    "Phi3Mini": {
        "easy": {
            "base": {"answer_accuracy": 0.6330434782608696, "explanation_accuracy": 0.851304347826087, "both_correct": 0.6304347826086957, "answer_only": 0.0026086956521739132, "total": 1150},
            "rag": {"answer_accuracy": 0.8017391304347826, "explanation_accuracy": 0.8686956521739131, "both_correct": 0.8017391304347826, "answer_only": 0.0, "total": 1150}
        },
        "hard": {
            "base": {"answer_accuracy": 0.5412844036697247, "explanation_accuracy": 0.7706422018348624, "both_correct": 0.5412844036697247, "answer_only": 0.0, "total": 327},
            "rag": {"answer_accuracy": 0.7339449541284404, "explanation_accuracy": 0.8103975535168195, "both_correct": 0.7339449541284404, "answer_only": 0.0, "total": 327}
        }
    },
    "Mistral7B": {
        "easy": {
            "base": {"answer_accuracy": 0.22956521739130434, "explanation_accuracy": 0.802608695652174, "both_correct": 0.22782608695652173, "answer_only": 0.0017391304347826088, "total": 1150},
            "rag": {"answer_accuracy": 0.6243478260869565, "explanation_accuracy": 0.8608695652173913, "both_correct": 0.6234782608695653, "answer_only": 0.0008695652173913044, "total": 1150}
        },
        "hard": {
            "base": {"answer_accuracy": 0.18654434250764526, "explanation_accuracy": 0.7186544342507645, "both_correct": 0.18654434250764526, "answer_only": 0.0, "total": 327},
            "rag": {"answer_accuracy": 0.45871559633027525, "explanation_accuracy": 0.7828746177370031, "both_correct": 0.45565749235474007, "answer_only": 0.0030581039755351682, "total": 327}
        }
    },
    "Qwen3B": {
        "easy": {
            "base": {"answer_accuracy": 0.571304347826087, "explanation_accuracy": 0.8443478260869566, "both_correct": 0.568695652173913, "answer_only": 0.0026086956521739132, "total": 1150},
            "rag": {"answer_accuracy": 0.7460869565217392, "explanation_accuracy": 0.8626086956521739, "both_correct": 0.7434782608695653, "answer_only": 0.0026086956521739132, "total": 1150}
        },
        "hard": {
            "base": {"answer_accuracy": 0.4984709480122324, "explanation_accuracy": 0.7828746177370031, "both_correct": 0.4984709480122324, "answer_only": 0.0, "total": 327},
            "rag": {"answer_accuracy": 0.6636085626911316, "explanation_accuracy": 0.8042813455657493, "both_correct": 0.6636085626911316, "answer_only": 0.0, "total": 327}
        }
    }
}

with open("code/results/results.json", "w") as f:
    json.dump(results, f, indent=2)

print("Results restored successfully with 7 models.")
print("Waiting for Qwen4B to be added after job completes.")