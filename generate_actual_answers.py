"""Script to generate actual answers using domain_assistant.py."""
import sys
import shutil
from pathlib import Path
import domain_assistant

def main():
    ret = domain_assistant.main()
    if ret == 0:
        artifact_path = Path("artifacts/actual_answers.json")
        data_path = Path("data/actual_answers.json")
        if artifact_path.exists():
            data_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(artifact_path, data_path)
            print(f"Copied {artifact_path} -> {data_path}")
    return ret

if __name__ == "__main__":
    raise SystemExit(main())
