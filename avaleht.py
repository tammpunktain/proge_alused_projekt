import tkinter as tk
from datetime import date


def loo_avaleht(parent):

    leht_1 = tk.Frame(parent)

    def lisa_harjumus():
        '''
        harjumuse lisamisel sisendisse kuvab teate ja kustutab sisendi. Samuti lisab kohe 
        harjumuse lehele ja salvestab faili.
        '''
        harjumus = sisend.get()
        if harjumus:
            teade.config(font=('Arial', 20), text=f'Lisatud {harjumus}')
            sisend.delete(0, tk.END)
            with open('harjumused.txt', 'a', encoding='utf-8') as harjumused:
                harjumused.write(harjumus + '\n')
            
            harjumused_lst.append(harjumus)

            rida = len(harjumused_lst) - 1

            tk.Label(tabel, text=harjumus, font=('Arial', 20)).grid(row=rida, column=0, padx=10, pady=5)
            tk.Button(tabel, text='✅Tehtud!', font=('Arial', 20), fg='green', command=lambda h=harjumus: tehtud(h)).grid(row=rida, column=1, padx=5)
            tk.Button(tabel, text='❌Jäi vahele.', font=('Arial', 20), fg='red', command=lambda h=harjumus: tegemata(h)).grid(row=rida, column=2, padx=5)

    def tehtud(harjumus):
        #Lisab faili kirje, et harjumus on tehtud
        with open('andmed.txt', 'a', encoding='utf-8') as andmed:
            andmed.write(f'{tänane},{harjumus},tehtud\n')

    def tegemata(harjumus):
        #Lisab faili kirje, et harjumus jäi tegemata
        with open('andmed.txt', 'a', encoding='utf-8') as andmed:
            andmed.write(f'{tänane},{harjumus},tegemata\n')




    '''avaleht'''

    tervitus = tk.Label(
        leht_1,
        text = 'Tere tulemast harjumuste jälgijasse, kus saate oma harjumusi jälgida!',
        font=('Arial', 30),
        fg='blue'
    )
    tervitus.pack(pady=30, )

    #harjumuse sisestus
    sisend = tk.Entry(leht_1, font=('Arial', 20), width=50)
    sisend.pack(pady=10)

    nupp = tk.Button(leht_1, font=('Arial', 20), text='Lisa harjumus', command=lisa_harjumus)
    nupp.pack(pady=5)
    #vajutamisel kutsub valja funktsiooni

    teade = tk.Label(leht_1,font=('Arial', 20), text='')
    teade.pack(pady=10)
    #config muudab teate sisu, mis muidu on tühi

    tänane = date.today()

    kuupäev = tk.Label(leht_1, text=f'Täna on {tänane}', font=('Arial', 20)).pack(pady=10)
    #kuvab tänase kuupäeva

    tabel = tk.Frame(leht_1)
    tabel.pack(pady=10)

    #kuvab lehele salvestatud harjumused kui lehe avada
    with open('harjumused.txt', 'r', encoding='utf-8') as file:
        harjumused_lst = []
        for harjumus in file:
            harjumus = harjumus.strip()
            harjumused_lst.append(harjumus)

    for rida, harjumus in enumerate(harjumused_lst):
        harjumus_salvestus = tk.Label(tabel, text=harjumus, font=('Arial', 20))
        harjumus_salvestus.grid(row=rida, column=0, padx=10, pady=5)
        tk.Button(tabel, text='✅Tehtud!', font=('Arial', 20), fg='green', command=lambda h=harjumus: tehtud(h)).grid(row=rida, column=1, padx=5)
        tk.Button(tabel, text='❌Jäi vahele.', font=('Arial', 20), fg='red', command=lambda h=harjumus: tegemata(h)).grid(row=rida, column=2, padx=5)

    return leht_1
