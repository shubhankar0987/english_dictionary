import json

try:
    with open('j_eng_dict_database.json', 'r') as file:
        eng_dict = json.load(file)
except:
    eng_dict = {}

def dict_ser():
    print("Enter the word you want to find: ")
    ui = str(input("--> ")).lower()
    given_value = eng_dict.get(ui)
    if given_value is None:
        print("Sorry the word doesn't exsisted in our database.......")
        ui_to_add = str(input("Do you want to add this word and it's meaning to our database('Y/N'): ")).lower()
        if ui_to_add == 'y':
            ui_add_key = str(input("Enter the word: ")).lower()
            ui_add_value = str(input("Enter the above word meaning: "))
            eng_dict[ui_add_key] = ui_add_value
            print("----::::You word add to the dictionary successfully::::----")
    else:
        print(given_value)

def dict_view():
    for k, v in eng_dict.items():
        print(f"{k}: {v}")
    print("----::::This is the end of the Dictionary::::----")

def dict_delete():
    ui_add_key = str(input("Enter the word you want to delete: ")).lower()
    vaildate_key = eng_dict.get(ui_add_key)
    if vaildate_key is None:
        print("----:::: Sorry The word you entered, doesn't exist in our database ::::----")
    else:
        del eng_dict[ui_add_key]
        print("----::::The word you entered is successfully deleted from the dictionary::::----")

main_menu = """
        Choose the below options
    Enter '1' to 'Search a word's meaning'
    Enter '2' to 'View the whole dictionary'
    Enter '3' to 'Delete a word'
    Enter '4' to 'Save and Close the app'
"""

while True:
    print(main_menu)
    ui_f = int(input("Enter a number: "))
    if ui_f == 1:
        dict_ser()
    elif ui_f == 2:
        dict_view()
    elif ui_f == 3:
        dict_delete()
    elif ui_f == 4:
        print("----:::: THE DICTIONARY APP CLOSE SUCCESSFULLY ::::----")
        break

with open("j_eng_dict_database.json", 'w') as file:
    json.dump(eng_dict, file)






# if __name__ == '__main__':
#     dict()
