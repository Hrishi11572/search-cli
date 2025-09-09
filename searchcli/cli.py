# Standard library
import argparse
import urllib.parse
import sys
import os
import threading

# Local imports
from searchcli.engines import ENGINES
from searchcli.utils import open_in_browser, is_browser_available
from searchcli.search import ddg_search
from searchcli.interactive import interactive_select, open_urls


def clear_terminal():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def main() : 
    # ---------------------------
    # First parser: handle --list
    # ---------------------------
    
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--list", action="store_true", help="List supported search engines")
    args, remaining = parser.parse_known_args()
    
    if args.list:
        print("Supported search engines: ")
        for e in ENGINES: 
            print(" -", e)
        sys.exit(0)

    # ---------------------------
    # Second parser: normal CLI
    # ---------------------------
    
    parser = argparse.ArgumentParser(description="A CLI package to search from terminal")
    parser.add_argument("engine" , help="Search engine (google, bing, duckduckgo)")
    parser.add_argument("query", help="The search query. For ex : `What's the weather today`")
    parser.add_argument("-a", "--app", help="The browser name (eg. Safari, Chrome, Firefox)")
    parser.add_argument("-i", "--interactive", action="store_true", help="Interactive mode: preview and select multiple results (DuckDuckGo only)")

    args = parser.parse_args(remaining)

    q = urllib.parse.quote_plus(args.query)
    engine = args.engine.lower()
    
    # ---------------------------
    # Pre-flight checks
    # ---------------------------
    
    # Engine check 
    if engine not in ENGINES: 
        print("Unsupported search engine")
        sys.exit(1)
        
    # Browser check 
    if args.app and not is_browser_available(args.app):
        print(f"Browser '{args.app}' not found on this system. Using default browser …")
        args.app = None
        
    url = ENGINES[engine].format(q=q)
    
    # ---------------------------
    # Interactive mode (DuckDuckGo)
    # ---------------------------
    
    if args.interactive:
        if engine != "duckduckgo":
            print("Interactive mode is only supported with DuckDuckGo for now.")
            open_in_browser(url, app=args.app)
            timer = threading.Timer(1.0, clear_terminal)
            timer.start()
            sys.exit(0)
        
        # DuckDuckGo interactive menu 
        clear_terminal()
        results = ddg_search(args.query, n=5)
        chosen = interactive_select(results, query=args.query)
        if chosen:
            open_urls(chosen, app=args.app)
            timer = threading.Timer(1.0, clear_terminal)
            timer.start()
        else:
            print("No results selected.")
        sys.exit(0)
    
    # ---------------------------
    # Normal search
    # ---------------------------
    
    open_in_browser(url, app=args.app)
    timer = threading.Timer(1.25, clear_terminal)
    timer.start()

   