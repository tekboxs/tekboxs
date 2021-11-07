import numpy as np
from tkinter import *
import tkinter as tk
from decimal import Decimal as dec
from tkinter import ttk


def erroFun():
    lbcalc["text"] = "ENTRADA INVALIDA, TENTE NOVAMENTE"


def convert():
    per1 = float(ed5.get())
    per2 = float(ed6.get())
    tax = float(ed7.get()) / 100
    ele = per2 / per1
    taxequi = pow((1 + tax), ele) - 1
    taxequi = taxequi * 100
    ed8.delete(0, 'end')
    ed8.insert(string=f'{taxequi:.5f}', index=2)


def use():
    novatax = ed8.get()
    ed2.delete(0, 'end')
    ed2.insert(string=f'{novatax}', index=2)


def calculo_c():
    # verificação de quem esta ativo
    cx = var1.get()
    ix = var2.get()
    tx = var3.get()
    mx = var4.get()
    # verificação de quem esta ativo

    if cx and ix and tx == 1 and mx == 0:
        c = dec(ed1.get())
        ta = (dec(ed2.get()) / 100) + 1
        te = dec(ed3.get())
        ele = pow(ta, te)
        m = c * pow(ta, te)
        j = m - c

        lb["text"] = 'Com o uso da formula: J = C * (1 + i) ^ t'
        lbcalc["text"] = f"""
        M = {c} * ({ta})^{te}

        M = {c} * {ele:.4f}

        Dessa forma os juros serão: {j:.4f}

        E o montante: {m:.4f}
        """

    elif cx and ix and mx == 1 and tx == 0:  # achar tempo
        c = float(ed1.get())
        m = float(ed4.get())
        ta = float(ed2.get())
        if c <= 0 or m <= 0:
            erroFun()

        else:

            ta = (ta / 100) + 1
            log1 = np.log(m / c)
            log2 = np.log(ta)
            te = log1 / log2
            lb["text"] = f"Com a formula : n = ln( Fv / Pv ) / ln( 1 + i )"
            lbcalc["text"] = f"""n = ln( {m} / {c}) / ln( {ta} ) => n = {log1:.4f} / {log2:.4f}

            Dessa forma o tempo será: {te:.4f} Periodos"""

    elif cx and mx and tx == 1 and ix == 0:  # achar taxa
        c = dec(ed1.get())
        m = dec(ed4.get())
        te = dec(ed3.get())

        if te == 0 or c == 0:
            print(f'aqui {c} {te}')
            erroFun()

        else:
            ta = pow((m / c), (1 / te)) - 1

            lb["text"] = f"Com a formula : i = (( Fv / Pv )^(1 / n)) - 1"
            lbcalc["text"] = f"""i = ({m} / {c})^(1 / {te}) - 1 => i = ({m / c:.4f})^({1 / te:.4f}) - 1

            Desse modo a taxa vale: {ta:.5f} ou {ta * 100:.5f}% """

    elif mx and ix and tx == 1 and cx == 0:
        ta = (dec(ed2.get()) / 100) + 1
        te = dec(ed3.get())
        m = dec(ed4.get())

        if ta or te == 0:
            erroFun()

        c = m / (pow(ta, te))
        lb["text"] = "Usando a formula: Fv = Pv ( 1 + i)^ n"
        lbcalc["text"] = f"""{m} = Pv ( {ta} )^{te}

        {m} = Pv * ( {pow(ta, te):.4f} ) => Pv = ({m} / {pow(ta, te):.4f})

        Assim o Capital equivale a : {c:.4f} Reais """

    else:
        erroFun()


