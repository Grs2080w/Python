import requests


def check_internet():
    def check_internet1():
        """
        Checar a conexão de internet.
        :return:
        """
        url = 'https://www.google.com'
        timeout = 5
        try:
            requests.get(url, timeout=timeout)
            return True
        except requests.exceptions.ConnectionError:
            return False
    if not check_internet1():
        print('\033[31mInternet fora do ar!\033[m')
    else:
        print('\033[33mInternet OK!\033[m')