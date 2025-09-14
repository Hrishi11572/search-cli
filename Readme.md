# search-cli-pro

A simple cross-platform CLI tool to search the web directly from your terminal.
Supports multiple search engines, interactive preview, and opens results in your favorite browser.

# Features

- Search across Google, Bing, DuckDuckGo, YouTube, Wikipedia, GitHub, Reddit, StackOverflow, and more.

- Interactive mode for DuckDuckGo, wikipedia, github , arxiv : preview top results, select multiple links, and open them at once.
  
- Works on macOS, Linux, and Windows.

- Optionally specify which browser to open (-a) — Safari, Chrome, Firefox, etc.

- Automatically clears the terminal before/after searches for a clean interface.
  
- Lightweight and easy to use.

# Installation

        pip install search-cli-pro

Or install directly from source:

        git clone https://github.com/Hrishi11572/search-cli-pro.git
        cd search-cli-pro
        pip install -e .

# Usage

Search google:

        search google "What's the weather today?"

Search Youtube:

        search youtube "lofi hip hop beats"

Search wikipedia:

        search wikipedia "Python programming"

Open with Safari (macOS):

        search google "machine learning" -a Safari

Interactive mode (DuckDuckGo , Wikipedia, Github , arxiv)

        search duckduckgo "python dataclasses" -i


List supported search engines:

        search --list

# Supported Search Engines
`search-cli-pro` currently supports the following engines:

### General search / news

- Google: search google "query"
- Bing: search bing "query"
- DuckDuckGo: search duckduckgo "query"
- Yahoo: search yahoo "query"
- Qwant (privacy-focused): search qwant "query"

### Academic / Scientific

- Google Scholar: search scholar "query"
- arXiv: search arxiv "query"
- PubMed: search pubmed "query"
- Wikipedia: search wikipedia "query"

### Shopping / Marketplaces

- Amazon: search amazon "query"
- eBay: search ebay "query"

### Social Media

- Twitter: search twitter "query"
- Instagram: search instagram "query"

### Q&A / Forums

- Quora: search quora "query"
- Reddit: search reddit "query"

### Programming / Developer

- PyPI: search pypi "query"
- npm: search npm "query"
- StackOverflow: search stackoverflow "query"
- GitHub: search github "query"

### Maps / Travel

- Google Maps: search maps "query"

### Video / Streaming

- Vimeo: search vimeo "query"
- YouTube: search youtube "query"

# Platform notes

- macOS : Supports custom browsers via -a
- Linux : Tries given browser, falls back to default if not found
- Windows : Opens in default browser (custom -a not supported yet)

# Development

Clone the repo and install in editable mode:

        git clone https://github.com/Hrishi11572/search-cli-pro.git
        cd search-cli-pro
        pip install -e . 

Then run:

        search google "python argparse"
        search duckduckgo "machine learning" -i

# License

MIT License - free to use, modify and share
