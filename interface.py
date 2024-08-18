import tkinter as tk
from tkinter import messagebox
from password_manager import PasswordManager

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Senhas")
        self.manager = PasswordManager()
        
        # Interface de adição de senha
        self.add_frame = tk.Frame(self.root)
        self.add_frame.pack(pady=10)

        tk.Label(self.add_frame, text="Site:").grid(row=0, column=0)
        self.site_entry = tk.Entry(self.add_frame)
        self.site_entry.grid(row=0, column=1)

        tk.Label(self.add_frame, text="Senha:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.add_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.add_frame, text="Adicionar Senha", command=self.add_password).grid(row=2, columnspan=2, pady=5)

        # Interface de visualização de senha
        self.view_frame = tk.Frame(self.root)
        self.view_frame.pack(pady=10)

        tk.Label(self.view_frame, text="Site:").grid(row=0, column=0)
        self.view_site_entry = tk.Entry(self.view_frame)
        self.view_site_entry.grid(row=0, column=1)

        tk.Button(self.view_frame, text="Mostrar Senha", command=self.view_password).grid(row=1, columnspan=2, pady=5)
        self.result_label = tk.Label(self.view_frame, text="")
        self.result_label.grid(row=2, columnspan=2)

        # Interface de exclusão de senha
        self.delete_frame = tk.Frame(self.root)
        self.delete_frame.pack(pady=10)

        tk.Label(self.delete_frame, text="Site para excluir:").grid(row=0, column=0)
        self.delete_site_entry = tk.Entry(self.delete_frame)
        self.delete_site_entry.grid(row=0, column=1)

        tk.Button(self.delete_frame, text="Excluir Senha", command=self.delete_password).grid(row=1, columnspan=2, pady=5)

    def add_password(self):
        site = self.site_entry.get()
        password = self.password_entry.get()
        if site and password:
            self.manager.add_password(site, password)
            messagebox.showinfo("Sucesso", "Senha adicionada com sucesso!")
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

    def view_password(self):
        site = self.view_site_entry.get()
        if site:
            password = self.manager.get_password(site)
            if password:
                self.result_label.config(text=f"Senha: {password}")
            else:
                self.result_label.config(text="Senha não encontrada.")
        else:
            messagebox.showwarning("Erro", "Por favor, insira um site.")

    def delete_password(self):
        site = self.delete_site_entry.get()
        if site:
            self.manager.delete_password(site)
            messagebox.showinfo("Sucesso", "Senha excluída com sucesso!")
        else:
            messagebox.showwarning("Erro", "Por favor, insira um site.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
