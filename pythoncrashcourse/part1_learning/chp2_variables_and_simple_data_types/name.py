# string methods
name = "ada lovelace"
print(name.title())
print(name.capitalize())
print(name.upper())

# string concatenation
first_name = "amanda"
last_name = "ong"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

# Whitespace
print("\tPython")
print("\nPython\nJavaScript\nC")
favorite_language = ' Python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

print(favorite_language)
favorite_language = favorite_language.strip() #To remove the whitespace permanently, store the stripped value back into the variable
print(favorite_language)