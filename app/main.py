from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    def cadastrar_usuario():
        print("\nAdicionando usuário.")
        nome = input("Digite seu nome: ")
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")
    #Funcao para armazenar os dados digitado a cima
        service.criar_usuario(nome= nome, email = email, senha=senha)


    #Solicitando dados para o usuario.
    print(f"\n== Tabela de serviços disponiveis ==")
    print(f"1- Cadastrar Usuário")
    print(f"2- Atualizar cadastro")
    print(f"2- Consultar Usuário")
    print(f"3- Excluir Usuário")
    print(f"4- Listar Usuário")
    opcao = input("Digite a opção desejada: ")

    if opcao == 1:
        cadastro = cadastrar_usuario()
        return 
    

    if opcao == 2:
        print("dfwqdqw")


    #Listar todos os usuários cadastrados.


    print("\nListando usuários cadastrados.")
    listar_usuario = service.listar_todos_usuario()
    for usuario in listar_usuario:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")

if __name__ == "__main__":
    main()