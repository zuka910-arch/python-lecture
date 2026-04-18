import requests


def main():
    response = requests.get("https://api.artic.edu/api/v1/artworks/search")
    print(response)
    content = response.json()
    print(content)


main()