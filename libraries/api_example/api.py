import sys
import requests


def main():
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search" , {"q": "van gogh"})
    except requests.HTTPError:
        print("An error occurred while making the request.")
        sys.exit(1)
    content = response.json()
    for artwork in content["data"]:
        print(f"{artwork['title']}")
    

main()