import pytest
from app.models.usuario_model import Usuario, EmailInvalidoError, SenhaInvalidaError

@pytest.fixture
def criar_usuario():
    # Criando um usuário válido para outros testes
    return Usuario("Silvestre", "silvestre1@gmail.com", "senha123")

def test_email_invalido():
    # Testando email inválido
    with pytest.raises(EmailInvalidoError, match="O email fornecido é inválido."):
        Usuario("Silvestre", "emailinvalido", "senha123")

def test_senha_invalida():
    # Testando senha inválida (menos de 6 caracteres)
    with pytest.raises(SenhaInvalidaError, match="A senha deve ter pelo menos 6 caracteres."):
        Usuario("Silvestre", "silvestre1@gmail.com", "123")

def test_usuario_valido(criar_usuario):
    # Teste para garantir que um usuário válido seja criado
    assert criar_usuario.nome == "Silvestre"
    assert criar_usuario.email == "silvestre1@gmail.com"
    assert criar_usuario.senha == "senha123"
