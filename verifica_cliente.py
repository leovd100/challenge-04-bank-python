from cria_produto import cria_produto

def verifica(value):
    age = value['age']
    uf = value['uf']
    renda = value['renda_mensal']
    list_emprestimo = [cria_produto('Eprestimo_pessoal', 4)]

    if renda >= 5000:
        if age <= 30:
            list_emprestimo.append( cria_produto('Emprestimo_com_garantia', 3))
        list_emprestimo.append(cria_produto('Credito_consignato', 2))
    elif renda >= 3000 and uf == 'sp' or (renda < 3000 and age <= 30 and uf == 'sp'):
        list_emprestimo.append( cria_produto('Emprestimo_com_garantia', 3))
    return list_emprestimo