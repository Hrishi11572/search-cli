'''
mapping of engines to URLs. This file contains all the search engines 
that are supported and their corresponding url formats as a dictionary 
'''
ENGINES = {
        # General search / news
        "google" : "https://www.google.com/search?q={q}",
        "bing" : "https://www.bing.com/search?q={q}",
        "duckduckgo" : "https://duckduckgo.com/?q={q}",
        "yahoo": "https://search.yahoo.com/search?p={q}",
        "qwant": "https://www.qwant.com/?q={q}",  # privacy-focused search

        # Academic / scientific
        "scholar": "https://scholar.google.com/scholar?q={q}",
        "arxiv": "https://arxiv.org/search/?query={q}&searchtype=all",
        "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term={q}",
        "wikipedia" : "https://en.wikipedia.org/wiki/Special:Search?search={q}",


        # Shopping / marketplaces
        "amazon": "https://www.amazon.com/s?k={q}",
        "ebay": "https://www.ebay.com/sch/i.html?_nkw={q}",
        
        # Social media
        "twitter": "https://twitter.com/search?q={q}",
        "instagram": "https://www.instagram.com/explore/tags/{q}/",
        
        # Q&A / forums
        "quora": "https://www.quora.com/search?q={q}",      
        "reddit": "https://www.reddit.com/search/?q={q}",
        
        # Programming / dev
        "pypi": "https://pypi.org/search/?q={q}",
        "npm": "https://www.npmjs.com/search?q={q}",
        "stackoverflow" : "https://stackoverflow.com/search?q={q}",
        "github": "https://github.com/search?q={q}",

        # Maps / travel
        "maps": "https://www.google.com/maps/search/{q}",
        
        # Video / streaming
        "vimeo": "https://vimeo.com/search?q={q}",
        "youtube" : "https://www.youtube.com/results?search_query={q}",
}

