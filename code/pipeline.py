import json

with open("code/mathdial_bridge.json") as f:
    data = json.load(f)

example = data[0]

print("PROBLEM:")
print(example["problem"])
print("\nREFERENCE SOLUTION:")
print(example["reference_solution"])
print("\nDIALOG HISTORY:")
for turn in example["dialog_history"]:
    print(f"{turn['user']}: {turn['text']}")