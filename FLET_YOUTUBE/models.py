from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

CONN = "sqlite:///projeto.db"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    produtos = relationship("Produto", back_populates="categoria")

class Produto(Base):
    __tablename__ = "produto"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    preco = Column(Float(), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    categoria = relationship("Categoria", back_populates="produtos")

Base.metadata.create_all(engine)
