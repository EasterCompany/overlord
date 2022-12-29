# Overlord library
from core.library import path, include, exists, console


def make_django_urls(client):
    """
    Automatically generates the URL patterns for your project using your clients __init__.py file

    :param client obj: a client class object from an __init__ file found within a client directory
    :return obj: path object from the django.urls library containing the url pattern for that client
    """
    client = client.Client()
    endpoint = client.ENDPOINT
    return path(endpoint, include([client.URL]), name=client.NAME)


def make_client_load_order(client_data, index):
    """
    Automatically generates which order to import and install clients. Load order decides which clients
    get priority of their declared url paths. The INDEX client will always load last and overwrite
    all other client urls so it can maintain the root path (ie; "http://www.easter.company/")

    :param client_data dict: dictionary container the '.config/clients.json' file
    :param index str: the name of the client you wish to be the index of your project
    :return str: a str styled as a list of client names with indentation for being injected into 'web/urls.py'
    """
    load_order = str()

    for client in client_data:
        if not client == index:
            load_order += f"    {client},\n"

    return load_order + f"    {index}"


def write_django_urls(load_order, urls_file_path):
    """
    Automatically generates the 'web/urls.py' file by using the <make_django_urls> & <make_client_load_order>
    functions

    :param load_order str: the results of the <make_client_load_order> function
    :param urls_file_path str: the path to the 'web/urls.py' file
    """

    with open(urls_file_path) as urls_file:
        file_content = urls_file.read()

    with open(urls_file_path, 'w+') as urls_file:
        urls_file.write(file_content.replace('__installed_clients_tag__', load_order))


def acquire_client_api(client:str, git_ssh:str, api_dir:str):
    """
    Automatically acquires installs an API from a git ssh link

    :param client str: name of the target client
    :param git_ssh str: ssh link to the git repository
    :param api_dir str: the directory of the new api
    """
    out = console.input(f"git clone {git_ssh} {client}", cwd=api_dir, show_output=True)
    return out


def acquire_all_clients_api(client_data:dict, cwd:str = '.'):
    """
    Automatically scan each client for any missing associated APIs which may have not already been installed

    :param client_data dict: a dictionary containing all the captured client data
    :param cwd str: current working directory of the server
    """
    for client in client_data:
        api_dir = f"{cwd}/api"
        if 'api' in client_data[client] and not exists(f"{api_dir}/{client}"):
            acquire_client_api(client, client_data[client]['api'], api_dir)


def write_api_urls():
    """
    Automatically generates the 'api/urls.py' file
    """
    return None
