"""Helper to download a VOSK model archive and extract it to a target directory.

Usage:
    python download_model.py --url <model_url> --target models/model-small

This script streams the download to avoid high memory usage. It requires `requests`.
"""
import argparse
import os
import tarfile
import shutil

try:
    import requests
except Exception:
    print("requests is required: python -m pip install requests")
    raise


def download_and_extract(url, target_dir):
    os.makedirs(target_dir, exist_ok=True)
    local_archive = os.path.join(target_dir, "model.tar.gz")
    print(f"Downloading {url} to {local_archive}...")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_archive, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print("Extracting archive...")
    with tarfile.open(local_archive, "r:gz") as tar:
        tar.extractall(path=target_dir)
    os.remove(local_archive)
    print(f"Model downloaded and extracted to {target_dir}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--url", required=True, help="URL to model tar.gz file")
    p.add_argument("--target", required=True, help="Target directory for the model")
    args = p.parse_args()
    download_and_extract(args.url, args.target)
