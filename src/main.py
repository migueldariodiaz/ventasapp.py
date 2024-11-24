import pyfiglet
import sys

# Instancia para texto grande "DeppSale" desde la libreria pyfiglet
deepsale_title = pyfiglet.figlet_format('DeppSale')


clients = 'miguel,sybell,alonso,'


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


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
    else:
        _print_message_not_client_in_list()


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        _print_message_not_client_in_list()


def search_client(client_name):
    global clients
    clients_list = clients.split(',')
    
    for client in clients_list:
        if client_name != client:
            continue
        else:
            return True


def _add_comma():
    global clients

    clients += ','


def _print_welcome():
    print(deepsale_title)
    print('Welcome to DeepSale')
    print('What would you like to do today?')
    print('')
    print('[C]reate a client')
    print('[U]pdate a client')
    print('[D]elete a client')
    print('[S]earch a client')


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _print_message_not_client_in_list():
    print('Client is not in client\'s list')


if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        crear_client(client_name)
        list_client()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_client()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the update client name? ')
        update_client(client_name, update_client_name)
        list_client()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('Client {} is in client\'s list'.format(client_name))
        else:
            print('Client {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')
