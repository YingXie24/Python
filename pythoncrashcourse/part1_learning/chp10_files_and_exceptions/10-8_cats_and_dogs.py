kombucha = "learning/chp10_files_and_exceptions/kombucha_recipe.txt"
toppoki = "learning/chp10_files_and_exceptions/toppoki_recipe.txt"
files = [kombucha, 'green_curry.txt', toppoki]

def count_word(file):

    try:
        with open(file) as f:
            content = f.read()

    except FileNotFoundError:
        print(f"The file {file} is missing. ")
        print("\n------\n")
        # pass
    
    else: 
        number = content.lower().count('it')
        print(f"There are {number} occurences of the word 'it' in the recipe {file}. ")
        print("\n------\n")

for file in files:
    count_word(file)
    
