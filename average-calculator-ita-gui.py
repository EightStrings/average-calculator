import tkinter as tk
from tkinter import messagebox, simpledialog

def crea_campi_input():
    num_materie = int(num_materie_entry.get())

    for i in range(num_materie):
        materia_label = tk.Label(window, text=f"Materia {i+1}:")
        materia_label.pack()

        materia_entry = tk.Entry(window)
        materia_entry.pack()
        materie_entries.append(materia_entry)

        num_voti_label = tk.Label(window, text=f"Numero di voti per Materia {i+1}:")
        num_voti_label.pack()

        num_voti_entry = tk.Entry(window)
        num_voti_entry.pack()
        num_voti_entries.append(num_voti_entry)

    crea_campi_button.config(state=tk.DISABLED)
    calcola_button.config(state=tk.NORMAL)
    crea_campi_button.pack_forget()

def inserisci_voti():
    for i in range(len(materie_entries)):
        materia = materie_entries[i].get()
        num_voti = int(num_voti_entries[i].get())

        voti_row = []
        for j in range(num_voti):
            voto = simpledialog.askfloat(f"Voto per Materia {i+1}", f"Inserisci il voto {j+1} di: {materia}")
            voti_row.append(voto)

        voti_entries.append(voti_row)

    calcolatore_medie()

def calcolatore_medie():
    medie = {}

    for i in range(len(materie_entries)):
        materia = materie_entries[i].get()
        voti_row = voti_entries[i]
        num_voti = len(voti_row)
        voti = []

        for j in range(num_voti):
            voto = voti_row[j]
            voti.append(voto)

        media = sum(voti) / num_voti
        medie[materia] = media

    messagebox.showinfo("Risultati", f"Risultati:\n{medie}")

# Creazione della finestra principale
window = tk.Tk()
window.title("Calcolatore di Medie")
window.geometry("400x300")
# Popup di Saluto
messagebox.showinfo("Benvenuto", "Benvenuto nel Calcolatore di Medie!")

# Etichetta e campo di input per il numero di materie
num_materie_label = tk.Label(window, text="Quante materie vuoi calcolare?")
num_materie_label.pack()

num_materie_entry = tk.Entry(window)
num_materie_entry.pack()

# Bottone per creare i campi di input per le materie e il numero di voti
crea_campi_button = tk.Button(window, text="OK", command=crea_campi_input)
crea_campi_button.pack()

# Liste per memorizzare le voci di input delle materie, dei numeri di voti e dei voti
materie_entries = []
num_voti_entries = []
voti_entries = []

# Bottone per calcolare le medie
calcola_button = tk.Button(window, text="Calcola", command=inserisci_voti, state=tk.DISABLED)
calcola_button.pack()

# Avvio dell'applicazione
window.mainloop()
