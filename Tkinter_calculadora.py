from tkinter import *

def envia_boton(valor):
	global una_vez
	global igual_usado
	global ultimo_es_ope
	if not igual_usado:
		ultimo_es_ope = False
		if operador != "" and not una_vez:  # Para que solo se borre una vez al introducir un digito despues del operador
			pantalla.delete(0, END)
			una_vez = True
		aux = pantalla.get()
		if aux == "0" and valor != ".":  # Posición inicial. Hay que borrar
				pantalla.delete(0, END)
				auxiliar = pantalla_feedback.get()
				print(auxiliar)
				auxiliar = auxiliar.rstrip("0")
				print(auxiliar)
				pantalla_feedback.delete(0, END)
				pantalla_feedback.insert(END, auxiliar)
		if valor == "." and aux.count(".") > 0:  # Si ya hay un punto
			pass
		else:  # Se inserta digito
			if valor == "." and aux == "":
				pantalla.insert(END, "0" + valor)
				pantalla_feedback.insert(END, "0" + valor)
			else:
				pantalla.insert(END, valor)
				pantalla_feedback.insert(END, valor)
	else:  # Si se acaba de usar el igual y se ha introducido un número
		limpiar()
		pantalla.delete(0, END)
		pantalla_feedback.delete(0, END)
		if valor == ".":
			pantalla.insert(END, "0" + valor)
			pantalla_feedback.insert(END, "0" + valor)
		else:
			pantalla.insert(END, valor)
			pantalla_feedback.insert(END, valor)
		#igual_usado = False
		#una_vez = True

def operacion(ope):
	if pantalla.get() != "Error (dividir entre 0)":
		global num1
		global num2
		global operador
		global operador_igual
		global num_operador
		global igual_usado
		global ultimo_es_ope
		if num_operador == 0:
			num1 = pantalla.get()
			num1 = float(num1)
			num_operador = 1
			operador = ope
			if igual_usado:  # Si coge el valor que viene del igual
				pantalla_feedback.delete(0, END)
				pantalla_feedback.insert(END, num1)
				igual_usado = False
			pantalla_feedback.insert(END, " " + ope + " ")
			print(ultimo_es_ope)
		elif num_operador == 1 and not ultimo_es_ope:
			operador_igual = ope
			num2 = pantalla.get()
			num_operador = 2
			igual()
		if ultimo_es_ope:  # Para cambiar de ope directamente
			auxiliar = pantalla_feedback.get()
			auxiliar = auxiliar.rstrip(" +-/*")
			pantalla_feedback.delete(0, END)
			pantalla_feedback.insert(END, auxiliar)
			operador = ope
			pantalla_feedback.insert(END, " " + ope + " ")
		ultimo_es_ope = True
	else:
		limpiar()

def igual():
	global una_vez
	global igual_usado
	global operador
	global num_operador
	global num1
	global num2
	if pantalla.get() != "Error (dividir entre 0)":
		if operador != "":
			if num_operador == 1:
				num2 = pantalla.get()
				igual_usado = True
				num_operador = 0
			if ultimo_es_ope:  # Para introducir el mismo valor en feedback, cuando se pulsa operador e igual sin num2
				pantalla_feedback.insert(END, num2)
				operador = ""
			num2 = float(num2)
			if operador == "+":
				pantalla.delete(0, END)
				pantalla.insert(0, num1 + num2)
				una_vez = False
				if num_operador == 2:
					pantalla_feedback.delete(0, END)
					print(f"num1= {num1} num2= {num2} operador_igual= {operador_igual}")
					pantalla_feedback.insert(END, str(num1 + num2) + " " + operador_igual + " ")
					num1 = num1 + num2
					operador = operador_igual
					num_operador = 1
			elif operador == "-":
				pantalla.delete(0, END)
				pantalla.insert(0, num1 - num2)
				una_vez = False
				if num_operador == 2:
					pantalla_feedback.delete(0, END)
					print(f"num1= {num1} num2= {num2} operador_igual= {operador_igual}")
					pantalla_feedback.insert(END, str(num1 - num2) + " " + operador_igual + " ")
					num1 = num1 - num2
					operador = operador_igual
					num_operador = 1
			elif operador == "*":
				pantalla.delete(0, END)
				pantalla.insert(0, num1 * num2)
				una_vez = False
				if num_operador == 2:
					pantalla_feedback.delete(0, END)
					print(f"num1= {num1} num2= {num2} operador_igual= {operador_igual}")
					pantalla_feedback.insert(END, str(num1 * num2) + " " + operador_igual + " ")
					num1 = num1 * num2
					operador = operador_igual
					num_operador = 1
			elif operador == "/":
				if num2 != 0.0:
					pantalla.delete(0, END)
					pantalla.insert(0, num1 / num2)
					una_vez = False
					if num_operador == 2:
						pantalla_feedback.delete(0, END)
						print(f"num1= {num1} num2= {num2} operador_igual= {operador_igual}")
						pantalla_feedback.insert(END, str(num1 / num2) + " " + operador_igual + " ")
						num1 = num1 / num2
						operador = operador_igual
						num_operador = 1
				else:
					pantalla.delete(0, END)
					pantalla.insert(0, "Error (dividir entre 0)")
					igual_usado = True
	else:
		limpiar()

