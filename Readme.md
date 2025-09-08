# search-cli-pro

A simple cross-platform CLI tool to search the web directly from your terminal.
Supports multiple search engines and opens results in your favorite browser.

# Features

- Search across Google, Bing, DuckDuckGo, YouTube, Wikipedia, GitHub, Reddit, and StackOverflow.

- Works on macOS, Linux, and Windows.

- Optionally specify which browser to open (Safari, Chrome, Firefox, etc.).

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

List supported search engines:

        search --list

# Platform notes

- macOS : Supports custom browsers via -a
- Liux : Tries given browser, falls back to default if not found
- Windows : Opens in default browser (custom -a not supported yet)

# Development

Clone the repo and install in editable mode:

        git clone https://github.com/Hrishi11572/search-cli-pro.git
        cd search-cli-pro
        pip install -e .

Then run:

        search google "python argparse"

# License

MIT License - free to use, modify and share
