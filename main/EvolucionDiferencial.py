#     @author: Esdras Victoria

import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

mu = 0.5 #Factor de Escala
cr = 0.5 #Tasa de recombinacion

#Funcion para obtener el peso con ciertos parametros con la formula peso = x^2 + y^3 + z^4
      #@param x,y,z
def obtenerPeso(x, y, z):
    peso = pow(x, 2) + pow(y, 3) + pow(z, 4)
    return peso

#Se Generan 3 valores aleatorios entre [1:10]
def generarTrios(): 
    x = random.randint(1,10)
    y = random.randint(1,10)
    z = random.randint(1,10)
    return (x, y, z)

def crearFamilia(v):
    familiaGenerada = [generarTrios() for _ in range(v)]    #Genera una lista entre [4:5] elementos con tuplas de 3 elementos (x,y,z)
    return familiaGenerada  

def calcMaxFamilias(familiaGenerada):
      result = []
      result.append("\t\tMetodo para Maximizar")
      result.append("Este metodo genera familias tomando como objetivo un valor dentro del arreglo de la familia"
          +"\ncada familia NUEVA se calcula comparando que si el peso de los valores obtenidos apartir de los v1, v2, v3" 
          +"\nes MAYOR que el peso del OBJETIVO")
    
      familiaOriginal = familiaGenerada
      length = len (familiaOriginal)

      for i in range(length):
        
            result.append(f"\n\n\t\tPara la familia No. {i}: {familiaOriginal}")
            listaSinObjetivo = familiaOriginal[:]   #Replica la lista original creado en la funcion crearFamilia()
            del listaSinObjetivo[i]     #Elimina el objetivo[i] en cada una de las iteraciones y devuleve la lista SIN objetivo

            vectorVi = random.sample(listaSinObjetivo, 3) #Selecciona de forma aleatoria 3 valores de la lista para usarlos como v1, v2, v3
            result.append(f"El vector de vI es: \n {vectorVi}"
                  +f"\n\tv1: {vectorVi[0]}"
                  +f"\n\tv2: {vectorVi[1]}"
                  +f"\n\tv3: {vectorVi[2]}")

            #Calcula los valores del nuevo elemento con la formula 
                  # wi = v1 + mu*(v2 - v3) para los elementos de wiX, wiY, wiZ
            wiX = vectorVi[0][0] + mu*(vectorVi[1][0] - vectorVi[2][0])
            result.append(f"El valor de wiX es: {wiX}")

            wiY = vectorVi[0][1] + mu*(vectorVi[1][1] - vectorVi[2][1])
            result.append(f"El valor de wiY es: {wiY}")

            wiZ = vectorVi[0][2] + mu*(vectorVi[1][2] - vectorVi[2][2])
            result.append(f"El valor de wiZ es: {wiZ}")

            #Se obtienen los pesos del valor del objetivo y el valor del nuevo elemento calculado vI
            pesoVi = obtenerPeso(wiX, wiY, wiZ)
            pesoObj = obtenerPeso(familiaOriginal[i][0], familiaOriginal[i][1], familiaOriginal[i][2])
      
            result.append(f"\nEl valor de los pesos de: \n"
                  + f"\tviX: {wiX}\n" 
                  + f"\tviY: {wiY}\n" 
                  + f"\tviZ: {wiZ}\n"
                  + f"Es de: {pesoVi}")
      
            #Verifica que el peso del nuevo elemento sea MAYOR que el de la familiaOriginal
                  #Si hay cambios la nueva generacion sustituira al objetivo con el nuevo elemento
                  #De lo contrario la familia se conserva para la siguiente generacion
            if (pesoVi > pesoObj):
                  nuevaGeneracion = familiaOriginal[:]
                  nuevaGeneracion[i] = (wiX, wiY, wiZ)

                  result.append(f"El peso del objetivo: {familiaOriginal[i]} es: {pesoObj}" 
                        +f"\nEl peso del nuevo elemento es: {pesoVi}" 
                        +f"\nDebido a que el nuevo elemento {pesoVi} es > {pesoObj}")
            
                  result.append(f"\tLa nueva generacion No. {i+1} Es: \n" 
                        +f"{nuevaGeneracion}")
      else:
            result.append(f"El peso del objetivo: {familiaOriginal[i]} es: {pesoObj}" 
                  +f"\nEl peso del nuevo elemento es: {pesoVi}" 
                  +f"\nDebido a que el nuevo elemento {pesoVi} es < {pesoObj}"
                  +f"\n\tLa familia No. {i-1} pasa igual a la generacion No. {i+1}\n"
                  +f"{familiaOriginal}")
      
      #Regresa toda la lista de mensajes como una sola cadena de texto
      return "\n".join(result)
            
