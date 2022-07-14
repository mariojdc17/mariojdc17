from tkinter import *
from tkinter import Entry
from tkinter import messagebox
from tkinter import ttk
import math
import os
import sys


# Agrupar archivos

def resource_path(relative_path):
    # """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def ayuda():
    messagebox.showinfo(title="Ayuda", message="Agregar los valores Lab en las "
                                               "entradas correspondientes.\nun valor por caja")


def info():
    messagebox.showinfo(title="Información", message="Autor : Mario Dutruel.\nCalculadora de ΔE para la carta de color "
                                                     "X-rite Colorchecker Color Rendition Chart.\n"
                                                     "Usando la fórmula CIE76.")


TK = ttk
root = Tk()
root.title("Calculadora ΔE")
root.resizable(False, False)
root.anchor("n")
image_path = resource_path("icono.ico")
root.iconbitmap(image_path)
barraMenu = Menu(root)
mnuAyuda = Menu(barraMenu, tearoff=0)
mnuAyuda.add_command(label="Ayuda", command=ayuda)
mnuAyuda.add_command(label="Info", command=info)
mnuAyuda.add_separator()
mnuAyuda.add_command(label="Salir", command=root.quit)
barraMenu.add_cascade(label="Inicio", menu=mnuAyuda)
root.config(bg="#7c7c7c", menu=barraMenu)
snline = Menu(barraMenu, tearoff=0)


ancho_ventana = 800
alto_ventana = 800

x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)

entryL = Label(root, text="L", fg="white", bg="#7c7c7c", font='bold 12')
entryL.place(x=100, y=5)
entryA = Label(root, text="a", fg="white", bg="#7c7c7c", font='bold 12')
entryA.place(x=250, y=5)
entryB = Label(root, text="b", fg="white", bg="#7c7c7c", font='bold 12')
entryB.place(x=400, y=5)

uno = Label(root, text="1", fg="white", bg="#7c7c7c", font='bold 12')
uno.place(x=20, y=27)
dos = Label(root, text="2", fg="white", bg="#7c7c7c", font='bold 12')
dos.place(x=20, y=57)
tres = Label(root, text="3", fg="white", bg="#7c7c7c", font='bold 12')
tres.place(x=20, y=87)
cuatro = Label(root, text="4", fg="white", bg="#7c7c7c", font='bold 12')
cuatro.place(x=20, y=117)
cinco = Label(root, text="5", fg="white", bg="#7c7c7c", font='bold 12')
cinco.place(x=20, y=147)
seis = Label(root, text="6", fg="white", bg="#7c7c7c", font='bold 12')
seis.place(x=20, y=177)
siete = Label(root, text="7", fg="white", bg="#7c7c7c", font='bold 12')
siete.place(x=20, y=207)
ocho = Label(root, text="8", fg="white", bg="#7c7c7c", font='bold 12')
ocho.place(x=20, y=237)
nueve = Label(root, text="9", fg="white", bg="#7c7c7c", font='bold 12')
nueve.place(x=20, y=267)
diez = Label(root, text="10", fg="white", bg="#7c7c7c", font='bold 12')
diez.place(x=20, y=297)
once = Label(root, text="11", fg="white", bg="#7c7c7c", font='bold 12')
once.place(x=20, y=327)
doce = Label(root, text="12", fg="white", bg="#7c7c7c", font='bold 12')
doce.place(x=20, y=357)
trece = Label(root, text="13", fg="white", bg="#7c7c7c", font='bold 12')
trece.place(x=20, y=387)
catorce = Label(root, text="14", fg="white", bg="#7c7c7c", font='bold 12')
catorce.place(x=20, y=417)
quince = Label(root, text="15", fg="white", bg="#7c7c7c", font='bold 12')
quince.place(x=20, y=447)
dieciseis = Label(root, text="16", fg="white", bg="#7c7c7c", font='bold 12')
dieciseis.place(x=20, y=477)
diecisiete = Label(root, text="17", fg="white", bg="#7c7c7c", font='bold 12')
diecisiete.place(x=20, y=507)
dieciocho = Label(root, text="18", fg="white", bg="#7c7c7c", font='bold 12')
dieciocho.place(x=20, y=537)
diecinuve = Label(root, text="19", fg="white", bg="#7c7c7c", font='bold 12')
diecinuve.place(x=20, y=567)
veinte = Label(root, text="20", fg="white", bg="#7c7c7c", font='bold 12')
veinte.place(x=20, y=597)
veintiuno = Label(root, text="21", fg="white", bg="#7c7c7c", font='bold 12')
veintiuno.place(x=20, y=627)
veintidos = Label(root, text="22", fg="white", bg="#7c7c7c", font='bold 12')
veintidos.place(x=20, y=657)
veintitres = Label(root, text="23", fg="white", bg="#7c7c7c", font='bold 12')
veintitres.place(x=20, y=687)
veinticuatro = Label(root, text="24", fg="white", bg="#7c7c7c", font='bold 12')
veinticuatro.place(x=20, y=717)

