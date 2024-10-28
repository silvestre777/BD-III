from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)


    #Solicitando dados para o usuario.

    print("\nAdicionando usuário.")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    #Funcao para armazenar os dados digitado a cima
    service.criar_usuario(nome= nome, email = email, senha=senha)
    
    #Listar todos os usuários cadastrados.
    print("\nListando usuários cadastrados.")
    listar_usuario = service.listar_todos_usuario()
    for usuario in listar_usuario:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")

if __name__ == "__main__":
    main()