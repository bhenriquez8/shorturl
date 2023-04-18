from pyshorteners import Shortener
from pyshorteners.exceptions import ShorteningErrorException
import pyperclip
import platform, subprocess, sys

def check_os():
    os_name = platform.system()

    if os_name == "Linux":
        try:
            cmd = ["dpkg-query", "-W", "xclip"]
            subprocess.check_output(cmd)
        except subprocess.CalledProcessError:
            print("Detected Debian based OS. Required 'sudo apt install xclip' to copy to clipboard.")

def short_url():
    url = input("Enter url to shorten: ")

    try:
        short = Shortener().dagd.short(url)
    except ShorteningErrorException:
        print("couldn't shorten or invalid url")
        sys.exit()

    try:
        pyperclip.copy(short)
    except pyperclip.PyperclipException as e:
        print("An error occurred while copying to the clipboard: ", e)
    finally:
        print(f"\nCopied to clipboard! {short}")

if __name__ == '__main__':
    check_os()
    short_url()