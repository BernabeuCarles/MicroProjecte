import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connexió a la base de dades
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Creació de les taules amb les modificacions sol·licitades
c.execute('''CREATE TABLE IF NOT EXISTS AGENCIA
             (AgenciaID INTEGER PRIMARY KEY, nom TEXT, Email TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS MANAGER
             (ManagerID INTEGER PRIMARY KEY, AgenciaID INTEGER, Nom TEXT, Email TEXT,
              Nacionalitat TEXT, Benefici TEXT,
              FOREIGN KEY(AgenciaID) REFERENCES AGENCIA(AgenciaID))''')
c.execute('''CREATE TABLE IF NOT EXISTS MODEL
             (ModelID INTEGER PRIMARY KEY, ManagerID INTEGER, Edat INTEGER, Nom TEXT,
              Email TEXT, Nacionalitat TEXT, Benefici TEXT, Subscriptors INTEGER,
              FOREIGN KEY(ManagerID) REFERENCES MANAGER(ManagerID))''')
conn.commit()

# Funció per inserir dades a la taula AGENCIA
def insert_agencia():
    # Obtindre les dades de la finestra
    nom = agencia_nom.get()
    email = agencia_email.get()
    
    if nom and email:
        data = (nom, email)
        c.execute('INSERT INTO AGENCIA (nom, Email) VALUES (?, ?)', data)
        conn.commit()
        messagebox.showinfo('Èxit', 'Dades inserides a AGENCIA')
    else:
        messagebox.showerror('Error', 'Si us plau, introdueix el nom i l\'email de l\'agència')

# Funció per inserir dades a la taula MANAGER
def insert_manager():
    # Obtindre les dades de la finestra
    agencia_id = manager_agencia_id.get()
    nom = manager_nom.get()
    email = manager_email.get()
    nacionalitat = manager_nacionalitat.get()
    benefici = manager_benefici.get()
    
    if nom and email and nacionalitat and benefici:
        if agencia_id:
            data = (agencia_id, nom, email, nacionalitat, benefici)
        else:
            data = (None, nom, email, nacionalitat, benefici)
        c.execute('INSERT INTO MANAGER (AgenciaID, Nom, Email, Nacionalitat, Benefici) VALUES (?, ?, ?, ?, ?)', data)
        conn.commit()
        messagebox.showinfo('Èxit', 'Dades inserides a MANAGER')
    else:
        messagebox.showerror('Error', 'Si us plau, introdueix totes les dades del manager')

# Funció per inserir dades a la taula MODEL
def insert_model():
    # Obtindre les dades de la finestra
    manager_id = model_manager_id.get()
    edat = model_edat.get()
    nom = model_nom.get()
    email = model_email.get()
    nacionalitat = model_nacionalitat.get()
    benefici = model_benefici.get()
    subscriptors = model_subscriptors.get()
    
    if edat and nom and email and nacionalitat and benefici and subscriptors:
        if manager_id:
            data = (manager_id, edat, nom, email, nacionalitat, benefici, subscriptors)
            c.execute('INSERT INTO MODEL (ManagerID, Edat, Nom, Email, Nacionalitat, Benefici, Subscriptors) VALUES (?, ?, ?, ?, ?, ?, ?)', data)
        else:
            data = (None, edat, nom, email, nacionalitat, benefici, subscriptors)
            c.execute('INSERT INTO MODEL (ManagerID, Edat, Nom, Email, Nacionalitat, Benefici, Subscriptors) VALUES (?, ?, ?, ?, ?, ?, ?)', data)
        conn.commit()
        messagebox.showinfo('Èxit', 'Dades inserides a MODEL')
    else:
        messagebox.showerror('Error', 'Si us plau, introdueix totes les dades del model')

# Funció per mostrar els models sense manager assignat
def show_models_without_manager():
    c.execute('SELECT * FROM MODEL WHERE ManagerID IS NULL')
    data = c.fetchall()
    
    # Crear una nova finestra per mostrar les dades
    show_window = tk.Toplevel()
    show_window.title("Models sense Manager")
    
    # Crear un widget de text per mostrar les dades
    text_widget = tk.Text(show_window)
    text_widget.pack()
    
    # Afegir les dades al widget de text
    for row in data:
        text_widget.insert(tk.END, f"{row}\n")

