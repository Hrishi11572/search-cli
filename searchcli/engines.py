'''
mapping of engines to URLs. This file contains all the search engines 
that are supported and their corresponding url formats as a dictionary 
'''

from searchcli.search import (
    ddg_search,
    wikipedia_search,
    arxiv_search,
    stackoverflow_search,
    github_search,
)


ENGINES = {
    # General search / news
    "google": {
        "url": "https://www.google.com/search?q={q}",
        "preview": None
    },
    "bing": {
        "url": "https://www.bing.com/search?q={q}",
        "preview": None
    },
    "duckduckgo": {
        "url": "https://duckduckgo.com/?q={q}",
        "preview": ddg_search
    },
    "yahoo": {
        "url": "https://search.yahoo.com/search?p={q}",
        "preview": None
    },
    "qwant": {
        "url": "https://www.qwant.com/?q={q}",
        "preview": None
    },

    # Academic / scientific
    "scholar": {
        "url": "https://scholar.google.com/scholar?q={q}",
        "preview": None
    },
    "arxiv": {
        "url": "https://arxiv.org/search/?query={q}&searchtype=all",
        "preview": arxiv_search
    },
    "pubmed": {
        "url": "https://pubmed.ncbi.nlm.nih.gov/?term={q}",
        "preview": None
    },
    "wikipedia": {
        "url": "https://en.wikipedia.org/wiki/Special:Search?search={q}",
        "preview": wikipedia_search
    },

    # Shopping / marketplaces
    "amazon": {
        "url": "https://www.amazon.com/s?k={q}",
        "preview": None
    },
    "ebay": {
        "url": "https://www.ebay.com/sch/i.html?_nkw={q}",
        "preview": None
    },

    # Social media
    "twitter": {
        "url": "https://twitter.com/search?q={q}",
        "preview": None
    },
    "instagram": {
        "url": "https://www.instagram.com/explore/tags/{q}/",
        "preview": None
    },

    # Q&A / forums
    "quora": {
        "url": "https://www.quora.com/search?q={q}",
        "preview": None
    },
    "reddit": {
        "url": "https://www.reddit.com/search/?q={q}",
        "preview": None
    },

    # Programming / dev
    "pypi": {
        "url": "https://pypi.org/search/?q={q}",
        "preview": None
    },
    "npm": {
        "url": "https://www.npmjs.com/search?q={q}",
        "preview": None
    },
    "stackoverflow": {
        "url": "https://stackoverflow.com/search?q={q}",
        "preview": stackoverflow_search
    },
    "github": {
        "url": "https://github.com/search?q={q}",
        "preview": github_search
    },

    # Maps / travel
    "maps": {
        "url": "https://www.google.com/maps/search/{q}",
        "preview": None
    },

    # Video / streaming
    "vimeo": {
        "url": "https://vimeo.com/search?q={q}",
        "preview": None
    },
    "youtube": {
        "url": "https://www.youtube.com/results?search_query={q}",
        "preview": None
    },
}
