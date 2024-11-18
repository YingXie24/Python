names = {
    'ying': 'xie',
    'andrei': "gorbatch",
    "jeremy": "ooi",
    "alina": "gorbatch"
    }

# add another item in the dictionary
names["teh heng"] = "chia"
print(names)

desired_peoples = ["jack", "alina", "dasha"]
for desired_people in desired_peoples:
    if desired_people in names.keys():

        
        print(f"{desired_people.title()}, thanks for responding.")
    else: 
        print(f"{desired_people.title()}, please take the poll.")