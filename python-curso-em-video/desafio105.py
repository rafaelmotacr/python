# Analisando e gerando dicionários

def notas (* nota, sit = False):
    """
    > Funçao para analisar notas e situaçoes de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou nao adicionar a descriçao ao dicionário.  
    :return: dicionário com várias informaçoes sobre a situaçao da turma.
    """
    turma = {'total': len(nota), 'maior': max(nota), 'menor': min(nota), 'média': sum(nota) / len(nota)}
    if sit:
        turma['situação'] = 'RUIN'
        if turma['média'] >= 7:
            turma['situação'] = 'BOA'
        elif turma['média'] >= 5:
            turma['situação'] = 'RAZOÁVEl'
    return turma


p = notas(3,2.5,1,4,7.3, sit = False)
print(p)
