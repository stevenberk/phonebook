
header1 = 'Electronic Phone Book\n' 
header2 = '=====================\n'
option1 = '1. Look up a number\n'
option2 = '2. Create an entry\n'
option3 = '3. Delete an entry\n'
option4 = '4. List all entries\n'
option5 = '5. Quit'
menu = header1 + header2 + option1 + option2 + option3 + option4 + option5
phonebookdict = { "test1" : "1", "test2" : "2", "test3" : "3"}
def run_phonebook():
    print menu
    number = raw_input('What do you want to do? (1-5)')
    if number == "1":
        contact = find_contact()
        print contact
        return True
    elif number == "2":
        contact2 = make_contact()
        print contact2
        return True
    elif number == "3":
        contact3 = delete_contact()
        print contact3
        return True
    elif number == "4":
        contact4 = list_contacts()
        print contact4
        return True
    elif number == "5":
        bye = goodbye()
        print bye
        return False
    else:
        print "invalid"
        return True
def find_contact():
    enter_name = raw_input('Enter name:')
    if enter_name in phonebookdict:
        return phonebookdict[enter_name]
    else:
        return "invalid"
def make_contact():
    set_entry_name = raw_input('Enter First Name:')
    set_entry_number = raw_input('Enter Thier Number:')
    phonebookdict[set_entry_name] = set_entry_number
    return phonebookdict
def delete_contact():
    enter_name = raw_input('Enter name:')
    del phonebookdict[enter_name]
    return phonebookdict
def list_contacts():
    return phonebookdict
def goodbye():
    return "Bye"
keep_running = True
while keep_running:     
    keep_running = run_phonebook()