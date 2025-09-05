# Starter file for students to create a Random Quote Generator

# Step 1: Import any necessary modules
# Step 2: Define a function to load quotes from a file when called
# Step 3: Define a function that returns a random quote when called
# Step 4: Define a main function that runs the program. Make sure to call the function.
import random
# Functions takes in filename parameter and returns list of strings with lines from file
def load_quotes(filename):
    with open (filename, 'r') as file:
        quotes = [line.strip() for line in file.readlines()]
    return quotes

# Function takes in list of strings and randomly chooses one to return
def get_random_quote(quotes):
    return random.choice(quotes)

def add_to_favorites(file_name, quote):
    with open(file_name, "a") as file:
        file.write(quote + "\n")

# Function returns a list of favorite quotes from file
def view_favorites(file_name):
    try:
        with open(file_name, "r") as file:
            favorites = [line.strip() for line in file.readlines()]
        return favorites
    except FileNotFoundError:
        return []

# Runs program. Main() is the only function called so that it calls the other functions appropriately and controls logic flow.
def main():
    quotes = load_quotes("quotes.txt")
    print("Loaded quotes:", quotes)  # Debug line
    if not quotes:
        print("No quotes found in quotes.txt!")
        return
    quote = get_random_quote(quotes)
    print("Random Quote:", quote)
    fav = input("Add to favorites? (yes/no): ").strip().lower()
    if fav == "yes":
        add_to_favorites("favorite_quotes.txt", quote)
        print("Quote added to favorites!")
    print("Your favorite quotes:")
    favorites = view_favorites("favorite_quotes.txt")
    for f in favorites:
        print(f)

main()


