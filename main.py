import tkinter as tk
from datetime import date

aken = tk.Tk()
#tekitab akna

aken.title('Harjumuste jälgija')
aken.geometry('400x300')

tervitus = tk.Label(
    
    aken,
    text = 'Tere tulemast harjumuste jalgijasse, kus saate oma harjumusi jalgida!',
    font=('Arial', 14),
    fg='blue'
)
tervitus.pack(pady=20)
#Lisab eelneva teksti aknasse, y teljel marginiga 20

def lisa_harjumus():
    #harjumuse lisamisel sisendisse kuvab teate ja kustutab sisendi
    harjumus = sisend.get()
    if harjumus:
        teade.config(text=f'Lisatud {harjumus}')
        sisend.delete(0, tk.END)
        with open('harjumused.txt', 'a', encoding='utf-8') as harjumused:
            harjumused.write(harjumus + '\n')
            


sisend = tk.Entry(aken, width=30)
sisend.pack(pady=10)

nupp = tk.Button(aken, text='Lisa harjumus', command=lisa_harjumus)
nupp.pack(pady=5)
#vajutamisel kutsub valja funktsiooni

teade = tk.Label(aken, text='')
teade.pack(pady=10)
#config muudab teate sisu, mis muidu on tyhi

def tehtud():
    harjumus = harjumus_salvestus.cget('text')
    with open('andmed.txt', 'a', encoding='utf-8') as andmed:
        andmed.write(f'{tanane},{harjumus},tehtud\n')

def tegemata():
    harjumus = harjumus_salvestus.cget('text')
    with open('andmed.txt', 'a', encoding='utf-8') as andmed:
        andmed.write(f'{tanane},{harjumus},tegemata\n')


tanane = date.today()

kuupaev = tk.Label(aken, text=f'Täna on {tanane}', font=('Arial', 12)).pack(pady=10)
#kuvab tänase kuupäeva

harjumused = []

with open('harjumused.txt', 'r', encoding='utf-8') as file:

    for harjumus in file:
        harjumus = harjumus.strip()
        harjumused.append(harjumus)

tabel = tk.Frame(aken)
tabel.pack(pady=10)

for rida, harjumus in enumerate(harjumused):
   harjumus_salvestus = tk.Label(tabel, text=harjumus, font=('Arial', 12))
   harjumus_salvestus.grid(row=rida, column=0, padx=10, pady=5)
   tk.Button(tabel, text='✅Tehtud!', width=12, fg='green', command=tehtud).grid(row=rida, column=1, padx=5)
   tk.Button(tabel, text='❌Jäi vahele.', width=12, fg='red', command=tegemata).grid(row=rida, column=2, padx=5)



aken.mainloop()