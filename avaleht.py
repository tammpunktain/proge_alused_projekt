import tkinter as tk
from datetime import date


def loo_avaleht(parent):

    leht_1 = tk.Frame(parent)

    def lisa_harjumus():
        #harjumuse lisamisel sisendisse kuvab teate ja kustutab sisendi
        harjumus = sisend.get()
        if harjumus:
            teade.config(text=f'Lisatud {harjumus}')
            sisend.delete(0, tk.END)
            with open('harjumused.txt', 'a', encoding='utf-8') as harjumused:
                harjumused.write(harjumus + '\n')
            
            harjumused_lst.append(harjumus)

            rida = len(harjumused_lst) - 1

            tk.Label(tabel, text=harjumus, font=('Arial', 12)).grid(row=rida, column=0, padx=10, pady=5)
            tk.Button(tabel, text='✅Tehtud!', width=12, fg='green', command=lambda h=harjumus: tehtud(h)).grid(row=rida, column=1, padx=5)
            tk.Button(tabel, text='❌Jäi vahele.', width=12, fg='red', command=lambda h=harjumus: tegemata(h)).grid(row=rida, column=2, padx=5)

    def tehtud(harjumus):
        with open('andmed.txt', 'a', encoding='utf-8') as andmed:
            andmed.write(f'{tanane},{harjumus},tehtud\n')

    def tegemata(harjumus):
        with open('andmed.txt', 'a', encoding='utf-8') as andmed:
            andmed.write(f'{tanane},{harjumus},tegemata\n')




    '''avaleht'''

    tervitus = tk.Label(
        leht_1,
        text = 'Tere tulemast harjumuste jalgijasse, kus saate oma harjumusi jalgida!',
        font=('Arial', 14),
        fg='blue'
    )
    tervitus.pack()


    sisend = tk.Entry(leht_1, width=30)
    sisend.pack(pady=10)

    nupp = tk.Button(leht_1, text='Lisa harjumus', command=lisa_harjumus)
    nupp.pack(pady=5)
    #vajutamisel kutsub valja funktsiooni

    teade = tk.Label(leht_1, text='')
    teade.pack(pady=10)
    #config muudab teate sisu, mis muidu on tyhi

    tanane = date.today()

    kuupaev = tk.Label(leht_1, text=f'Täna on {tanane}', font=('Arial', 12)).pack(pady=10)
    #kuvab tänase kuupäeva

    tabel = tk.Frame(leht_1)
    tabel.pack(pady=10)


    with open('harjumused.txt', 'r', encoding='utf-8') as file:
        harjumused_lst = []
        for harjumus in file:
            harjumus = harjumus.strip()
            harjumused_lst.append(harjumus)

    for rida, harjumus in enumerate(harjumused_lst):
        harjumus_salvestus = tk.Label(tabel, text=harjumus, font=('Arial', 12))
        harjumus_salvestus.grid(row=rida, column=0, padx=10, pady=5)
        tk.Button(tabel, text='✅Tehtud!', width=12, fg='green', command=lambda h=harjumus: tehtud(h)).grid(row=rida, column=1, padx=5)
        tk.Button(tabel, text='❌Jäi vahele.', width=12, fg='red', command=lambda h=harjumus: tegemata(h)).grid(row=rida, column=2, padx=5)

    return leht_1
