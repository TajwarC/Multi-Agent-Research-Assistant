import requests

def fetch_citations(query: str):
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,url"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()["data"]
    return []
