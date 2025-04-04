from sqlalchemy import Column,Integer,VARCHAR
from sqlalchemy.ext.declarative import declarative_base

base_sol =  declarative_base()

class tblSolAcesso(base_sol):
    __tablename__ = 'tblSolAcesso'
    tbaId       = Column(Integer,primary_key=True,autoincrement=True)
    tbaMatricula= Column(VARCHAR(10))
    tbaEmail    = Column(VARCHAR(200))
    tbaNome     = Column(VARCHAR(200))
    tbaSenha    = Column(VARCHAR(200))
    tbaPerfil   = Column(VARCHAR(15))
    tbaDtCriacao= Column(VARCHAR(10)) 
