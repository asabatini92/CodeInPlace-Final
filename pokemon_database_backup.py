import csv

def main():
    pokedex = load_pokedex_from_csv('pokemon_game.csv')
    print("")
    print("Welcome to Pokédex: From 001 to 151, where you'll find stats for Gen 1 Pokémon!")
    pokemon = input("Name a Pokémon, and I'll tell you all about it!: ")

    score = 0

    if pokemon in pokedex:
        print(f"A wild {pokemon} was caught!")
        print("Type:", pokedex[pokemon]["type"])
        print("HP:", pokedex[pokemon]["HP"])
        print("Attack:", pokedex[pokemon]["Attack"])
        print("Defense:", pokedex[pokemon]["Defense"])
    else:
        print(f"{pokemon} is not found in the Kanto region. Try again!")



def load_pokedex_from_csv(filepath):
    """
    Loads Pokémon data from a CSV file into a dictionary.
    Returns a dictionary with Pokémon names as keys and their stats as values.
    """
    pokedex = {}
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            pokedex[name] = {
                'type': row['Type'],
                'HP': int(row['HP']),
                'Attack': int(row['Attack']),
                'Defense': int(row['Defense'])
            }
    return pokedex



























if __name__ == "__main__":
    main()





 #pokedex = {
        #"Bulbasaur": {"type": "Grass", "HP": 45, "Attack": 49, "Defense": 49},
        #"Charmander": {"type": "Fire", "HP": 39, "Attack": 52, "Defense": 43},
        #"Squirtle": {"type": "Water", "HP": 44, "Attack": 48, "Defense": 65}
    #}