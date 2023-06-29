import customtkinter as ctk
import tkinter as tk
opciones={"movilidad geografica":20,
          "modificacion sustancial de las condiciones de trabajo":20,
          "incumplimiento empresa":33,
          "despido improcedente":33,
          "causas objetivas":20,
          "colectivo y fuerza mayor":20
          }

#front-end
root=ctk.CTk()
root.geometry("800x600")
root.iconbitmap("logo.ico")
root.title("calculadora")
root.resizable(0,0)
#tkinter menu 
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
def info ():
    from tkinter import messagebox
    messagebox.showinfo("info", "para añadir los complementos escriba en la caja el numero y pulse el boton, si quieres añadir mas borre el numero ya escrito y haga lo mismo, por favor siempre escriba numeros positivos")
def save():
    import datetime
    now = datetime.datetime.now()
    hora=now.strftime("%Y-%m-%d %H %M %S")
    file=open(f"nominas/{hora}.txt","w")
    file.write(f"el salario es: {sbt.get()}\nlas horas extras son: {hxt.get()} \nla antiguedad es: {antg.get()}\n")
    if len(cache) != 0:
        file.write("complementos:\n")
        for i in range(len(cache)):
            file.write(f"{cache[i]} \n")
        
# Create the file menu
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="opciones", menu=file_menu)
file_menu.add_command(label="info", command=info)
file_menu.add_command(label="save", command=save)
cache =[]
#menu
#titulo
ctk.CTkLabel(root,text="Calculadora indemnizaciones",font=("Arial",30)).place(relx=0.3,rely=0)
#salario base
ctk.CTkLabel(root,text="SALARIO BASE",font=("Arial",20)).place(relx=0.1,rely=0.3)
sbt=ctk.CTkEntry(root,width=50)
sbt.place(relx=0.1,rely=0.35)
#horas extras
ctk.CTkLabel(root,text="PAGAS EXTRA",font=("Arial",20)).place(relx=0.1,rely=0.45)
hxt=ctk.CTkEntry(root,width=50)
hxt.place(relx=0.1,rely=0.5)
#complementos
complementoslista=[]
ctk.CTkLabel(root,text="COMPLEMENTOS",font=("Arial",20)).place(relx=0.4,rely=0.3)
compt=ctk.CTkEntry(root,width=50)
compt.place(relx=0.4,rely=0.35)
def add():
    intcompt=int(compt.get())
    complementoslista.append(intcompt)
    labelcomp = ctk.CTkLabel(root, text="\n".join([str(elem) for elem in complementoslista]) + "\n", font=("Arial", 20))
    labelcomp.place(relx=0.7,rely=0.4,)
ctk.CTkButton(root,text="AÑADIR",command=add,width=50).place(relx=0.5,rely=0.35)
#antiguedad
ctk.CTkLabel(root,text="ANTIGUEDAD",font=("Arial",20)).place(relx=0.4,rely=0.45)
antg=ctk.CTkEntry(root,width=50)
antg.place(relx=0.4,rely=0.5)
#menu
menu=ctk.CTkComboBox(root,values=list(opciones.keys()))
menu.place(relx=0.4,rely=0.6)
#botones
def calcular():
    cache.clear()
    if menu.get()=="movilidad geografica":
        mns=12
        dias=20
    elif menu.get()=="modificacion sustancial de las condiciones de trabajo":
        mns=9
        dias=20
    elif menu.get()=="incumplimiento empresa":
        mns=24
        dias=33
    elif menu.get()=="despido improcedente":
        mns=24
        dias=33
    elif menu.get()=="causas objetivas":
        mns=12
        dias=20
    elif menu.get()=="colectivo y fuerza mayor":
        mns=12
        dias=20
    suma=sum(complementoslista)
    try:
        salario=int(sbt.get())
        pagas=int(hxt.get())
        antiguedad=int(antg.get())
    except:
        from tkinter import messagebox
        messagebox.showerror("error","solo se admiten numeros")
    if salario<=0 or pagas<=0 or antiguedad<=0:
        from tkinter import messagebox
        messagebox.showerror("error","solo se admiten numeros positivos")
    anual=(salario + suma )*12 + salario*pagas
    dia=round(anual/365,2)
    mes=round(anual/12,2)
    indemnizacion=round(dias*dia*antiguedad,2)
    limite=round(mns*mes,2)
    
    if indemnizacion>limite:
         ctk.CTkLabel(root,text=limite,font=("Arial",20)).place(relx=0.4,rely=0.8)
    else:
         ctk.CTkLabel(root,text=indemnizacion,font=("Arial",20)).place(relx=0.4,rely=0.8)
    for elem in complementoslista:
        cache.append(elem)   
    complementoslista.clear()
ctk.CTkButton(root,text="calcular",command=calcular).place(relx=0.4,rely=0.7)
#cierre ventana
root.mainloop()