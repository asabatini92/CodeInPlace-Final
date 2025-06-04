import csv

def main():
    pokedex = load_pokedex_from_csv('pokemon_game.csv')
    print("")
    print("Welcome to Pokédex: From 001 to 151, where you'll find stats for Gen 1 Pokémon!")
    print("You've got 5 rounds to catch some wild Pokémon. Type a Pokémon's name to scan its stats.")
    print("")   
    
    #keeps track of the score
    score = 0
    rounds = 0

    while rounds < 5:
        pokemon = input("Throw a PokéBall, you gotta catch 'em all!: ")
        if pokemon in pokedex:
            score += 1
            # Display Pokémon stats
            print(f"A wild {pokemon} was caught!")
            print("Type:", pokedex[pokemon]["type"])
            print("HP:", pokedex[pokemon]["HP"])
            print("Attack:", pokedex[pokemon]["Attack"])
            print("Defense:", pokedex[pokemon]["Defense"])
            print("")
        else:
            print(f"Sorry, {pokemon} is not found in the Kanto region. Try again!")
            print("")
        rounds += 1
            
    print(f"You caught {score}/5 Pokémon! Play again to catch more!")



#Makes CSV file readable in Python
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




