import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///prpojeto2.db"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()

def main(page: ft.Page):

    lista_produtos = ft.ListView()
    def cadastrar(e):
        try:
            novo_produto = Produto(nome=produto.value, preco=float(preco.value))
            session.add(novo_produto)
            session.commit()
            lista_produtos.controls.append(ft.Container(
                    ft.Text(novo_produto.nome),
                    bgcolor=ft.Colors.BLACK12,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10
                ))
            txt_acerto.visible = True
            txt_erro.visible = False
        except:
            txt_erro.visible = True
            txt_acerto.visible = False

        page.update()
        print("")
    txt_erro = ft.Container(ft.Text('Erro ao cadastrar produto'), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_acerto = ft.Container(ft.Text('Produto cadastrado com sucesso!'), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)

    page.title = "Cadastro App"
    txt_titulo = ft.Text('Títulodo Produto')
    produto = ft.TextField(label= "Digite o título do produto...",text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('Preço do Produto')
    preco = ft.TextField(value="0", label= "Digite o preço do produto...",text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)
    page.add(
        txt_erro,
        txt_acerto,
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto
    )
    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                 ft.Text(p.nome),
                 bgcolor=ft.Colors.BLACK12,
                 padding=15,
                 alignment=ft.alignment.center,
                 margin=3,
                 border_radius=10
            )
        )

    page.add(
        lista_produtos,
        )
    
ft.app(target= main)