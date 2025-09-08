import argparse
import urllib.parse 
import subprocess 
import sys
import webbrowser 


def main() : 
    # first parser to catch --list
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--list", action="store_true", help="List supported search engines")
    args, remaining = parser.parse_known_args()
    

    # mapping the engine names to correct URL: 
    engines = {
        "google" : "https://www.google.com/search?q={q}",
        "bing" : "https://www.bing.com/search?q={q}",
        "duckduckgo" : "https://duckduckgo.com/?q={q}",
        "youtube" : "https://www.youtube.com/results?search_query={q}",
        "wikipedia" : "https://en.wikipedia.org/wiki/Special:Search?search={q}",
        "stackoverflow" : "https://stackoverflow.com/search?q={q}",
        "github": "https://github.com/search?q={q}",
        "reddit": "https://www.reddit.com/search/?q={q}"
    };  
    
    if args.list:
        print("Supported search engines: ")
        for e in engines: 
            print(" -", e)
        sys.exit(0)

    # second parser (only if not listing)
    parser = argparse.ArgumentParser(description="A CLI package to search from terminal")
    parser.add_argument("engine" , help="Search engine (google, bing, duckduckgo)")
    parser.add_argument("query", help="The search query. For ex : `What's the weather today`")
    parser.add_argument("-a", "--app", help="The browser name (eg. Safari, Chrome, Firefox)")
    args = parser.parse_args(remaining)

    q = urllib.parse.quote_plus(args.query)
    engine = args.engine.lower()

    if engine not in engines: 
        print("Unsupported search engine")
        sys.exit(1)
    
    url = engines[engine].format(q=q)
    
    # Handle browser opening -- cross platform 
    if args.app: 
        if sys.platform.startswith("darwin"): # macOS 
            subprocess.run(["open", "-a", args.app, url])
        elif sys.platform.startswith("linux"): 
            try: 
                subprocess.run([args.app.lower(), url])
            except FileNotFoundError: 
                print(f"Browser '{args.app}' not found. Opening in default browser ... ")
                webbrowser.open(url)
        elif sys.platform.startswith("win"): 
            print("Custom browser (-a) not supported on windows. Opening in default browser ...")
            webbrowser.open(url)
        else:
            print("Unknown Platform. Opening in default browser ...")
            webbrowser.open(url)
    else:
        # default browser 
        webbrowser.open(url)


   