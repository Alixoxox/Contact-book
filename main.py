def welcome():
    print("-" * 50)
    print("Welcome to this App.\nHope you will enjoy using it")
    print("\tHow would you like to proceed?\n\t1.Create account\n\t2.Login\n\t3.Exit")

def create_acc(dict_user):
    nme = input("Enter your name: ")
    while True:
        log = input("Enter a username: ")

        if log in dict_user:
            print("Username already taken. Please choose another one.")
        else:
            break

    while True:
        pas = input("Enter a password (7 or more characters): ")
        if len(pas) >= 7:
            print('Account created successfully.')
            break
        else:
            print('Password should be 7 or more characters.')

    save_user_info(dict_user, nme, log, pas)

def login(dict_user):
    log = input("Enter your username: ")
    pas = input("Enter your password: ")

    if log in dict_user and dict_user[log] == pas:
        print('Successfully logged in. Good job!')
    else:
        print('Invalid username or password.')
        while True:
            v = input('Would you like to create a new account? (yes/no)').lower()
            if v == 'yes':
                create_acc(dict_user)
                break
            elif v == 'no':
                login(dict_user)
                break
            else:
                print("Please enter yes/no value!")

# Save Info
def save_user_info(dict_user, nme, log, pas):
    dict_user[log] = pas

    with open('user_file.txt', 'a+') as file:
        file.write(f'{nme}:{log}:{pas}\n')

def load_user_info(dict_user):
    with open('user_file.txt', 'r') as file:
        contents = file.read()

    modif_contents = contents.split('\n')

    for line in modif_contents:
        if line:
            name, username, password = line.split(':')
            dict_user[username] = password

def update_content(dict_peeps):
    with open('file_contacts.txt', 'w') as f:
        for name, details in dict_peeps.items():
            f.write(f'{name}:{details["phone"]}:{details["email"]}:{details["address"]}\n')

def load_old_contents(dict_peeps):
    with open('file_contacts.txt', 'r') as file:
        contents = file.readlines()

    for line in contents:
        parts = line.strip().split(":")
        if len(parts) == 4:
            name, phone, email, address = parts
            dict_peeps[name] = {'phone': phone, 'email': email, 'address': address}

#_______________________________________________________________________________________________________________#
def menu(dict_peeps):
    while True:
        print("-" * 50)
        print(f'What would you like to do?\n\t1.ADD CONTACT\n\t2.REMOVE CONTACT\n\t3.VIEW CONTACTS\n\t4.EDIT CONTACTS\n\t5.EXIT') 
        while True:
            c = input("Enter the value of operation: ")
            if c.isdigit():
                try:
                    load_old_contents(dict_peeps)
                except Exception as e:
                    print(e)

                if c == '1':
                    create_content(dict_peeps)
                    break
                elif c == '2':
                    del_content(dict_peeps)
                    break
                elif c == "3":
                    view_contents(dict_peeps)
                    break
                elif c == '4':
                    edit_content(dict_peeps)
                    break
                elif c == '5':
                    update_content(dict_peeps)
                    return True
              
            else:
                print('Please enter a valid operation')

def create_content(dict_peeps):
    while True:
        while True:
            name = input("Enter name: ")
            if name in dict_user:
                print("Username already taken. Please choose another one.")
            else:
                break 

        while True:
            phone = input("Enter phone no: ")
            if phone.isdigit():
                break
            else:
                print("Retry.\nEnter numeric values only")

        while True:
            email = input("Enter email address: ")
            if email.endswith('@gmail.com'):
                break
            else:
                print("Please enter a valid email address")

        address = input("Enter address: ")
        print(f"Contact info of {name} has been successfully saved.\nGood Job!")
        dict_peeps[name] = {'phone': phone, 'email': email, 'address': address}

        isb=input("Do u wish to enter another contact info:\nType (yes/no): ").lower()
        if isb.isalpha():
            if isb == 'no':

                try :
                    update_content(dict_peeps)
                except Exception as e:
                    print(e)

                break
            else:
                pass
        else:
            print("Please enter or answer in alphabets")

def del_content(dict_peeps):
    view_contents(dict_peeps)
    name = input("Enter the contact-name you want to remove: ") 
    if name in dict_peeps:
        print('This contact shall now be deleted')
        while True:
            confirm = input('Are you sure you want to delete it?\nInput Yes Or NO: ').lower()
            if confirm.isalpha():
                if confirm == 'yes':
                    print('This shall be deleted now')
                    del dict_peeps[name]
                    update_content(dict_peeps)
                    break
                elif confirm == 'no':
                    break
                else:
                    print('Please select a valid input. Either (yes or no)')
            else:
                print("The input value entered is not yes or no")
    else:
        print(f'Sorry!\nThe contact-name {name} entered is not in the contact book')


def view_contents(dict_peeps):
    with open('file_contacts.txt', 'r') as file:
        contents = file.readlines()

    print('.' * 25)
    for line in contents:
        parts = line.strip().split(":")

        if len(parts) > 0:
            formatted_result = f"{line}. name:{parts[0]}\n  phone:{parts[1]}\n  email:{parts[2]}\n  address:{parts[3]}"
            
            print(formatted_result)
            print('.' * 25)


def edit_content(dict_peeps):
    view_contents(dict_peeps)
    o = input("Would you like to edit one of these contacts?\nType (yes/no)").lower()

    if o == 'yes':
        name_to_edit = input("Enter the contact name you want to edit: ")

        if name_to_edit in dict_peeps:
            while True:
                print("What information do you want to change?\n\t1. Name\n\t2. Phone number\n\t3. Email\n\t4. Address\n\t5. Exit")

                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    new_name = input("Enter the new name: ")
                    dict_peeps[new_name] = dict_peeps[name_to_edit]
                    del dict_peeps[name_to_edit]
                    print("Name updated successfully!")
                    break

                elif choice == '2':
                    new_phone = input("Enter the new phone number: ")
                    dict_peeps[name_to_edit]['phone'] = new_phone
                    print("Phone number updated successfully!")
                    break

                elif choice == '3':
                    new_email = input("Enter the new email address: ")
                    dict_peeps[name_to_edit]['email'] = new_email
                    print("Email address updated successfully!")
                    break

                elif choice == '4':
                    new_address = input("Enter the new address: ")
                    dict_peeps[name_to_edit]['address'] = new_address
                    print("Address updated successfully!")
                    break

                elif choice == '5':
                    print("Exiting edit mode.")
                    break

                else:
                    print("Invalid choice. Please enter a number from 1 to 5.")

            # Save changes to file
            update_content(dict_peeps)

        else:
            print(f"The contact name '{name_to_edit}' is not in the contact book.")
        
    elif o == 'no':
        print("Redirecting back to home.")

    else:
        print("Invalid value entered. Redirecting back to home.")

###_____________MAIN PROGRAM____________________
dict_user = {}
dict_peeps = {}

while True:
    load_user_info(dict_user)
    welcome()
    p = input('Enter your choice from 1-3 ONLY: ')
    if p == '1':
        create_acc(dict_user)
        menu(dict_peeps)
        break
    elif p == '2':
        login(dict_user)
        menu(dict_peeps)
        break
    elif p == '3':
        break
    else:
        print('You entered invalidly. Please try again.')