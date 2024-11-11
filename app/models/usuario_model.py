import re
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.database import db

# Exceções Personalizadas
class EmailInvalidoError(ValueError):
    pass

class SenhaInvalidaError(ValueError):
    pass

Base = declarative_base()

class Usuario(Base):
    # Definindo as características da tabela no banco de dados.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    senha = Column(String(150), nullable=False)

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = self._nome_vazio(nome)
        self.email = self._validar_email(email)
        self.senha = self._validar_senha(senha)

    # Funções de validação
    def _nome_vazio(self, nome: str):
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        return nome

    def _validar_email(self, email: str):
        # Verificar se o email tem o formato adequado usando regex
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(email_regex, email):
            raise EmailInvalidoError("O email fornecido é inválido.")
        return email

    def _validar_senha(self, senha: str):
        # Verificar se a senha tem pelo menos 6 caracteres
        if len(senha) < 6:
            raise SenhaInvalidaError("A senha deve ter pelo menos 6 caracteres.")
        return senha

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=db)
