def notas(*num, sit=False):
    """
Calcula estatísticas sobre as notas digitadas.

    :param num: Recebe qualquer quantidade de valores, seja float ou int, e usa esses valores
    para fazer a média.

    :param sit: Se sit=false (padrão), ele não mostra a situação, se sit=True, ele mostra a situação.

    :return: Retorna quantidade de valores, maior e menor nota, a média e se sit=True, a situação em um dicionário.
    """
    notas_s = dict()
    notas_s['Total'] = len(num)
    notas_s['MaiorNota'] = max(num)
    notas_s['MenorNota'] = min(num)
    notas_s['Média'] = sum(num) / len(num)
    if not sit:
        return notas_s

    if sit:
        if notas_s['Média'] >= 7:
            notas_s['Situação'] = 'Aprovado'
        elif 5 < notas_s['Média'] < 7:
            notas_s['Situação'] = 'Recuperação'
        else:
            notas_s['Situação'] = 'Reprovado'
        return notas_s


print(notas(6, 2, 3, 7, 10, 11, 12, sit=True))