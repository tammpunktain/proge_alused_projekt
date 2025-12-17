'''
Projekti eesmärk on luua graafiline kasutajaliides, mis aitab kasutajal jälgida oma igapäevaseid harjumusi.
Kasutaja saab lisada uusi harjumusi, märkida need tehtud või tegemata ning vaadata oma edusamme heatmapi kujul.

Requirements: NumPy, Matplotlib

Autorid: Ville Fohs, Ain Tamm

Kasutatud allikad: W3Schools, Stack Overflow, ChatGPT, matplotlib dokumentatsioon

'''


import tkinter as tk
from avaleht import loo_avaleht
from heatmap import loo_heatmap

def vaheta_lehte(leht):
    # Peidab kõik lehed ja näitab ainult valitud lehte
    leht_1.pack_forget()
    leht_2.pack_forget()
    leht.pack()

aken = tk.Tk()
aken.title('Harjumuste jälgija')
aken.geometry('400x300')

'''lehed'''
leht_1 = loo_avaleht(aken)
leht_2 = loo_heatmap(aken)

'''menyy'''
menyy = tk.Frame(aken)
leht_1_nupp = tk.Button(menyy, text='Avaleht', font=('Arial', 20), width=30, command=lambda: vaheta_lehte(leht_1)).grid(row=0, column=0, padx=5)
leht_2_nupp = tk.Button(menyy, text='Heatmap', font=('Arial', 20), width=30, command=lambda: vaheta_lehte(leht_2)).grid(row=0, column=1, padx=5)
menyy.pack(pady=10)
vaheta_lehte(leht_1)
#paneb kohe avalehe ekraanile


aken.mainloop()