def calculo_s():
    # verificação de quem esta ativo
    cx = var1.get()
    ix = var2.get()
    tx = var3.get()
    mx = var4.get()
    # verificação de quem esta ativo

    if cx and ix and tx == 1 and mx == 0:
        c = dec(ed1.get())
        ta = (dec(ed2.get()) / 100)
        te = dec(ed3.get())
        j = c * ta * te
        m = c+j

        lb["text"] = 'Com o uso da formula: J = C * i * t'
        lbcalc["text"] = f"""
            J = {c} * {ta} * {te}

            J = {c*ta*te}

            Dessa forma os juros serão: {j:.4f}

            E o montante: {m:.4f}
            """

    elif cx and ix and mx == 1 and tx == 0:  # achar tempo
        c = float(ed1.get())
        m = float(ed4.get())
        ta = float(ed2.get())
        if c <= 0 or m <= 0:
            erroFun()

        else:

            ta = (ta / 100) + 1
            log1 = np.log(m / c)
            log2 = np.log(ta)
            te = log1 / log2
            lb["text"] = f"Com a formula : n = ln( Fv / Pv ) / ln( 1 + i )"
            lbcalc["text"] = f"""n = ln( {m} / {c}) / ln( {ta} ) => n = {log1:.4f} / {log2:.4f}

                Dessa forma o tempo será: {te:.4f} Periodos"""

    elif cx and mx and tx == 1 and ix == 0:  # achar taxa
        c = dec(ed1.get())
        m = dec(ed4.get())
        te = dec(ed3.get())

        if te == 0 or c == 0:
            print(f'aqui {c} {te}')
            erroFun()

        else:
            ta = pow((m / c), (1 / te)) - 1

            lb["text"] = f"Com a formula : i = (( Fv / Pv )^(1 / n)) - 1"
            lbcalc["text"] = f"""i = ({m} / {c})^(1 / {te}) - 1 => i = ({m / c:.4f})^({1 / te:.4f}) - 1

                Desse modo a taxa vale: {ta:.5f} ou {ta * 100:.5f}% """

    elif mx and ix and tx == 1 and cx == 0:
        ta = (dec(ed2.get()) / 100) + 1
        te = dec(ed3.get())
        m = dec(ed4.get())

        if ta or te == 0:
            erroFun()

        c = m / (pow(ta, te))
        lb["text"] = "Usando a formula: Fv = Pv ( 1 + i)^ n"
        lbcalc["text"] = f"""{m} = Pv ( {ta} )^{te}

            {m} = Pv * ( {pow(ta, te):.4f} ) => Pv = ({m} / {pow(ta, te):.4f})

            Assim o Capital equivale a : {c:.4f} Reais """

    else:
        erroFun()


janela = tk.Tk()
janela.title('Juros')

ed1 = Entry(janela, font='arialblack')
ed1.grid(row=0, column=2)
ed1.insert(string='0', index=2)
labcap = Label(janela, text='Capital', font='arialblack')
labcap.grid(row=0, column=1)

ed2 = Entry(janela, font='arialblack')
ed2.grid(row=1, column=2)
ed2.insert(string='1', index=2)
labtax = Label(janela, text='Taxa', font='arialblack')
labtax.grid(row=1, column=1)

ed3 = Entry(janela, font='arialblack')
ed3.grid(row=2, column=2)
ed3.insert(string='1', index=2)
labtemp = Label(janela, text='Periodos', font='arialblack')
labtemp.grid(row=2, column=1)

ed4 = Entry(janela, font='arialblack')
ed4.grid(row=3, column=2)
ed4.insert(string='0', index=2)
labmont = Label(janela, text='Montante', font='arialblack')
labmont.grid(row=3, column=1)

var1 = tk.IntVar()
chk1 = ttk.Checkbutton(janela, text='', variable=var1)
chk1.grid(row=0, column=0)

var2 = tk.IntVar()
chk2 = ttk.Checkbutton(janela, text='', variable=var2)
chk2.grid(row=1, column=0)

var3 = tk.IntVar()
chk3 = ttk.Checkbutton(janela, text='', variable=var3)
chk3.grid(row=2, column=0)

var4 = tk.IntVar()
chk4 = ttk.Checkbutton(janela, text='', variable=var4)
chk4.grid(row=3, column=0)

bt1 = Button(janela, width=15, text="Calculo Simples", command=calculo_s)
bt1.grid(row=4, column=0, pady=50)

bt2 = Button(janela, width=15, text="Calculo Composto", command=calculo_c)
bt2.grid(row=4, column=1)

lb = Label(janela, text='', font='arialblack')
lb.place(x=480, y=10)

lbtitle = Label(janela, text='', font='arialblack')
# lbtitle.place(x=550, y=10)

lbcalc = Label(janela, text='', font='arialblack')
lbcalc.place(x=450, y=50)

var1.set(1), var2.set(1), var3.set(1), var4.set(0)  # tudo marcado - mont

ed5 = Entry(janela, justify='center', bg='yellow')
ed5.grid(row=6, column=2)
ed5.i

ed6 = Entry(janela, justify='center', bg='yellow')
ed6.grid(row=7, column=2)
ed6.insert(string='1', index=2)

labper = Label(janela, text='períodos').grid(row=5, column=2)  # label informativa

ed7 = Entry(janela, bg='yellow')
ed7.grid(row=6, column=1)
lbconv1 = Label(janela, text='taxa de juros (%):').grid(row=6, column=0)

ed8 = Entry(janela, fg='red')
ed8.grid(row=7, column=1)
lbconv2 = Label(janela, text='taxa equivalente (%):').grid(row=7, column=0)

btok = Button(janela, text='OK', command=convert, width=10, height=1, border='4').grid(row=8, column=1)
btuse = Button(janela, text='USAR', command=use, width=10, height=1, border='4').grid(row=8, column=2)

janela.geometry("850x405+200+100")  # Largura x altura + x + y

janela.mainloop()
