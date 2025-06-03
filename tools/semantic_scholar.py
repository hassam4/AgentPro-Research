import requests


API_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
FIELDS = "title,url,openAccessPdf"


def search_papers(query: str, limit: int = 5):
    """Search Semantic Scholar for papers."""
    params = {"query": query, "limit": limit, "fields": FIELDS}
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    papers = []
    for paper in data.get("data", []):
        pdf_url = None
        open_access = paper.get("openAccessPdf")
        if open_access and "url" in open_access:
            pdf_url = open_access["url"]
        papers.append({
            "title": paper.get("title"),
            "url": paper.get("url"),
            "pdf_url": pdf_url,
        })
    return papers
