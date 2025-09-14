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


def wikipedia_search(query: str, n: int = 5):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
    }

    headers = {
        "User-Agent": "search-cli-pro/1.0 (https://pypi.org/project/search-cli-pro/)"
    }

    try:
        res = requests.get(url, params=params, headers=headers, timeout=10)
        res.raise_for_status()
        data = res.json()
    except Exception as e:
        return [{"title": "Error", "url": "", "snippet": str(e)}]

    results = []
    for item in data.get("query", {}).get("search", [])[:n]:
        results.append({
            "title": item["title"],
            "url": f"https://en.wikipedia.org/wiki/{item['title'].replace(' ', '_')}",
            "snippet": item["snippet"]
                .replace("<span class=\"searchmatch\">", "")
                .replace("</span>", "")
        })

    return results

        
def arxiv_search(query: str, n: int = 5):
    url = "http://export.arxiv.org/api/query"
    params = {"search_query": query, "start": 0, "max_results": n}
    res = requests.get(url, params=params)
    import xml.etree.ElementTree as ET
    root = ET.fromstring(res.text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    results = []
    for entry in root.findall("atom:entry", ns):
        results.append({
            "title": entry.find("atom:title", ns).text.strip(),
            "url": entry.find("atom:id", ns).text.strip(),
            "snippet": entry.find("atom:summary", ns).text.strip()
        })
        
    return results

def stackoverflow_search(query: str, n: int = 5):
    url = "https://api.stackexchange.com/2.3/search/advanced"
    params = {
        "order": "desc",
        "sort": "relevance",
        "q": query,
        "site": "stackoverflow",
        "pagesize": n,
    }
    res = requests.get(url, params=params).json()
    results = []
    for item in res.get("items", []):
        results.append({
            "title": item["title"],
            "url": item["link"],
            "snippet": f"Score {item['score']} | Answers {item['answer_count']}"
        })
        
    return results

def github_search(query: str, n: int = 5):
    url = "https://api.github.com/search/repositories"
    params = {"q": query, "per_page": n}
    res = requests.get(url, params=params).json()
    results = []
    for item in res.get("items", []):
        results.append({
            "title": item["full_name"],
            "url": item["html_url"],
            "snippet": item["description"] or "(no description)"
        })
        
    return results
