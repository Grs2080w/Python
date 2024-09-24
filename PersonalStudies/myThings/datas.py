import datetime


def data_atual():
    """
    Mostra a data atual, dd mm aa
    :return:
    """
    print(str(datetime.date.today().today()))


def dia_atual():
    """
    Mostra o dia atual, dd
    :return:
    """
    print(int(datetime.date.today().day))


def mes_atual():
    """
    Mostra a data do mes atual, mm
    :return:
    """
    int(datetime.date.today().month)


def ano_atual():
    """
    Mostra o ano atual, aa
    :return:
    """
    int(datetime.date.today().year)




