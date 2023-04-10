from cryptography.fernet import Fernet

'''
# these lines will only run for the first time to generate your key

def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)

write_key()
'''

def read_key():
    with open("key.key", "rb") as f:
        generated_key = f.read()
        return generated_key

fer = Fernet(read_key())

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            name, passw = line.rstrip().split('|')
            print(name, '|', fer.decrypt(passw.encode()).decode())

def add():
    name = input("Enter title: ")
    pwd = input("Enter password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')

while True:
    mode = input("Want to add password or view? (Enter add/view or q to quit) ").lower()

    if(mode == "q"):
        quit()

    if(mode == "view"):
        view()
    
    elif (mode == "add"):
        add()

    else:
        print("Valid option not entered !!!")
        continue
