import tkinter as tk

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



aken.mainloop()