# Valores L
addLuno = StringVar()
addLdos = StringVar()
addLtres = StringVar()
addLcuatro = StringVar()
addLcinco = StringVar()
addLseis = StringVar()
addLsiete = StringVar()
addLocho = StringVar()
addLnueve = StringVar()
addLdiez = StringVar()
addLonce = StringVar()
addLdoce = StringVar()
addLtrece = StringVar()
addLcatorce = StringVar()
addLquince = StringVar()
addLdieciseis = StringVar()
addLdiecisiete = StringVar()
addLdieciocho = StringVar()
addLdiecinueve = StringVar()
addLveinte = StringVar()
addLveintiuno = StringVar()
addLveintidos = StringVar()
addLveintitres = StringVar()
addLveinticuatro = StringVar()

Luno = Entry(root, textvariable=addLuno)
Luno.place(x=50, y=30)
Ldos = Entry(root, textvariable=addLdos)
Ldos.place(x=50, y=60)
Ltres = Entry(root, textvariable=addLtres)
Ltres.place(x=50, y=90)
Lcuatro = Entry(root, textvariable=addLcuatro)
Lcuatro.place(x=50, y=120)
Lcinco = Entry(root, textvariable=addLcinco)
Lcinco.place(x=50, y=150)
Lseis = Entry(root, textvariable=addLseis)
Lseis.place(x=50, y=180)
Lsiete = Entry(root, textvariable=addLsiete)
Lsiete.place(x=50, y=210)
Locho = Entry(root, textvariable=addLocho)
Locho.place(x=50, y=240)
Lnueve = Entry(root, textvariable=addLnueve)
Lnueve.place(x=50, y=270)
Ldiez = Entry(root, textvariable=addLdiez)
Ldiez.place(x=50, y=300)
Lonce = Entry(root, textvariable=addLonce)
Lonce.place(x=50, y=330)
Ldoce = Entry(root, textvariable=addLdoce)
Ldoce.place(x=50, y=360)
Ltrece = Entry(root, textvariable=addLtrece)
Ltrece.place(x=50, y=390)
Lcatorce = Entry(root, textvariable=addLcatorce)
Lcatorce.place(x=50, y=420)
Lquince = Entry(root, textvariable=addLquince)
Lquince.place(x=50, y=450)
Ldieciseis = Entry(root, textvariable=addLdieciseis)
Ldieciseis.place(x=50, y=480)
Ldiecisiete = Entry(root, textvariable=addLdiecisiete)
Ldiecisiete.place(x=50, y=510)
Ldieciocho = Entry(root, textvariable=addLdieciocho)
Ldieciocho.place(x=50, y=540)
Ldiecinueve = Entry(root, textvariable=addLdiecinueve)
Ldiecinueve.place(x=50, y=570)
Lveinte = Entry(root, textvariable=addLveinte)
Lveinte.place(x=50, y=600)
Lveintiuno = Entry(root, textvariable=addLveintiuno)
Lveintiuno.place(x=50, y=630)
Lveintidos = Entry(root, textvariable=addLveintidos)
Lveintidos.place(x=50, y=660)
Lveintitres = Entry(root, textvariable=addLveintitres)
Lveintitres.place(x=50, y=690)
Lveinticuatro = Entry(root, textvariable=addLveinticuatro)
Lveinticuatro.place(x=50, y=720)

