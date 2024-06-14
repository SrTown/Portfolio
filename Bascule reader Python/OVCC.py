import sys
import subprocess
libraries = ['tkinter', 'pyautogui', 'keyboard', 'serial', 'threading']

for library in libraries:
    try:
        __import__(library)
        print(f"Library {library} already installed.")
    except ImportError:
        print(f"Library {library} not installed yet. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", library])
        print(f"Library {library} installed succesfully.")

import tkinter as tk
import pyautogui
import keyboard
import serial
import threading
import time


puerto_com = 'COM4'
puerto_com2 = 'COM3'
error=""
datos = []
datos2 = []
p=""
p2=""

def retry_on_unbound_local_error(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except UnboundLocalError:
                error="UnboundLocalError detected. Retrying..."
                print(error)
            except serial.serialutil.SerialException:
                error="Ports error, please check the ports."
                print(error)
            
            except UnicodeDecodeError:
                error="Error of errors, please check the ports."
                print(error)
            etiqueta.config(text=error)
    return wrapper

@retry_on_unbound_local_error
def leer_puerto_com():
    global datos
    global datos2
    global p
    global p2
    puerto = serial.Serial(puerto_com, baudrate=9600)
    puerto2= serial.Serial(puerto_com2, baudrate=9600)
    while True:
        byte_dato = puerto.read(1)
        byte_dato2 = puerto2.read(1)

        if byte_dato:
            dato = byte_dato.decode('utf-8')
            datos.insert(0, dato)
            
        if byte_dato2:
            dato2 = byte_dato2.decode('utf-8')
            datos2.insert(0, dato2)
        if dato == '=':
            del datos[0]
            p = "".join(datos)
            boton1.config(text="Bascula 1: "+p+" Kg")
            print(p)
            datos = []

        if dato2 == '=':
            del datos2[0]
            p2 = "".join(datos2)
            boton2.config(text="Bascula 2: "+p2+" Kg")
            print(p2)
            datos2 = []
            
        error=" "
        etiqueta.config(text=error)


def escribir_texto(event=None):
    global datos
    global p
    texto_leido = "".join(datos)
    pyautogui.typewrite(p)
    pyautogui.press('tab')
    time.sleep(0.1)

def escribir_texto2(event=None):
    global datos2
    global p2
    texto_leido2 = "".join(datos2)
    pyautogui.typewrite(p2)
    pyautogui.press('tab')
    time.sleep(0.1)

# Crear y configurar la ventana principal
ventana = tk.Tk()
ventana.title("Programa Basculas")
ventana.geometry("520x70")
ventana.attributes("-topmost", True)
boton1 = tk.Button(ventana, text="", font=("DS-Digital", 20), bg="black", fg="#52FF27", relief="raised", borderwidth=5,
                   highlightthickness=0, highlightbackground="#FFF", highlightcolor="#FFF",
                   padx=10, compound=tk.CENTER)


boton2 = tk.Button(ventana, text="", font=("DS-Digital", 20), bg="black", fg="#52FF27", relief="raised", borderwidth=5,
                   highlightthickness=0, highlightbackground="#FFF", highlightcolor="#FFF",
                   padx=10, compound=tk.CENTER)
boton1.grid(row=0, column=0)
boton2.grid(row=0, column=1)
etiqueta = tk.Label(ventana,text="")
etiqueta.grid(row=1, column=0, columnspan=2)

keyboard.add_hotkey('f4', escribir_texto)
keyboard.add_hotkey('f9', escribir_texto2)

hilo_puerto_com = threading.Thread(target=leer_puerto_com, daemon=True)
hilo_puerto_com.start()

ventana.mainloop()

