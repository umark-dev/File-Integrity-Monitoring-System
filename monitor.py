import hashlib
import json
import os

BASELINE_FILE = "baseline.json"
TARGET_DIR = "files"
ALERT_FILE = "alerts.txt"


def calculate_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()


def create_baseline():
    baseline = {}

    for filename in os.listdir(TARGET_DIR):
        path = os.path.join(TARGET_DIR, filename)
        if os.path.isfile(path):
            baseline[filename] = calculate_hash(path)

    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)

    print("Baseline created.")


def check_integrity():
    if not os.path.exists(BASELINE_FILE):
        print("Baseline not found. Creating baseline...")
        create_baseline()
        return

    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    alerts = []

    for filename in os.listdir(TARGET_DIR):
        path = os.path.join(TARGET_DIR, filename)

        if os.path.isfile(path):
            current_hash = calculate_hash(path)

            if filename not in baseline:
                alerts.append(f"[ALERT] New file detected: {filename}")

            elif baseline[filename] != current_hash:
                alerts.append(f"[ALERT] File modified: {filename}")

    for filename in baseline:
        if filename not in os.listdir(TARGET_DIR):
            alerts.append(f"[ALERT] File deleted: {filename}")

    with open(ALERT_FILE, "w") as f:
        for alert in alerts:
            f.write(alert + "\n")

    print("Integrity check complete.")
    for alert in alerts:
        print(alert)


if __name__ == "__main__":
    print("1. Create Baseline")
    print("2. Check Integrity")

    choice = input("Select option: ")

    if choice == "1":
        create_baseline()
    elif choice == "2":
        check_integrity()
    else:
        print("Invalid choice.")