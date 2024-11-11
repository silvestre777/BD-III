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
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("", "silvestre1@gmail.com", "12345")

def test_usuario_tipo_nome_invalido():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario(000, "silvestre1@gmail.com", "12345") 

def test_usuario_email_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("maria", "", "12345")

def test_usuario_email_invalido():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario("Silvestre", 000, "12345")  

def test_usuario_senha_vazia_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("Silvestre", "silvestre1@gmail.com", "")

def test_usuario_senha_invalida():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario("Silvestre", "silvestre1@gmail.com", 12665)  