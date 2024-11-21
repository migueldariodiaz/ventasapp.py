import pyfiglet

# Instancia para texto grande "DeppSale" desde la libreria pyfiglet
deepsale_title = pyfiglet.figlet_format('DeppSale')


clients = 'miguel,sybell,'


def crear_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already in the client\'s list')


def list_client():
    global clients

    print(clients)


def _add_comma():
    global clients

    clients += ','


def _print_welcome():
    print(deepsale_title)
    print('Welcome to DeepSale')
    print('What would you like to do today?')
    print('')
    print('[C]reate a client')
    print('[D]elete a client')


if __name__ == '__main__':
    _print_welcome()
    command = input()
    if command == 'C':
        client_name = input('What is the client name? ')
        crear_client(client_name)
        list_client()
    elif command == 'D':
        pass
    else:
        print('Invalid command')
    pass