def calcMinFamilias(familiaGenerada):     
      result = []
      result.append("\t\tMetodo para Minimizar")
      result.append("Este metodo genera familias tomando como objetivo un valor dentro del arreglo de la familia"
          +"\ncada familia NUEVA se calcula comparando que si el peso de los valores obtenidos apartir de los v1, v2, v3" 
          +"\nes MAYOR que el peso del OBJETIVO")
    
      familiaOriginal = familiaGenerada
      length = len (familiaOriginal)

      for i in range(length):
        
            result.append(f"\n\n\t\tPara la familia No. {i}: {familiaOriginal}")
            listaSinObjetivo = familiaOriginal[:]   #Replica la lista original creado en la funcion crearFamilia()
            del listaSinObjetivo[i]     #Elimina el objetivo[i] en cada una de las iteraciones y devuleve la lista SIN objetivo

            vectorVi = random.sample(listaSinObjetivo, 3) #Selecciona de forma aleatoria 3 valores de la lista para usarlos como v1, v2, v3
            result.append(f"El vector de vI es: \n {vectorVi}"
                  +f"\n\tv1: {vectorVi[0]}"
                  +f"\n\tv2: {vectorVi[1]}"
                  +f"\n\tv3: {vectorVi[2]}")

            #Calcula los valores del nuevo elemento con la formula 
                  # wi = v1 + mu*(v2 - v3) para los elementos de wiX, wiY, wiZ
            wiX = vectorVi[0][0] + mu*(vectorVi[1][0] - vectorVi[2][0])
            result.append(f"El valor de wiX es: {wiX}")

            wiY = vectorVi[0][1] + mu*(vectorVi[1][1] - vectorVi[2][1])
            result.append(f"El valor de wiY es: {wiY}")

            wiZ = vectorVi[0][2] + mu*(vectorVi[1][2] - vectorVi[2][2])
            result.append(f"El valor de wiZ es: {wiZ}")

            #Se obtienen los pesos del valor del objetivo y el valor del nuevo elemento calculado vI
            pesoVi = obtenerPeso(wiX, wiY, wiZ)
            pesoObj = obtenerPeso(familiaOriginal[i][0], familiaOriginal[i][1], familiaOriginal[i][2])
      
            result.append(f"\nEl valor de los pesos de: \n"
                  + f"\tviX: {wiX}\n" 
                  + f"\tviY: {wiY}\n" 
                  + f"\tviZ: {wiZ}\n"
                  + f"Es de: {pesoVi}")
      
            #Verifica que el peso del nuevo elemento sea MENOR que el de la familiaOriginal
                  #Si hay cambios la nueva generacion sustituira al objetivo con el nuevo elemento
                  #De lo contrario la familia se conserva para la siguiente generacion
            if (pesoVi < pesoObj):
                  nuevaGeneracion = familiaOriginal[:]
                  nuevaGeneracion[i] = (wiX, wiY, wiZ)

                  result.append(f"El peso del objetivo: {familiaOriginal[i]} es: {pesoObj}" 
                        +f"\nEl peso del nuevo elemento es: {pesoVi}" 
                        +f"\nDebido a que el nuevo elemento {pesoVi} es < {pesoObj}")
            
                  result.append(f"\tLa nueva generacion No. {i+1} Es: \n" 
                        +f"{nuevaGeneracion}")
      else:
            result.append(f"El peso del objetivo: {familiaOriginal[i]} es: {pesoObj}" 
                  +f"\nEl peso del nuevo elemento es: {pesoVi}" 
                  +f"\nDebido a que el nuevo elemento {pesoVi} es > {pesoObj}"
                  +f"\n\tLa familia No. {i-1} pasa igual a la generacion No. {i+1}\n"
                  +f"{familiaOriginal}")
            
      #Regresa toda la lista de mensajes como una sola cadena de texto
      return "\n".join(result)
      

