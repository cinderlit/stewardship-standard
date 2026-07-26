import json
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMAS_DIR = os.path.join(REPO_ROOT, "schemas")
SAMPLES_DIR = os.path.join(REPO_ROOT, "samples")


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def schema_path(*parts):
    return os.path.join(SCHEMAS_DIR, *parts)


def sample_path(filename):
    return os.path.join(SAMPLES_DIR, filename)
