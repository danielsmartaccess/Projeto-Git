from ninja import Router
from typing import List, Optional
from models import session, Produto, Categoria
from ninja.schema import Schema

produtos_router = Router()

class CategoriaSchema(Schema):
    id: int = None
    nome: str

class ProdutoSchema(Schema):
    id: int = None
    nome: str
    preco: float
    categoria_id: Optional[int] = None

@produtos_router.get("/categorias/", response=List[CategoriaSchema])
def listar_categorias(request):
    categorias = session.query(Categoria).all()
    return categorias

@produtos_router.post("/categorias/", response=CategoriaSchema)
def criar_categoria(request, payload: CategoriaSchema):
    categoria = Categoria(nome=payload.nome)
    session.add(categoria)
    session.commit()
    return categoria

@produtos_router.get("/produtos/", response=List[ProdutoSchema])
def listar_produtos(request, nome: Optional[str] = None):
    query = session.query(Produto)
    if nome:
        query = query.filter(Produto.nome.ilike(f"%{nome}%"))
    return query.all()

@produtos_router.post("/produtos/", response=ProdutoSchema)
def criar_produto(request, payload: ProdutoSchema):
    produto = Produto(
        nome=payload.nome,
        preco=payload.preco,
        categoria_id=payload.categoria_id
    )
    session.add(produto)
    session.commit()
    return produto

@produtos_router.delete("/produtos/{produto_id}")
def deletar_produto(request, produto_id: int):
    produto = session.query(Produto).get(produto_id)
    if produto:
        session.delete(produto)
        session.commit()
        return {"success": True}
    return {"success": False, "message": "Produto não encontrado"}
