'''
helpers for URL encoding, browser handling
'''
# Standard library
import subprocess
import sys
import webbrowser
import shutil
import os


def is_browser_available(app: str) -> bool:
    if not app:
        return True  # default browser is always available
    
    # macOS
    if sys.platform.startswith("darwin"):
        # Check if the app exists in /Applications
        return os.path.exists(f"/Applications/{app}.app")
    
    # Linux / Windows
    return shutil.which(app) is not None


def open_in_browser(url : str, app : str | None = None) -> None:
    '''
    A utility to open a url in the specified browser (if given), otherwise in the default browser 
    (Supports macOS, linux, windows)
    '''
    if app :
        if sys.platform.startswith("darwin"): # macOS 
            subprocess.run(["open", "-a", app, url])
        elif sys.platform.startswith("linux"): 
            try: 
                subprocess.run([app.lower(), url])
            except FileNotFoundError: 
                print(f"Browser '{app}' not found. Opening in default browser ... ")
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
    