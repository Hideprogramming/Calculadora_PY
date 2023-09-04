from tkinter import * 

ventana = Tk()

ventana.title(" Calculadora ")


# Entrada de texto
texto = Entry( ventana, font = ("Calibri 20") ) 
texto.grid( row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)  



# Botones
Button1 = Button(ventana, text = " 1 ", width = 5, height = 2, command = lambda: click( 1 ))
Button2 = Button(ventana, text = " 2 ", width = 5, height = 2, command = lambda: click( 2 ))
Button3 = Button(ventana, text = " 3 ", width = 5, height = 2, command = lambda: click( 3 ))
Button4 = Button(ventana, text = " 4 ", width = 5, height = 2, command = lambda: click( 4 ))
Button5 = Button(ventana, text = " 5 ", width = 5, height = 2, command = lambda: click( 5 ))
Button6 = Button(ventana, text = " 6 ", width = 5, height = 2, command = lambda: click( 6 ))
Button7 = Button(ventana, text = " 7 ", width = 5, height = 2, command = lambda: click( 7 ))
Button8 = Button(ventana, text = " 8 ", width = 5, height = 2, command = lambda: click( 8 ))
Button9 = Button(ventana, text = " 9 ", width = 5, height = 2, command = lambda: click( 9 ))
Button0 = Button(ventana, text = " 0 ", width = 15, height = 2, command = lambda: click( 0 ))

Button_Borrar = Button(ventana, text = " AC ", width = 5, height = 2, command = lambda: borrar())
Button_ParentesisA = Button(ventana, text = " ( ", width = 5, height = 2, command = lambda: click(" ( "))
Button_ParentesisC = Button(ventana, text = " ) ", width = 5, height = 2, command = lambda: click( " ) "))
Button_Punto = Button(ventana, text = " . ", width = 5, height = 2, command = lambda: click( " . "))

Button_Suma = Button(ventana, text = " + ", width = 5, height = 2, command = lambda: click( " + "))
Button_Resta = Button(ventana, text = " - ", width = 5, height = 2, command = lambda: click( " - "))
Button_Multiplicacion = Button(ventana, text = " * ", width = 5, height = 2, command = lambda: click( " * "))
Button_Division = Button(ventana, text = " / ", width = 5, height = 2, command = lambda: click( " / "))


Button_Igual = Button(ventana, text = " = ", width = 5, height = 2, command = lambda: operacion())

# Botones en pantalla
Button_Borrar.grid(row = 1, column = 0 , padx = 5, pady = 5)
Button_ParentesisA.grid(row = 1, column = 1 , padx = 5, pady = 5)
Button_ParentesisC.grid(row = 1, column = 2 , padx = 5, pady = 5)
Button_Division.grid(row = 1, column = 3 , padx = 5, pady = 5)

Button7.grid(row = 2, column = 0 , padx = 5, pady = 5)
Button8.grid(row = 2, column = 1 , padx = 5, pady = 5)
Button9.grid(row = 2, column = 2, padx = 5, pady = 5)
Button_Multiplicacion.grid(row = 2, column = 3 , padx = 5, pady = 5)

Button4.grid(row = 3, column = 0 , padx = 5, pady = 5)
Button5.grid(row = 3, column = 1 , padx = 5, pady = 5)
Button6.grid(row = 3, column = 2 , padx = 5, pady = 5)
Button_Resta.grid(row = 3, column = 3 , padx = 5, pady = 5)

Button1.grid(row = 4, column = 0 , padx = 5, pady = 5)
Button2.grid(row = 4, column = 1 , padx = 5, pady = 5)
Button3.grid(row = 4, column = 2 , padx = 5, pady = 5)
Button_Suma.grid(row = 4, column = 3 , padx = 5, pady = 5)

Button0.grid(row = 5, column = 0 , columnspan = 2, padx = 5, pady = 5)
Button_Punto.grid(row = 5, column = 2 , padx = 5, pady = 5)
Button_Igual.grid(row = 5, column = 3 , padx = 5, pady = 5)


# Funciones
i = 0

def click(valor):
    global i
    texto.insert(i, valor)
    i += 1

def borrar():
    texto.delete(0, END)
    i = 0

def operacion():
    ecuacion = texto.get()
    resultado = eval(ecuacion)
    texto.delete(0, END)
    texto.insert(0, resultado)
    i = 0




ventana.mainloop()