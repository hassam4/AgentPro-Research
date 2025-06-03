import os
import requests


def download_pdfs(papers, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    paths = []
    for idx, paper in enumerate(papers, start=1):
        pdf_url = paper.get("pdf_url")
        if not pdf_url:
            continue
        response = requests.get(pdf_url, timeout=15)
        if response.status_code == 200:
            path = os.path.join(output_dir, f"paper_{idx}.pdf")
            with open(path, "wb") as f:
                f.write(response.content)
            paths.append(path)
    return paths
