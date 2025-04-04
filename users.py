from sqlalchemy import Column,Integer,VARCHAR
from sqlalchemy.ext.declarative import declarative_base

base_user =  declarative_base()
class tblUsers(base_user):
    __tablename__ = 'tblUsers'
    tbuId       = Column(Integer,primary_key=True,autoincrement=True)
    tbuNome     = Column(VARCHAR(200))
    tbuPerfil   = Column(VARCHAR(15))
    tbuDtCriacao= Column(VARCHAR(10)) 
