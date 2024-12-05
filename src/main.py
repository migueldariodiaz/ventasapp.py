import pyfiglet
import sys

# Instancia para texto grande "DeppSale" desde la libreria pyfiglet
deepsale_title = pyfiglet.figlet_format('DeppSale')


clients = [
    {
        'name': 'Miguel',
        'company': 'Weir Minerals',
        'email': 'miguel.diaz@weir.com',
        'position': 'Development Engineer'
    },
    {
        'name': 'Sybell',
        'company': 'Camara Comercio Santiago',
        'email': 'sybell.alejandria@ccs.cl',
        'position': 'Gerente fidelizacion clientes'
    }
]


def crear_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in the client\'s list')


def list_client():
    global clients

    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client['name']))


def update_client(clients, update_client_name):
    index = 0

    for client in clients:
        if client["name"] == update_client_name:
            clients[index] = {
                'name': _get_client_field('name'),
                'company': _get_client_field('company'),
                'email': _get_client_field('email'),
                'position': _get_client_field('position')
            }
            break
        else:
            index += 1
        print("No se encontro al cliente")


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        _print_message_not_client_in_list()


def search_client(client_name):
    global clients
    
    for client in clients:
        if client_name != client:
            continue
        else:
            return True


def _print_welcome():
    print(deepsale_title)
    print('Welcome to DeepSale')
    print('What would you like to do today?')
    print('')
    print('[C]reate a client')
    print('[L]ist clients')
    print('[U]pdate a client')
    print('[D]elete a client')
    print('[S]earch a client')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}? '.format(field_name))
    return field


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
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        crear_client(client)
        list_client()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_client()
    elif command == 'U':
        update_client_name = input('What is the update client name? ')
        update_client(clients, update_client_name)
        list_client()
    elif command == 'L':
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
