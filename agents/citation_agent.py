import requests

def fetch_citations(query: str):
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,url"
    try:
        res = requests.get(url)
        res.raise_for_status()  # raises HTTPError for bad status codes
        json_data = res.json()
        
        if "data" in json_data:
            return json_data["data"]
        else:
            print("⚠️ 'data' key not in response:", json_data)
            return []

    except requests.exceptions.RequestException as e:
        print(f"🚨 Request failed: {e}")
        return []
