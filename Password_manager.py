# from cryptography.fernet import Fernet 

pwd = input('What is the password?')
print(b'hello')
print('hello')

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
              data  = line.rstrip()
              user, passw = data.split("|")
              print ('User: ', user, '| Password: ', passw)
              
def add():
    name = input('Account Name: ')
    pwsd = input('Password: ')
    
    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + pwsd + '\n')

while True:
        mode = input('Would you like to add a new password or view existing ones (View,Add) or q to Quit ').lower()
        if mode == "q":
            break
        
        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print('Invalid mode.')
            continue
        
            
 