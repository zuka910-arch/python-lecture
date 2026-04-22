import requests

def main():
  response = requests.get("https://catfact.ninja/fact")  
  contents = response.json()
  print(contents)

main()