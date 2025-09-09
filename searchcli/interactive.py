'''
interactive multi-select UI
'''

# Standard library
import sys
import subprocess
import webbrowser

# Third-party
from InquirerPy import inquirer
from rich.console import Console  # Optional for fancy text formatting


console = Console()

def interactive_select(results, query):
    console.print(f"[bold] .... Preview .... [/bold]\n")
    console.print(f"\nTop 5 Results for: [bold]{query}[/bold]\n")
    
    for idx, r in enumerate(results, 1):
        snippet = r.get('snippet', '').replace('\n', ' ')
        if len(snippet) > 120:
            snippet = snippet[:120] + "…"
            
        console.print(f"[bold]{idx}. {r['title']}[/bold]")
        console.print(f"[dim]{snippet}[/dim]\n")

    # Now InquirerPy menu with plain numbers only
    choices = [f"{idx}. {r['title']}" for idx, r in enumerate(results, 1)]
    selected_indices = inquirer.checkbox(
        message="Select results to open:",
        choices=choices,
        instruction="[↑/↓ to navigate, Space to select, Enter to open]"
    ).execute()

    # Map back to full result dicts
    selected_results = [results[int(i.split('.')[0])-1] for i in selected_indices]
    return selected_results

def open_urls(results: list[dict[str, str]], app=None):
    """
    Open selected URLs in the default web browser.
    Fixes relative URLs starting with //
    """
    for r in results:
        url = r["url"]
        if url:
            if url.startswith("//"):
                url = "https:" + url
            # Open in specified app (macOS)
            if app and sys.platform.startswith("darwin"):
                try:
                    subprocess.run(["open", "-a", app, url])
                except FileNotFoundError:
                    print(f"Browser '{app}' not found. Opening default browser …")
                    webbrowser.open(url)
            else:
                webbrowser.open(url)
