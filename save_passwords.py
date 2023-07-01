print('Welcome to "password saver"!\nWrite "help" to see commands.')


def req_pwd():
    web = input('Website name: ')
    passwd = input('Password: ')
    with open('passwords.log', 'a') as log:
        print(web+':', passwd, file=log)


def read_pwd():
    with open('passwords.log') as log:
        cont = log.read()
    return cont


while True:
    command = input()
    if command == 'save_pwd':
        req_pwd()
    elif command == 'show_pwds':
        print(read_pwd())
    else:
        print('Command not found.')
