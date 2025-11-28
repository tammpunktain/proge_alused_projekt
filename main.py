import tkinter as tk
from avaleht import loo_avaleht
from heatmap import loo_heatmap

def vaheta_lehte(leht):
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
leht_1_nupp = tk.Button(menyy, text='Avaleht', width=30, command=lambda: vaheta_lehte(leht_1)).grid(row=0, column=0, padx=5)
leht_1_nupp = tk.Button(menyy, text='Heatmap', width=30, command=lambda: vaheta_lehte(leht_2)).grid(row=0, column=1, padx=5)
menyy.pack(pady=10)
vaheta_lehte(leht_1)    #paneb kohe avalehe ekraanile


aken.mainloop()