from tkinter import *
from tkinter import messagebox
root=Tk()

root.title("Datos")
root.geometry("400x200+500+300")



#----(Funciones de app)-----
def acercadeMenu():
    messagebox.showinfo("Acerca de..","Prueba de Franco Rottondi\n Aprendiendo 1.0")
def destruirRoot():
    messagebox.showinfo("Gracias","Es algo simple \n gracias por probarlo!\n\n**Franco Rottondi**")
    exit()

def DatosUser():
    if nomIuser.get()=="" or apellIuser.get()=="" or edadIuser.get=="":
        messagebox.showerror("Atencion!","Faltan datos")
    else:
        nombre1 = nomIuser.get()
        labelNombre = Label(frame1)
        labelNombre.config(text=nombre1)
        labelNombre.grid(column=2, row=1)
        nomIuser.destroy()

        apellido1 = apellIuser.get()
        labelApellido = Label(frame1)
        labelApellido.config(text=apellido1)
        labelApellido.grid(column=2, row=2)
        apellIuser.destroy()

        boton1.destroy()
        try:
            edad1 = int(edadIuser.get())
            labelEdad = Label(frame1)
            labelEdad.config(text=edad1, justify="center")
            labelEdad.grid(column=2, row=3)
            edadIuser.destroy()
        except:
            messagebox.showwarning("Error!", "La edad debe ser numerica!")

            #Creando funcion para abrir ventana en caso de error
            def Nuevavenanitaparalaedad():
                def cierreVN():
                    try:
                        edad1=int(entryEdadNueva.get())

                    except:
                        messagebox.showerror("Error!","Se cerrara el programa")
                        exit()

                    edadIuser.destroy()
                    labelEdad = Label(frame1)
                    labelEdad.config(text=edad1, justify="center")
                    labelEdad.grid(column=2, row=3)
                    boton1.destroy()

                    boton2 = Button(frame1, text="Gracias, Hasta luego!\n(Push me too)", command=destruirRoot)
                    boton2.grid(column=2, row=4)

                    root3.destroy()

                #Ventana extra para nueva edad
                root3=Tk()
                root3.title("Corrector de Edad")
                root3.geometry("300x100+500+300")
                labelEdadNueva=Label(root3,text="Ingresa la edad nueva: \n Correctamente")
                labelEdadNueva.pack()

                entryEdadNueva=Entry(root3,bd=2,textvariable=lambda:edad1)
                entryEdadNueva.pack()


                boton3=Button(root3,bd=2,text="Submit",command=lambda:cierreVN())
                boton3.pack()

                root3.mainloop()


            Nuevavenanitaparalaedad()





        boton2=Button(frame1, text="Gracias, Hasta luego!\n(Push me too)",command=destruirRoot)
        boton2.grid(column=2,row=4)

#------(fin funciones)----------
#-----------(menu bar)---------

menubar = Menu(root)
root.config(menu=menubar)

ArchivoMenu=Menu(menubar,tearoff=0)
ayudaMenu=Menu(menubar,tearoff=0)

menubar.add_cascade(label="Archivo",menu=ArchivoMenu)
menubar.add_cascade(label="Ayuda",menu=ayudaMenu)

ayudaMenu.add_command(label="Acerca de...",command=acercadeMenu)
ArchivoMenu.add_command(label="Salir",command=root.quit)

#------(GUI)----------

frame1=Frame(root,padx=25,pady=25)
frame1.pack()

nombrepro=Label(frame1,text="¡Bienvenido!")
nombrepro.config(padx=1,pady=2,justify="center")
nombrepro.grid(column=0,row=0)


#---------------------------------------------------

nomUser=Label(frame1,bd=1,text="Ingrese su nombre:",fg="Blue",justify="left")
nomUser.grid(column=0,row=1)

nombreUsuario=StringVar()
nomIuser=Entry(frame1,bd=2,textvariable=lambda:nombreUsuario)
nomIuser.grid(column=2,row=1)

apellUser=Label(frame1,bd=1,text="Ingrese su apellido:",fg="Blue",justify="left")
apellUser.grid(column=0,row=2)

apellidoUsuario=StringVar()
apellIuser=Entry(frame1,bd=2,textvariable=lambda:apellidoUsuario)
apellIuser.grid(column=2,row=2)

edadUser=Label(frame1,bd=1,text="Ingrese su edad:",fg="Blue",justify="left")
edadUser.grid(column=0,row=3)

edadUsuario=IntVar()
edadIuser=Entry(frame1,bd=2,textvariable=lambda:edadUsuario)
edadIuser.grid(column=2,row=3)

#--------------Boton enviar a Label-------------------------
boton1=Button(frame1,text="Push IT!",command=lambda:DatosUser())
boton1.grid(column=4,row=2)


root.mainloop()