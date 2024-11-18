import json

filename = "learning/chp10_files_and_exceptions/fav_num3.json"

try:
    with open(filename, 'r') as f:
        content = json.load(f)

except:
    fav_num = input("What is your favourite number? ")
    with open(filename, 'w') as f:
        json.dump(fav_num, f)
    print("We will remember your favourite number for the next time. ")

else:
    print(f"I know your favourite number! It is {content}! ")