# Funció per mostrar els managers sense agència assignada
def show_managers_without_agency():
    c.execute('SELECT * FROM MANAGER WHERE AgenciaID IS NULL')
    data = c.fetchall()
    
    # Crear una nova finestra per mostrar les dades
    show_window = tk.Toplevel()
    show_window.title("Managers sense Agència")
    
    # Crear un widget de text per mostrar les dades
    text_widget = tk.Text(show_window)
    text_widget.pack()
    
    # Afegir les dades al widget de text
    for row in data:
        text_widget.insert(tk.END, f"{row}\n")

# Crear la finestra principal
root = tk.Tk()
root.title("OnlyData")

# Entrades de text per a AGENCIA
tk.Label(root, text="Nom Agència:").grid(row=0, column=0)
agencia_nom = tk.Entry(root)
agencia_nom.grid(row=0, column=1)
tk.Label(root, text="Email Agència:").grid(row=1, column=0)
agencia_email = tk.Entry(root)
agencia_email.grid(row=1, column=1)

# Botons per inserir dades a AGENCIA
insert_agencia_btn = tk.Button(root, text="Inserir Agència", command=insert_agencia)
insert_agencia_btn.grid(row=2, column=0, columnspan=2)

# Entrades de text per a MANAGER
tk.Label(root, text="ID Agència Manager:").grid(row=3, column=0)
manager_agencia_id = tk.Entry(root)
manager_agencia_id.grid(row=3, column=1)
tk.Label(root, text="Nom Manager:").grid(row=4, column=0)
manager_nom = tk.Entry(root)
manager_nom.grid(row=4, column=1)
tk.Label(root, text="Email Manager:").grid(row=5, column=0)
manager_email = tk.Entry(root)
manager_email.grid(row=5, column=1)
tk.Label(root, text="Nacionalitat Manager:").grid(row=6, column=0)
manager_nacionalitat = tk.Entry(root)
manager_nacionalitat.grid(row=6, column=1)
tk.Label(root, text="Benefici Manager:").grid(row=7, column=0)
manager_benefici = tk.Entry(root)
manager_benefici.grid(row=7, column=1)

# Botons per inserir dades a MANAGER
insert_manager_btn = tk.Button(root, text="Inserir Manager", command=insert_manager)
insert_manager_btn.grid(row=8, column=0, columnspan=2)

# Entrades de text per a MODEL
tk.Label(root, text="ID Manager Model:").grid(row=9, column=0)
model_manager_id = tk.Entry(root)
model_manager_id.grid(row=9, column=1)
tk.Label(root, text="Edat Model:").grid(row=10, column=0)
model_edat = tk.Entry(root)
model_edat.grid(row=10, column=1)
tk.Label(root, text="Nom Model:").grid(row=11, column=0)
model_nom = tk.Entry(root)
model_nom.grid(row=11, column=1)
tk.Label(root, text="Email Model:").grid(row=12, column=0)
model_email = tk.Entry(root)
model_email.grid(row=12, column=1)
tk.Label(root, text="Nacionalitat Model:").grid(row=13, column=0)
model_nacionalitat = tk.Entry(root)
model_nacionalitat.grid(row=13, column=1)
tk.Label(root, text="Benefici Model:").grid(row=14, column=0)
model_benefici = tk.Entry(root)
model_benefici.grid(row=14, column=1)
tk.Label(root, text="Subscriptors Model:").grid(row=15, column=0)
model_subscriptors = tk.Entry(root)
model_subscriptors.grid(row=15, column=1)

# Botons per inserir dades a MODEL
insert_model_btn = tk.Button(root, text="Inserir Model", command=insert_model)
insert_model_btn.grid(row=16, column=0, columnspan=2)

# Botó per mostrar models sense manager
show_models_without_manager_btn = tk.Button(root, text="Mostrar models sense Manager", command=show_models_without_manager)
show_models_without_manager_btn.grid(row=17, column=0, columnspan=2)

# Botó per mostrar managers sense agència
show_managers_without_agency_btn = tk.Button(root, text="Mostrar managers sense Agència", command=show_managers_without_agency)
show_managers_without_agency_btn.grid(row=18, column=0, columnspan=2)

# Executar la finestra principal
root.mainloop()

# Tancar la connexió a la base de dades al tancar la finestra
conn.close()
