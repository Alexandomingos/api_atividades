from models import Pessoas

#Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Domingos', idade=32)
    print(pessoa)
    pessoa.save()

#Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoas = Pessoas.query.filter_by(nome='Alexandre').first()
    print(pessoas.idade)
#altera dados na tabela pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Domingos').first()
    pessoa.nome = 'Pietra'
    pessoa.save()

#Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoas = Pessoas.query.filter_by(nome='Domingos').first()
    pessoas.delete()


if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoas()
    exclui_pessoa()
    consulta_pessoas()