# Valores A

addAuno = StringVar()
addAdos = StringVar()
addAtres = StringVar()
addAcuatro = StringVar()
addAcinco = StringVar()
addAseis = StringVar()
addAsiete = StringVar()
addAocho = StringVar()
addAnueve = StringVar()
addAdiez = StringVar()
addAonce = StringVar()
addAdoce = StringVar()
addAtrece = StringVar()
addAcatorce = StringVar()
addAquince = StringVar()
addAdieciseis = StringVar()
addAdiecisiete = StringVar()
addAdieciocho = StringVar()
addAdiecinueve = StringVar()
addAveinte = StringVar()
addAveintiuno = StringVar()
addAveintidos = StringVar()
addAveintitres = StringVar()
addAveinticuatro = StringVar()

Auno = Entry(root, textvariable=addAuno)
Auno.place(x=200, y=30)
Ados = Entry(root, textvariable=addAdos)
Ados.place(x=200, y=60)
Atres = Entry(root, textvariable=addAtres)
Atres.place(x=200, y=90)
Acuatro = Entry(root, textvariable=addAcuatro)
Acuatro.place(x=200, y=120)
Acinco = Entry(root, textvariable=addAcinco)
Acinco.place(x=200, y=150)
Aseis = Entry(root, textvariable=addAseis)
Aseis.place(x=200, y=180)
Asiete = Entry(root, textvariable=addAsiete)
Asiete.place(x=200, y=210)
Aocho = Entry(root, textvariable=addAocho)
Aocho.place(x=200, y=240)
Anueve = Entry(root, textvariable=addAnueve)
Anueve.place(x=200, y=270)
Adiez = Entry(root, textvariable=addAdiez)
Adiez.place(x=200, y=300)
Aonce = Entry(root, textvariable=addAonce)
Aonce.place(x=200, y=330)
Adoce = Entry(root, textvariable=addAdoce)
Adoce.place(x=200, y=360)
Atrece = Entry(root, textvariable=addAtrece)
Atrece.place(x=200, y=390)
Acatorce = Entry(root, textvariable=addAcatorce)
Acatorce.place(x=200, y=420)
Aquince = Entry(root, textvariable=addAquince)
Aquince.place(x=200, y=450)
Adieciseis = Entry(root, textvariable=addAdieciseis)
Adieciseis.place(x=200, y=480)
Adiecisiete = Entry(root, textvariable=addAdiecisiete)
Adiecisiete.place(x=200, y=510)
Adieciocho = Entry(root, textvariable=addAdieciocho)
Adieciocho.place(x=200, y=540)
Adiecinueve = Entry(root, textvariable=addAdiecinueve)
Adiecinueve.place(x=200, y=570)
Aveinte = Entry(root, textvariable=addAveinte)
Aveinte.place(x=200, y=600)
Aveintiuno = Entry(root, textvariable=addAveintiuno)
Aveintiuno.place(x=200, y=630)
Aveintidos = Entry(root, textvariable=addAveintidos)
Aveintidos.place(x=200, y=660)
Aveintitres = Entry(root, textvariable=addAveintitres)
Aveintitres.place(x=200, y=690)
Aveinticuatro = Entry(root, textvariable=addAveinticuatro)
Aveinticuatro.place(x=200, y=720)

# Valores B

