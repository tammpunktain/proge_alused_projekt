import tkinter as tk
import calendar
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.colors import ListedColormap


def loo_heatmap(parent, aasta=None, kuu=None):




    leht_2 = tk.Frame(parent)


    #kuu valik
    täna = date.today()
    if aasta is None: aasta = täna.year
    if kuu is None: kuu = täna.month


    #harjumused
    harjumused = []
    try:
        with open("harjumused.txt", "r", encoding="utf-8") as f:
            for r in f:
                r = r.strip()
                if r:
                    harjumused.append(r)
    except FileNotFoundError:
        pass


    #kas tehtud või tegemata
    staatus = {}
    try:
        with open("andmed.txt", "r", encoding="utf-8") as f:
            for r in f:
                r = r.strip()
                if not r:
                    continue
                kuup_s, harjumus, s = r.split(",")
                kp = datetime.strptime(kuup_s, "%Y-%m-%d").date()
                staatus[(kp, harjumus)] = 1 if s == "tehtud" else 0
    except FileNotFoundError:
        pass


    kokku = len(harjumused)
    if kokku == 0:
        kokku = 1


    #kalender
    kal = calendar.Calendar(firstweekday=0)
    nädalad = kal.monthdatescalendar(aasta, kuu)
    ridu = len(nädalad)
    veerge = 7


    #tabel: -1 = teise kuu päev, 0 = 0 tehtud, 1 = midagi, 2 = kõik
    tabel = np.full((ridu, veerge), -1, dtype=int)


    for i, nädal in enumerate(nädalad):
        for j, kp in enumerate(nädal):
            if kp.month != kuu:
                continue


            tehtud = 0
            for h in harjumused:
                tehtud += staatus.get((kp, h), 0)


            if tehtud == 0:
                tabel[i, j] = 0
            elif tehtud == kokku:
                tabel[i, j] = 2
            else:
                tabel[i, j] = 1


    #värvid: -1 hall, 0 punane, 1 kollane, 2 roheline
    cmap = ListedColormap(["#e0e0e0", "#e74c3c", "#f1c40f", "#2ecc71"])
    #nihutamine
    pilt = tabel + 1


    #heatmap
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.imshow(pilt, cmap=cmap, vmin=0, vmax=3, interpolation="nearest", aspect="equal")


    #nädalapäevad
    ax.set_xticks(range(7))
    ax.set_xticklabels(["E", "T", "K", "N", "R", "L", "P"], fontsize=14)
    ax.xaxis.tick_top()
    ax.tick_params(axis="x", length=0)


    #y-telge pole vaja
    ax.set_yticks([])
    ax.tick_params(axis="y", length=0)


    #kasti piirid
    ax.set_xticks(np.arange(-0.5, 7, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, ridu, 1), minor=True)
    ax.grid(which="minor", linewidth=1, color="white")
    ax.tick_params(which="minor", bottom=False, top=False, left=False)


    #päevanumbrid kasti sisse
    for i, nädal in enumerate(nädalad):
        for j, kp in enumerate(nädal):
            if kp.month == kuu:
                ax.text(j, i, str(kp.day), ha="center", va="center", fontsize=12)


    #raamide eemaldamine
    for s in ax.spines.values():
        s.set_visible(False)


    #kuu nimi
    eesti_kuud = ["", "Jaanuar", "Veebruar", "Märts", "Aprill", "Mai", "Juuni",
              "Juuli", "August", "September", "Oktoober", "November", "Detsember"]
    fig.subplots_adjust(bottom=0.18, top=0.88)
    fig.text(0.5, 0.06, f"{eesti_kuud[kuu]} {aasta}", ha="center", fontsize=14)


    canvas = FigureCanvasTkAgg(fig, master=leht_2)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True, pady=100)


    return leht_2


