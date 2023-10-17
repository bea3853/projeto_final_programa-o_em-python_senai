import tkinter as tk

def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    print(senha, nome, email)
    
    # Processar e armazenar os dados aqui

root = tk.Tk()
root.title("Tela de Cadastro")

label_nome = tk.Label(root, text="Nome:")
entry_nome = tk.Entry(root)

label_email = tk.Label(root, text="E-mail:")
entry_email = tk.Entry(root)

label_senha = tk.Label(root, text="Senha:")
entry_senha = tk.Entry(root, show="*")  # Para ocultar a senha

botao_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar)

label_nome.pack()
entry_nome.pack()
label_email.pack()
entry_email.pack()
label_senha.pack()
entry_senha.pack()
botao_cadastrar.pack()

root.mainloop()