addBuno = StringVar()
addBdos = StringVar()
addBtres = StringVar()
addBcuatro = StringVar()
addBcinco = StringVar()
addBseis = StringVar()
addBsiete = StringVar()
addBocho = StringVar()
addBnueve = StringVar()
addBdiez = StringVar()
addBonce = StringVar()
addBdoce = StringVar()
addBtrece = StringVar()
addBcatorce = StringVar()
addBquince = StringVar()
addBdieciseis = StringVar()
addBdiecisiete = StringVar()
addBdieciocho = StringVar()
addBdiecinueve = StringVar()
addBveinte = StringVar()
addBveintiuno = StringVar()
addBveintidos = StringVar()
addBveintitres = StringVar()
addBveinticuatro = StringVar()

Buno = Entry(root, textvariable=addBuno)
Buno.place(x=350, y=30)
Bdos = Entry(root, textvariable=addBdos)
Bdos.place(x=350, y=60)
Btres = Entry(root, textvariable=addBtres)
Btres.place(x=350, y=90)
Bcuatro = Entry(root, textvariable=addBcuatro)
Bcuatro.place(x=350, y=120)
Bcinco = Entry(root, textvariable=addBcinco)
Bcinco.place(x=350, y=150)
Bseis = Entry(root, textvariable=addBseis)
Bseis.place(x=350, y=180)
Bsiete = Entry(root, textvariable=addBsiete)
Bsiete.place(x=350, y=210)
Bocho = Entry(root, textvariable=addBocho)
Bocho.place(x=350, y=240)
Bnueve = Entry(root, textvariable=addBnueve)
Bnueve.place(x=350, y=270)
Bdiez = Entry(root, textvariable=addBdiez)
Bdiez.place(x=350, y=300)
Bonce = Entry(root, textvariable=addBonce)
Bonce.place(x=350, y=330)
Bdoce = Entry(root, textvariable=addBdoce)
Bdoce.place(x=350, y=360)
Btrece = Entry(root, textvariable=addBtrece)
Btrece.place(x=350, y=390)
Bcatorce = Entry(root, textvariable=addBcatorce)
Bcatorce.place(x=350, y=420)
Bquince = Entry(root, textvariable=addBquince)
Bquince.place(x=350, y=450)
Bdieciseis = Entry(root, textvariable=addBdieciseis)
Bdieciseis.place(x=350, y=480)
Bdiecisiete = Entry(root, textvariable=addBdiecisiete)
Bdiecisiete.place(x=350, y=510)
Bdieciocho = Entry(root, textvariable=addBdieciocho)
Bdieciocho.place(x=350, y=540)
Bdiecinueve = Entry(root, textvariable=addBdiecinueve)
Bdiecinueve.place(x=350, y=570)
Bveinte = Entry(root, textvariable=addBveinte)
Bveinte.place(x=350, y=600)
Bveintiuno = Entry(root, textvariable=addBveintiuno)
Bveintiuno.place(x=350, y=630)
Bveintidos = Entry(root, textvariable=addBveintidos)
Bveintidos.place(x=350, y=660)
Bveintitres = Entry(root, textvariable=addBveintitres)
Bveintitres.place(x=350, y=690)
Bveinticuatro = Entry(root, textvariable=addBveinticuatro)
Bveinticuatro.place(x=350, y=720)

L = ["37.98", "65.71", "49.92", "43.14", "55.11", "70.71",
     "62.66", "40.02", "51.12", "30.32", "72.53", "71.94", "28.78", "55.26",
     "42.1", "81.73", "51.94", "51.04", "96.54", "81.26", "66.77",
     "50.87", "35.66", "20.46"]

A = ["13.55", "18.13", "-4.88", "-13.09", "8.84", "-33.4", "36.07", "10.41",
     "48.24", "22.98", "-23.71", "19.36", "14.18", "-38.34", "53.38", "4.04",
     "49.99", "-28.63", "-0.42", "-0.64", "-0.73", "-0.15", "-0.42", "-0.08"]