def limpiar():
	global num1
	global num2
	global operador
	global operador_igual
	global num_operador
	global una_vez
	global igual_usado
	global ultimo_es_ope
	num1 = 0
	num2 = 0
	operador = ""
	operador_igual = ""
	num_operador = 0
	una_vez = False
	igual_usado = False
	ultimo_es_ope = False
	pantalla.delete(0, END)
	pantalla_feedback.delete(0, END)
	pantalla.insert(0, "0")
	pantalla_feedback.insert(0, "0")


root = Tk()
root.title("Calculadora de Grog")
# root.iconbitmap("img/guybrush3.ico")
root.resizable(0, 0) #Ejes x e y. si ponemos 0 es no permitido. 1 es permitido.
# root.geometry("296x362")

pantalla_feedback = Entry(root, bg="white", fg="grey", width=30, borderwidth=3, font=("arial", 18, "bold"))
pantalla_feedback.grid(row=0, padx=2, pady=2, columnspan=4)
pantalla = Entry(root, bg="white", fg="black", width=30, borderwidth=3, font=("arial", 18, "bold"))
pantalla.grid(row=1, padx=2, pady=2, columnspan=4)
pantalla.insert(0, "0")
pantalla_feedback.insert(0, "0")
num1 = ""
num2 = ""
operador = ""
operador_igual = ""
num_operador = 0
una_vez = False  # variable global para controlar que se borre la pantalla una sola vez justo después de introducir el operador.
igual_usado = False
ultimo_es_ope = False

boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="blue", cursor="fleur", command=lambda :envia_boton(1))
boton_1.grid(row=4, column=0)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="blue", cursor="fleur", command=lambda :envia_boton(2))
boton_2.grid(row=4, column=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="blue", cursor="fleur", command=lambda :envia_boton(3))
boton_3.grid(row=4, column=2)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="blue", cursor="fleur", command=lambda :envia_boton(4))
boton_4.grid(row=3, column=0)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="blue", cursor="fleur", command=lambda :envia_boton(5))
boton_5.grid(row=3, column=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="blue", cursor="fleur", command=lambda :envia_boton(6))
boton_6.grid(row=3, column=2)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="blue", cursor="fleur", command=lambda :envia_boton(7))
boton_7.grid(row=2, column=0)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="blue", cursor="fleur", command=lambda :envia_boton(8))
boton_8.grid(row=2, column=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="blue", cursor="fleur", command=lambda :envia_boton(9))
boton_9.grid(row=2, column=2)
boton_0 = Button(root, text="0", width=9, height=3, bg="white", fg="blue", cursor="fleur", command=lambda :envia_boton(0))
boton_0.grid(row=5, column=1)
boton_igual = Button(root, text="=", width=9, height=3, bg="aquamarine", fg="black", cursor="fleur", command=igual)
boton_igual.grid(row=5, column=0)
boton_coma = Button(root, text=",", width=9, height=3, bg="orange", fg="black", cursor="fleur", command=lambda :envia_boton("."))
boton_coma.grid(row=5, column=2)
boton_suma = Button(root, text="+", width=9, height=3, bg="blue", fg="white", cursor="fleur", command=lambda :operacion("+"))
boton_suma.grid(row=5, column=3)
boton_resta = Button(root, text="-", width=9, height=3, bg="blue", fg="white", cursor="fleur", command=lambda :operacion("-"))
boton_resta.grid(row=4, column=3)
boton_multiplicar = Button(root, text="x", width=9, height=3, bg="blue", fg="white", cursor="fleur", command=lambda :operacion("*"))
boton_multiplicar.grid(row=3, column=3)
boton_dividir = Button(root, text="/", width=9, height=3, bg="blue", fg="white", cursor="fleur", command=lambda :operacion("/"))
boton_dividir.grid(row=2, column=3)
boton_despejar = Button(root, text="Clear", bg="yellow", fg="black", width=46, height=3, cursor="fleur", command=limpiar)
boton_despejar.grid(row=6, columnspan=4)
root.mainloop()