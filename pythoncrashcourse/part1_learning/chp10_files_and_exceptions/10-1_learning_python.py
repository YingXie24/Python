with open("learning/chp10_files_and_exceptions/toppoki_recipe.txt") as file_object:
    contents = file_object.read()

print(contents)

print("---------------")

with open("learning/chp10_files_and_exceptions/toppoki_recipe.txt") as file_object:
    for line in file_object:
        print(line.rstrip())

print("---------------")

with open("learning/chp10_files_and_exceptions/toppoki_recipe.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip().replace(",", "^_^"))