B = ["14.06", "17.81", "-21.95", "21.9", "-25.4", "-0.19", "57.1", "-45.96", "16.25", "-21.59",
     "57.25", "67.85", "-50.3", "31.37", "28.19", "79.82", "-14.57", "-28.64", "1.19", "-0.33",
     "-0.5", "-0.27", "-1.23", "-0.97"]


def calculo():
    try:
        runo = math.sqrt(float((float(L[0]) - float(Luno.get())) ** 2 + (float(A[0]) - float(Auno.get())) ** 2 +
                               (float(B[0]) - float(Buno.get())) ** 2))
        rdos = math.sqrt(float((float(L[1]) - float(Ldos.get())) ** 2 + (float(A[1]) - float(Ados.get())) ** 2 +
                               (float(B[1]) - float(Bdos.get())) ** 2))
        rtres = math.sqrt(float((float(L[2]) - float(Ltres.get())) ** 2 + (float(A[2]) - float(Atres.get())) ** 2 +
                                (float(B[2]) - float(Btres.get())) ** 2))
        rcuatro = math.sqrt(float((float(L[3]) - float(Lcuatro.get())) ** 2 + (float(A[3]) - float(Acuatro.get()))
                                  ** 2 + (float(B[3]) - float(Bcuatro.get())) ** 2))
        rcinco = math.sqrt(float((float(L[4]) - float(Lcinco.get())) ** 2 + (float(A[4]) - float(Acinco.get())) ** 2 +
                                 (float(B[4]) - float(Bcinco.get())) ** 2))
        rseis = math.sqrt(float((float(L[5]) - float(Lseis.get())) ** 2 + (float(A[5]) - float(Aseis.get())) ** 2 +
                                (float(B[5]) - float(Bseis.get())) ** 2))
        rsiete = math.sqrt(float((float(L[6]) - float(Lsiete.get())) ** 2 + (float(A[6]) - float(Asiete.get())) ** 2 +
                                 (float(B[6]) - float(Bsiete.get())) ** 2))
        rocho = math.sqrt(float((float(L[7]) - float(Locho.get())) ** 2 + (float(A[7]) - float(Aocho.get())) ** 2 +
                                (float(B[7]) - float(Bocho.get())) ** 2))
        rnueve = math.sqrt(float((float(L[8]) - float(Lnueve.get())) ** 2 + (float(A[8]) - float(Anueve.get())) ** 2 +
                                 (float(B[8]) - float(Bnueve.get())) ** 2))
        rdiez = math.sqrt(float((float(L[9]) - float(Ldiez.get())) ** 2 + (float(A[9]) - float(Adiez.get())) ** 2 +
                                (float(B[9]) - float(Bdiez.get())) ** 2))
        ronce = math.sqrt(float((float(L[10]) - float(Lonce.get())) ** 2 + (float(A[10]) - float(Aonce.get())) ** 2 +
                                (float(B[10]) - float(Bonce.get())) ** 2))
        rdoce = math.sqrt(float((float(L[11]) - float(Ldoce.get())) ** 2 + (float(A[11]) - float(Adoce.get())) ** 2 +
                                (float(B[11]) - float(Bdoce.get())) ** 2))
        rtrece = math.sqrt(float((float(L[12]) - float(Ltrece.get())) ** 2 + (float(A[12]) - float(Atrece.get())) ** 2 +
                                 (float(B[12]) - float(Btrece.get())) ** 2))
        rcatorce = math.sqrt(float((float(L[13]) - float(Lcatorce.get())) ** 2 + (float(A[13]) - float(Acatorce.get()))
                                   ** 2 + (float(B[13]) - float(Bcatorce.get())) ** 2))
        rquince = math.sqrt(float((float(L[14]) - float(Lquince.get())) ** 2 + (float(A[14]) - float(Aquince.get()))
                                  ** 2 + (float(B[14]) - float(Bquince.get())) ** 2))
        rdieciseis = math.sqrt(float((float(L[15]) - float(Ldieciseis.get())) ** 2 +
                                     (float(A[15]) - float(Adieciseis.get())) ** 2 +
                                     (float(B[15]) - float(Bdieciseis.get())) ** 2))
        rdiecisiete = math.sqrt(float((float(L[16]) - float(Ldiecisiete.get())) ** 2 +
                                      (float(A[16]) - float(Adiecisiete.get())) ** 2 +
                                      (float(B[16]) - float(Bdiecisiete.get())) ** 2))
        rdieciocho = math.sqrt(float((float(L[17]) - float(Ldieciocho.get())) ** 2 +
                                     (float(A[17]) - float(Adieciocho.get())) ** 2 +
                                     (float(B[17]) - float(Bdieciocho.get())) ** 2))
        rdiecinueve = math.sqrt(float((float(L[18]) - float(Ldiecinueve.get())) ** 2 +
                                      (float(A[18]) - float(Adiecinueve.get())) ** 2 +
                                      (float(B[18]) - float(Bdiecinueve.get())) ** 2))
        rveinte = math.sqrt(float((float(L[19]) - float(Lveinte.get())) ** 2 + (float(A[19]) - float(Aveinte.get()))
                                  ** 2 + (float(B[19]) - float(Bveinte.get())) ** 2))
        rveintiuno = math.sqrt(float((float(L[20]) - float(Lveintiuno.get())) ** 2 +
                                     (float(A[20]) - float(Aveintiuno.get())) ** 2 +
                                     (float(B[20]) - float(Bveintiuno.get())) ** 2))
        rveintidos = math.sqrt(float((float(L[21]) - float(Lveintidos.get())) ** 2 +
                                     (float(A[21]) - float(Aveintidos.get())) ** 2 +
                                     (float(B[21]) - float(Bveintidos.get())) ** 2))
        rveintitres = math.sqrt(float((float(L[22]) - float(Lveintitres.get())) ** 2 +
                                      (float(A[22]) - float(Aveintitres.get())) ** 2 +
                                      (float(B[22]) - float(Bveintitres.get())) ** 2))
        rveinticuatro = math.sqrt(float((float(L[23]) - float(Lveinticuatro.get())) ** 2 +
                                        (float(A[23]) - float(Aveinticuatro.get())) ** 2 +
                                        (float(B[23]) - float(Bveinticuatro.get())) ** 2))
        resultados = (runo + rdos + rtres + rcuatro + rcinco + rseis + rsiete + rocho +
                      rnueve + rdiez + ronce + rdoce + rtrece + rcatorce + rquince +
                      rdieciseis + rdiecisiete + rdieciocho + rdiecinueve + rveinte +
                      rveintiuno + rveintidos + rveintitres + rveinticuatro)
        resultado = float(resultados) / 24
        deltae = Label(root, text=f"ΔE= {resultado} ", font='bold 18')
        deltae.config(justify="center", fg="white", bg="#7c7c7c")
        deltae.place(x=500, y=100)

    except ValueError:
        alerta()


def alerta():
    messagebox.showerror("Alerta", "Faltan valores o uno de los valores es incorrecto")


calcular = ttk.Button(root, text="Calcular", command=calculo)
calcular.place(x=500, y=30)
info = Label(root, text="Fórmula CIE76", font='bold 15')
info.config(justify="center", fg="white", bg="#7c7c7c")
info.place(x=650, y=740)
usar = Label(root, text="Cálculos para X-rite Colorchecker Color Rendition Chart", font='bold 10')
usar.config(justify="center", fg="white", bg="#7c7c7c")
usar.place(x=10, y=750)
tolerancia = Label(root, text=f"Resultado aceptable menor a 5", font='bold 15')
tolerancia.config(justify="center", fg="white", bg="#7c7c7c")
tolerancia.place(x=500, y=300)

root.mainloop()
