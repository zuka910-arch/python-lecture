SHOWS = [
    "  Avatar: The Last Airbender",
    "ben 10",
    "Arthur",
    " spongebob squarepants",
    "phineas and ferb",
    " kim possible        ",
    "jimmy neutron",
    "the proud family",
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
    
    print(", ".join(cleaned_shows))
    
    for cleaned_show in cleaned_shows:
            print(cleaned_show)
main()