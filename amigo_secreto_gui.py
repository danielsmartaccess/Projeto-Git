"""
Sistema de Amigo Secreto - Interface Gráfica

Este script implementa um sistema completo de gerenciamento de amigo secreto com interface gráfica,
permitindo:
- Cadastro de participantes com sugestões de presentes
- Definição de valores mínimos e máximos para os presentes
- Realização do sorteio
- Envio de emails automáticos com os resultados
- Consulta dos resultados salvos
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import re
import os

class AmigoSecretoGUI:
    def __init__(self, root):
        """
        Inicializa a interface gráfica do sistema de Amigo Secreto.
        """
        self.root = root
        self.root.title("Amigo Secreto")
        self.root.geometry("800x600")
        
        # Configurações básicas
        self.participantes = []
        self.valor_minimo = tk.StringVar(value="0")
        self.valor_maximo = tk.StringVar(value="0")
        self.sorteio_realizado = False
        self.resultado_sorteio = {}
        
        # Configurações do email
        self.email_config = {
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587,
            "email_remetente": "seu_email@gmail.com",
            "senha_app": "sua_senha_app"
        }
        
        # Criação da interface
        self.criar_interface()
        
        # Carregar dados salvos se existirem
        self.carregar_dados()

    def criar_interface(self):
        """
        Cria todos os elementos da interface gráfica.
        """
        # Notebook para abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=5)
        
        # Aba de Cadastro
        self.aba_cadastro = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_cadastro, text='Cadastro')
        self.criar_aba_cadastro()
        
        # Aba de Sorteio
        self.aba_sorteio = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_sorteio, text='Sorteio')
        self.criar_aba_sorteio()
        
        # Aba de Configurações
        self.aba_config = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_config, text='Configurações')
        self.criar_aba_config()

    def criar_aba_cadastro(self):
        """
        Cria os elementos da aba de cadastro de participantes.
        """
        # Frame para entrada de dados
        frame_entrada = ttk.LabelFrame(self.aba_cadastro, text="Novo Participante")
        frame_entrada.pack(fill='x', padx=10, pady=5)
        
        # Campos de entrada
        ttk.Label(frame_entrada, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome = ttk.Entry(frame_entrada, width=40)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_entrada, text="Email:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_email = ttk.Entry(frame_entrada, width=40)
        self.entry_email.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_entrada, text="Sugestões:").grid(row=2, column=0, padx=5, pady=5)
        self.text_sugestoes = scrolledtext.ScrolledText(frame_entrada, width=40, height=4)
        self.text_sugestoes.grid(row=2, column=1, padx=5, pady=5)
        
        # Botão de cadastro
        ttk.Button(frame_entrada, text="Cadastrar", command=self.cadastrar_participante).grid(row=3, column=1, pady=10)
        
        # Lista de participantes
        frame_lista = ttk.LabelFrame(self.aba_cadastro, text="Participantes Cadastrados")
        frame_lista.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.lista_participantes = ttk.Treeview(frame_lista, columns=('Nome', 'Email', 'Sugestões'), show='headings')
        self.lista_participantes.heading('Nome', text='Nome')
        self.lista_participantes.heading('Email', text='Email')
        self.lista_participantes.heading('Sugestões', text='Sugestões')
        self.lista_participantes.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Botão para remover participante
        ttk.Button(frame_lista, text="Remover Selecionado", command=self.remover_participante).pack(pady=5)

    def criar_aba_sorteio(self):
        """
        Cria os elementos da aba de sorteio.
        """
        # Frame para controles do sorteio
        frame_sorteio = ttk.LabelFrame(self.aba_sorteio, text="Realizar Sorteio")
        frame_sorteio.pack(fill='x', padx=10, pady=5)
        
        # Botões de ação
        ttk.Button(frame_sorteio, text="Realizar Sorteio", command=self.realizar_sorteio).pack(pady=10)
        ttk.Button(frame_sorteio, text="Enviar E-mails", command=self.enviar_emails).pack(pady=10)
        
        # Área de resultados
        frame_resultado = ttk.LabelFrame(self.aba_sorteio, text="Resultado do Sorteio")
        frame_resultado.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.text_resultado = scrolledtext.ScrolledText(frame_resultado, width=50, height=10)
        self.text_resultado.pack(fill='both', expand=True, padx=5, pady=5)

    def criar_aba_config(self):
        """
        Cria os elementos da aba de configurações.
        """
        frame_config = ttk.LabelFrame(self.aba_config, text="Configurações")
        frame_config.pack(fill='x', padx=10, pady=5)
        
        # Valores dos presentes
        ttk.Label(frame_config, text="Valor Mínimo (R$):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_min = ttk.Entry(frame_config, textvariable=self.valor_minimo)
        self.entry_min.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_config, text="Valor Máximo (R$):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_max = ttk.Entry(frame_config, textvariable=self.valor_maximo)
        self.entry_max.grid(row=1, column=1, padx=5, pady=5)
        
        # Configurações de email
        ttk.Label(frame_config, text="Email Remetente:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_email_rem = ttk.Entry(frame_config, width=40)
        self.entry_email_rem.grid(row=2, column=1, padx=5, pady=5)
        self.entry_email_rem.insert(0, self.email_config["email_remetente"])
        
        ttk.Label(frame_config, text="Senha App:").grid(row=3, column=0, padx=5, pady=5)
        self.entry_senha = ttk.Entry(frame_config, width=40, show="*")
        self.entry_senha.grid(row=3, column=1, padx=5, pady=5)
        self.entry_senha.insert(0, self.email_config["senha_app"])
        
        # Botão para salvar configurações
        ttk.Button(frame_config, text="Salvar Configurações", command=self.salvar_configuracoes).grid(row=4, column=1, pady=10)

    def validar_nome(self, nome):
        """
        Valida o nome do participante.
        """
        if not nome:
            messagebox.showerror("Erro", "O nome não pode estar vazio.")
            return None
        
        nome = " ".join(nome.split())
        nome = nome.title()
        
        if len(nome) < 2:
            messagebox.showerror("Erro", "O nome deve ter pelo menos 2 caracteres.")
            return None
        
        if not all(c.isalpha() or c.isspace() for c in nome):
            messagebox.showerror("Erro", "O nome deve conter apenas letras e espaços.")
            return None
        
        return nome

    def validar_email(self, email):
        """
        Valida o endereço de email.
        """
        if not email:
            messagebox.showerror("Erro", "O email não pode estar vazio.")
            return None

        padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        email = email.lower().strip()
        
        if not re.match(padrao_email, email):
            messagebox.showerror("Erro", "Formato de email inválido.")
            return None
            
        if any(p["email"] == email for p in self.participantes):
            messagebox.showerror("Erro", "Este email já está cadastrado.")
            return None
            
        return email

    def cadastrar_participante(self):
        """
        Cadastra um novo participante na lista.
        """
        nome = self.validar_nome(self.entry_nome.get())
        if not nome:
            return
            
        email = self.validar_email(self.entry_email.get())
        if not email:
            return
            
        sugestoes = self.text_sugestoes.get("1.0", tk.END).strip()
        if not sugestoes:
            messagebox.showwarning("Aviso", "Nenhuma sugestão de presente fornecida.")
            sugestoes = "Sem sugestões"
        
        participante = {
            "nome": nome,
            "email": email,
            "sugestoes": sugestoes
        }
        
        self.participantes.append(participante)
        self.atualizar_lista_participantes()
        self.limpar_campos_cadastro()
        self.salvar_dados()

    def remover_participante(self):
        """
        Remove o participante selecionado da lista.
        """
        selecao = self.lista_participantes.selection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um participante para remover.")
            return
            
        if messagebox.askyesno("Confirmar", "Deseja realmente remover o participante selecionado?"):
            item = self.lista_participantes.item(selecao[0])
            email = item['values'][1]
            self.participantes = [p for p in self.participantes if p['email'] != email]
            self.atualizar_lista_participantes()
            self.salvar_dados()

    def atualizar_lista_participantes(self):
        """
        Atualiza a exibição da lista de participantes.
        """
        for item in self.lista_participantes.get_children():
            self.lista_participantes.delete(item)
            
        for p in self.participantes:
            self.lista_participantes.insert('', 'end', values=(p['nome'], p['email'], p['sugestoes']))

    def limpar_campos_cadastro(self):
        """
        Limpa os campos do formulário de cadastro.
        """
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.text_sugestoes.delete("1.0", tk.END)

    def realizar_sorteio(self):
        """
        Realiza o sorteio do amigo secreto.
        """
        if len(self.participantes) < 3:
            messagebox.showerror("Erro", "É necessário pelo menos 3 participantes para realizar o sorteio.")
            return
            
        nomes = [p["nome"] for p in self.participantes]
        sorteados = nomes.copy()
        
        while any(a == b for a, b in zip(nomes, sorteados)):
            random.shuffle(sorteados)
        
        self.resultado_sorteio = dict(zip(nomes, sorteados))
        self.sorteio_realizado = True
        
        # Atualiza a área de resultado
        self.text_resultado.delete("1.0", tk.END)
        for quem_dá, quem_recebe in self.resultado_sorteio.items():
            self.text_resultado.insert(tk.END, f"{quem_dá} → {quem_recebe}\n")
        
        self.salvar_dados()
        messagebox.showinfo("Sucesso", "Sorteio realizado com sucesso!")

    def enviar_emails(self):
        """
        Envia os emails com os resultados do sorteio.
        """
        if not self.sorteio_realizado:
            messagebox.showerror("Erro", "Realize o sorteio primeiro!")
            return
            
        try:
            servidor = smtplib.SMTP(self.email_config["smtp_server"], self.email_config["smtp_port"])
            servidor.starttls()
            servidor.login(self.email_config["email_remetente"], self.email_config["senha_app"])
            
            for participante in self.participantes:
                nome = participante["nome"]
                email = participante["email"]
                amigo_secreto = self.resultado_sorteio[nome]
                
                # Encontra as sugestões do amigo secreto
                sugestoes = next(p["sugestoes"] for p in self.participantes if p["nome"] == amigo_secreto)
                
                mensagem = MIMEMultipart()
                mensagem["From"] = self.email_config["email_remetente"]
                mensagem["To"] = email
                mensagem["Subject"] = "Seu Amigo Secreto!"
                
                corpo = f"""
                Olá {nome}!
                
                Você foi sorteado para ser o amigo secreto de: {amigo_secreto}
                
                Valor do presente: Entre R${float(self.valor_minimo.get()):.2f} e R${float(self.valor_maximo.get()):.2f}
                
                Sugestões de presentes do seu amigo secreto:
                {sugestoes}
                
                Boas compras!
                """
                
                mensagem.attach(MIMEText(corpo, "plain"))
                servidor.send_message(mensagem)
            
            servidor.quit()
            messagebox.showinfo("Sucesso", "E-mails enviados com sucesso!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao enviar e-mails: {str(e)}")

    def salvar_configuracoes(self):
        """
        Salva as configurações atuais.
        """
        try:
            self.email_config["email_remetente"] = self.entry_email_rem.get()
            self.email_config["senha_app"] = self.entry_senha.get()
            
            if not self.valor_minimo.get().replace(".", "").isdigit():
                raise ValueError("Valor mínimo inválido")
            if not self.valor_maximo.get().replace(".", "").isdigit():
                raise ValueError("Valor máximo inválido")
                
            if float(self.valor_minimo.get()) > float(self.valor_maximo.get()):
                raise ValueError("Valor mínimo não pode ser maior que o valor máximo")
            
            self.salvar_dados()
            messagebox.showinfo("Sucesso", "Configurações salvas com sucesso!")
            
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def salvar_dados(self):
        """
        Salva todos os dados em um arquivo JSON.
        """
        dados = {
            "participantes": self.participantes,
            "valor_minimo": self.valor_minimo.get(),
            "valor_maximo": self.valor_maximo.get(),
            "sorteio_realizado": self.sorteio_realizado,
            "resultado_sorteio": self.resultado_sorteio,
            "email_config": self.email_config
        }
        
        try:
            with open("amigo_secreto_dados.json", "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados: {str(e)}")

    def carregar_dados(self):
        """
        Carrega os dados salvos do arquivo JSON.
        """
        try:
            if os.path.exists("amigo_secreto_dados.json"):
                with open("amigo_secreto_dados.json", "r", encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                    
                self.participantes = dados.get("participantes", [])
                self.valor_minimo.set(dados.get("valor_minimo", "0"))
                self.valor_maximo.set(dados.get("valor_maximo", "0"))
                self.sorteio_realizado = dados.get("sorteio_realizado", False)
                self.resultado_sorteio = dados.get("resultado_sorteio", {})
                self.email_config.update(dados.get("email_config", {}))
                
                self.atualizar_lista_participantes()
                
                if self.sorteio_realizado:
                    self.text_resultado.delete("1.0", tk.END)
                    for quem_dá, quem_recebe in self.resultado_sorteio.items():
                        self.text_resultado.insert(tk.END, f"{quem_dá} → {quem_recebe}\n")
                        
        except Exception as e:
            messagebox.showwarning("Aviso", f"Erro ao carregar dados: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AmigoSecretoGUI(root)
    root.mainloop()
