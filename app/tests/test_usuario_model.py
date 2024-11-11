import pytest
from app.models.usuario_model import Usuario

@pytest.fixture
def criar_usuario():
    return Usuario("Silvestre", "silvestre1@gmail.com", "senha123")

def test_usuario_valido(criar_usuario):
    assert criar_usuario.nome == "Silvestre"
    assert criar_usuario.email == "silvestre1@gmail.com"
    assert criar_usuario.senha == "senha123"

def test_senha_invalida():
    with pytest.raises(ValueError, match="A senha deve ter pelo menos 6 caracteres."):
        Usuario("Silvestre", "silvestre1@gmail.com", "123")

def test_nome_vazio():
    with pytest.raises(ValueError, match="O nome não pode ser vazio."):
        Usuario("", "silvestre1@gmail.com","senha123")