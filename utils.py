from models import Pessoas, Usuarios

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

def insere_usuarios(login, senha):
     usuario = Usuarios(login=login, senha=senha)
     usuario.save()

def consulta_todos_usuarios():
    usuario = Usuarios.query.all()
    print(usuario)


if __name__ == '__main__':
    insere_usuarios('alexandre', '1234')
    insere_usuarios('pietra', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoas()
    # exclui_pessoa()
    # consulta_pessoas()
