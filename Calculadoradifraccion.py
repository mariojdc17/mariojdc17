from tkinter import *
from tkinter import Entry

root = Tk()
root.geometry("450x600")
root.resizable(FALSE, FALSE)
root.title('Calculadora de difracción')
root.config(background="gray")
tamanocensor1 = Label(root, text="Tamaño del censor vertical:", fg="white", bg="gray", font=8)
tamanocensor1.place(x=15, y=50)
tamanocensor2 = Label(root, text="Tamaño del censor horizontal:", fg="white", bg="gray", font=8)
tamanocensor2.place(x=15, y=125)
resolucioncensor1 = Label(root, text="Resolución del censor vertical:", fg="white", bg="gray", font=8)
resolucioncensor1.place(x=15, y=200)
resolucioncensor2 = Label(root, text="Resolución del censor horizontal:", fg="white", bg="gray", font=8)
resolucioncensor2.place(x=15, y=275)
distanciaf = Label(root, text="Distancia focal:", fg="white", bg="gray", font=8)
distanciaf.place(x=15, y=350)
disobj = Label(root, text="Distancia al objeto:", fg="white", bg="gray", font=8)
disobj.place(x=20, y=425)
tamanocensorv: Entry = Entry(root)
tamanocensorv.config(justify="center")
tamanocensorv.place(x=275, y=50)
tamanocensorh = Entry(root)
tamanocensorh.config(justify="center")
tamanocensorh.place(x=275, y=125)
resolucionv = Entry(root)
resolucionv.config(justify="center")
resolucionv.place(x=275, y=200)
resolucionh = Entry(root)
resolucionh.config(justify="center")
resolucionh.place(x=275, y=275)
distanciafocal = Entry(root)
distanciafocal.config(justify="center")
distanciafocal.place(x=275, y=350)
distanciaobjeto = Entry(root)
distanciaobjeto.config(justify="center")
distanciaobjeto.place(x=275, y=425)


def calculo():
    try:
        tv = float(tamanocensorv.get())
        th = float(tamanocensorh.get())
        rv = float(resolucionv.get())
        rh = float(resolucionh.get())
        df = float(distanciafocal.get())
        d = float(distanciaobjeto.get())
        dobj = d * 1000
        contantes = (2.44 * 0.000555)
        m = df / dobj
        f = ((((tv / rv) + (th / rh)) / 2) * 2) / (contantes * (1 + m))
        print(f)
        resultado = Label(root, text=f"f= {f} ", font="500")
        resultado.config(justify="center", fg="black", bg="grey")
        resultado.place(x=200, y=525)
    except ValueError:
        resultado = Label(root, text=f"Insertar valor", font="500")
        resultado.config(justify="center", fg="black", bg="grey")
        resultado.place(x=200, y=525)


calcular = Button(root, text="Calcular", command=calculo)
calcular.place(x=20, y=530)
crador = Label(root, text="Creada por Mario Dutruel", fg="white", bg="gray")
crador.place(x=10, y=575, width=150, height=20)

root.mainloop()
