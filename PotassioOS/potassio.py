import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class PotassioOS:
    def __init__(self, root):
        self.root = root
        self.root.title("PotássioOS v1.0 - [K]")
        self.root.geometry("900x600")
        self.root.configure(bg='#6A0DAD') # Roxo Vibrante (Chama de Potássio)

        # Barra de Status Superior
        self.top_bar = tk.Frame(root, bg='#2E0854', height=30)
        self.top_bar.pack(side="top", fill="x")
        
        self.lbl_status = tk.Label(self.top_bar, text="Estabilidade Atômica: 98% [ESTÁVEL]", 
                                   bg='#2E0854', fg="#00FF00", font=("Courier", 10, "bold"))
        self.lbl_status.pack(side="left", padx=10)

        # Área de Trabalho
        self.canvas = tk.Canvas(root, bg='#6A0DAD', highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")

        # Ícones Reativos
        self.criar_app("Laboratório", "#C0C0C0", 50, 50, self.abrir_terminal)
        self.criar_app("Eletrólise", "#FFD700", 50, 150, self.reacao_quimica)
        self.criar_app("Tabela", "#FFFFFF", 50, 250, self.mostrar_tabela)

        # Barra de Tarefas
        self.taskbar = tk.Frame(root, bg='#1A1A1A', height=50)
        self.taskbar.pack(side="bottom", fill="x")
        
        self.btn_k = tk.Button(self.taskbar, text="[ K ]", bg="#9370DB", fg="white", 
                               font=("Arial", 12, "bold"), command=self.menu_k)
        self.btn_k.pack(side="left", padx=10, pady=5)

    def criar_app(self, nome, cor, x, y, acao):
        btn = tk.Button(self.root, text=f"☢\n{nome}", command=acao, 
                        bg=cor, fg="black", width=10, height=3, relief="raised")
        btn.place(x=x, y=y)

    def abrir_terminal(self):
        cmd = simpledialog.askstring("Terminal K-OS", "Digite um comando atômico:")
        if cmd == "help":
            messagebox.showinfo("K-OS", "Comandos: fusao, fissao, estourar")
        elif cmd == "estourar":
            self.root.configure(bg="white")
            messagebox.showwarning("BOOM", "Reação violenta com a água!")
            self.root.configure(bg="#6A0DAD")
        else:
            messagebox.showerror("Erro", "Comando instável.")

    def reacao_quimica(self):
        self.lbl_status.config(text="Estabilidade Atômica: 15% [CRÍTICO]", fg="red")
        messagebox.showwarning("ALERTA", "Nível de radiação subindo!")

    def mostrar_tabela(self):
        messagebox.showinfo("Tabela Periódica", "Potássio (K)\nNúmero Atômico: 19\nMassa: 39.098\nStatus: Reativo pra caramba.")

    def menu_k(self):
        messagebox.showinfo("PotássioOS", "Versão 1.0\nDesenvolvido por: OsJanelas\nStatus: Licenciado para explodir.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PotassioOS(root)
    root.mainloop()