'''
logic to fetch & parse results (API/scraping)
'''
# Third-party
import requests
from bs4 import BeautifulSoup

def ddg_search(query: str, n: int = 5) -> list[dict[str, str]]:
    """
    Return top n DuckDuckGo results as a list of dicts:
    {title, url, snippet}.
    """
    url = "https://duckduckgo.com/html/"
    params = {"q": query}
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, params=params, headers=headers, timeout=5)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    results = []

    for i, a in enumerate(soup.select(".result__a")):
        if i >= n:
            break
        title = a.get_text(strip=True)
        link = a["href"]

        snippet_tag = a.find_parent("div", class_="result").select_one(".result__snippet")
        snippet = snippet_tag.get_text(strip=True) if snippet_tag else ""

        results.append({"title": title, "url": link, "snippet": snippet})

    if not results:
        results.append({"title": "No results found", "url": "", "snippet": ""})

    return results
