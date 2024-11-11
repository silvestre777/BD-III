import pytest
from app.models.usuario_model import Usuario

@pytest.fixture
def criar_usuario():
    return Usuario("Silvestre", "silvestre1@gmail.com", "senha123")

def test_usuario_valido(criar_usuario):
    assert criar_usuario.nome == "Silvestre"
def test_email_valido(criar_usuario):
    assert criar_usuario.email == "silvestre1@gmail.com"
def test_senha_valido(criar_usuario):
    assert criar_usuario.senha == "senha123"

def test_usuario_nome_vazio():
    with pytest.raises(ValueError, match="O nome não pode ser vazio."):
        Usuario("", "silvestre1@gmail.com", "12345")

def test_usuario_tipo_nome_invalido():
    with pytest.raises(TypeError, match="Nome inválido."):
        Usuario(000, "silvestre1@gmail.com", "12345") 

def test_usuario_email_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O email não pode ser vazio."):
        Usuario("Silvestre", "", "12345")

def test_usuario_email_invalido():
    with pytest.raises(TypeError, match="Email inválido."):
        Usuario("Silvestre", 000, "12345")  

def test_usuario_senha_vazia_erro():
    with pytest.raises(ValueError, match="A senha não pode ser vazia."):
        Usuario("Silvestre", "silvestre1@gmail.com", "")

def test_usuario_senha_invalida():
    with pytest.raises(TypeError, match="Senha inválida."):
        Usuario("Silvestre", "silvestre1@gmail.com", 12665)  