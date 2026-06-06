import requests
def main():
    user_input = input("Artist name: ")
    artworks = get_artwork(query = user_input, limit = 3)
    artists = get_artists(query = user_input, limit = 3)
    print(artworks) 
    #print(artists)

def get_artwork(query, limit):
    response = requests.get("https://api.artic.edu/api/v1/artworks/search", params={"q": query, "limit": limit})

    content = response.json()
    result = [artwork["title"] for artwork in content["data"]]
    return result

def get_artists(query, limit):
    response = requests.get("https://api.artic.edu/api/v1/agents/search", params={"q": query, "limit": limit})
    content = response.json()
    return [artists["title"] for artists in content["data"]]
   

main()