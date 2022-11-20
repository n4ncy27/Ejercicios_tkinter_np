# se importa la librería tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

# --------------------
# funciones de la app
# --------------------

def sumar():
    # messagebox.showinfo("Suma 1.0", "Hizo click en el boton sumar...")
    z = int(x.get()) + int(y.get())
    t_resultados.insert(INSERT, "La suma de " + x.get() + " + " + y.get() + " casi siempre es " + str(z) + "\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados..")
    x.set("")
    y.set("")
    t_resultados.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrará..")
    ventana_principal.destroy()

# ------------------
# ventana principal
# ------------------

# se crea una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas UIS")

# tamañan de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg= "black")

# ------------------
# variables globales
# ------------------
x = StringVar()
y = StringVar()

# ------------------------
# frame entrada datos
# ------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=240)
frame_entrada.place(x=10,y=10)

# logo de la app
logo = PhotoImage(file="img/logo_uis.png")
lb_logo = Label(frame_entrada, image=logo)
lb_logo.place(x=61,y=61)

# etiqueta para el titulo de la app
titulo = Label(frame_entrada, text= "Suma Enteros")
titulo.config(bg="white", fg="blue", font=("Arial",16))
titulo.place(x=240,y=10, width=230, height=30)

# etiqueta para x
lb_x = Label(frame_entrada, text = "X = ")
lb_x.config(bg="white", fg="blue", font=("Arial",16))
lb_x.place(x=240, y=50, width=115, height=30)

# entry para x
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(font=("Arial",20), justify=LEFT, fg="blue")
entry_x.focus_set()
entry_x.place(x=355,y=50,width=115, height=30)

# etiqueta para y
lb_y = Label(frame_entrada, text = "Y = ")
lb_y.config(bg="white", fg="blue", font=("Arial",16))
lb_y.place(x=240, y=90, width=115, height=30)

# entry para y
entry_y = Entry(frame_entrada,textvariable=y)
entry_y.config(font=("Arial",20), justify=LEFT, fg="blue")
entry_y.place(x=355,y=90,width=115, height=30)

# ------------------------
# frame operaciones
# ------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=120)
frame_operaciones.place(x=10,y=260)

# boton para sumar
bt_sumar = Button(frame_operaciones, text="Sumar", command=sumar)
bt_sumar.place(x=45,y=45, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190,y=45, width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones, text="Salir", command=salir)
bt_salir.place(x=335,y=45, width=100, height=30)

# ------------------------
# frame resultados
# ------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=100)
frame_resultados.place(x=10,y=390)

# area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="green", fg="black", font=("Arial",20))
t_resultados.place(x=10,y=10,width=460,height=80)

# se ejecuta el metodo mainloop() de la clase Tk a través de la instancia ventana_principal.  Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc)  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()