#Establecemos la accion del Boton "Calcular"
def calcular():
      tamanoFamilia = noDeElementos.get()
      if not tamanoFamilia:
            messagebox.showerror("FatalError", "Por favor introduce un valor dentro del cuadro de texto")
      else:
            tamanoFamilia = int(noDeElementos.get())
            if(tamanoFamilia !=4 and tamanoFamilia !=5):
                  messagebox.showerror("Error", "Por favor introduce un valor que sea valido: 4 o 5")
            else:
                  familiaGenerada = crearFamilia(tamanoFamilia)
                  listaFamilia = f"La familia original generada es: {familiaGenerada}"
                  
                  mostrarFamilia.config(state="normal")
                  mostrarFamilia.delete(1.0, tk.END)
                  mostrarFamilia.insert(tk.END, listaFamilia)
                  mostrarFamilia.config(state="disabled")

                  #Definimos los hilos y los iniciamos para cada una de las funciones     
                        #calcMaxFamilias & calcMinFamiias
                  hilo_1 = threading.Thread(target=calcMaxFamilias(familiaGenerada))
                  hilo_2 = threading.Thread(target=calcMinFamilias(familiaGenerada))
                  hilo_1.start
                  hilo_2.start

                  #Anade la lista de mensajes que se ha generado en la funcion calcMaxFamilias
                  ##resultMax = calcMaxFamilias(familiaGenerada)
                  resultMax = calcMaxFamilias(familiaGenerada)
                  resultCalcMax.config(state="normal")
                  resultCalcMax.delete(1.0, tk.END)
                  resultCalcMax.insert(tk.END, resultMax)
                  resultCalcMax.config(state="disabled")

                  #Anade la lista de mensajes que se ha generado en la funcion calcMinFamilias
                  ##resultMin = calcMinFamilias(familiaGenerada)
                  resultMin = calcMinFamilias(familiaGenerada)
                  resultCalcMin.config(state="normal")
                  resultCalcMin.delete(1.0, tk.END)
                  resultCalcMin.insert(tk.END, resultMin)
                  resultCalcMin.config(state="disabled")

                

#Establecemos la accion del Boton "Limpiar"
def limpiar():
      resultCalcMax.config(state="normal")
      resultCalcMax.delete(1.0, tk.END)
      resultCalcMax.config(state="disabled")

      resultCalcMin.config(state="normal")
      resultCalcMin.delete(1.0, tk.END)
      resultCalcMin.config(state="disabled")

      mostrarFamilia.config(state="normal")
      mostrarFamilia.delete(1.0, tk.END)
      mostrarFamilia.insert(tk.END, "Aqui se mostrara la familia que se ha generado aleatoriamente")
      mostrarFamilia.config(state="disabled")

#Definimos los elementos de la ventana 
ventana = tk.Tk()
ventanaStyle = ttk.Style()
ventanaStyle.theme_use("clam")
ventana.title("Programa de Evolucion Diferencial")
ventana.geometry("1350x700")

frame1 = tk.Frame(ventana)
frame2 = tk.Frame(ventana)
frame3 = tk.Frame(ventana)

frame1.pack(side = "top")
frame2.pack()
frame3.pack(side = "bottom")

#Anadimos los elementos dentro del "Frame1"
#Crear las etiquetas y cuadros de texto
elementosLabel = tk.Label(frame1, text="Dame un valor que sea 4 o 5: ")
elementosLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

noDeElementos = tk.Entry(frame1, width=30)
noDeElementos.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


#Crear los dos botones y los anadimos al Frame1
btnCalcular = tk.Button(frame1, text = "Calcular", command=calcular)
btnCalcular.grid(row=2, column=0, padx=2, pady= 5)
btnLimpiar = tk.Button(frame1, text = "Limpiar", command=limpiar)
btnLimpiar.grid(row=2, column=1, padx=2, pady=5)

#Creamos un Area de Texto que mostrara el vector generado
mostrarFamilia = tk.Text(frame2, height=1, width=90)
mostrarFamilia.insert(tk.END, "Aqui se mostrara la familia que se ha generado aleatoriamente")
mostrarFamilia.grid(row=3, column=0, padx=5, pady=5, columnspan=2)
mostrarFamilia.config(state="disabled")

#Anadimos los elementos dentro del FrameInterior contenido en el Canva
#Crear las areas de Texto
resultCalcMax = tk.Text(frame3, state="disabled", height=32)
resultCalcMax.grid(row=0, column=0, padx=10, pady=10)

resultCalcMin = tk.Text(frame3, state="disabled", height=32)
resultCalcMin.grid(row=0, column=1, padx=10, pady=10)


#Iniciamos la ventana
ventana.mainloop()

