import json
import os


save_files = "save.json"

# -----------------------------
# Load tasks from JSON file
# -----------------------------
def load_save(save_files):
    if os.path.exists(save_files) and os.path.getsize(save_files) > 0:
        with open(save_files, "r") as file:
            tasks = json.load(file)
            return {int(k): v for k, v in tasks.items()}
    return {}

# -----------------------------
# Save tasks to JSON file
# -----------------------------
def saving_file(save_files, tasks):
    with open(save_files, "w") as file:
        json.dump(tasks, file, indent=4)


