"""
def say_hello( name):
    print("Hello " + name) 

def ask_name():
   return  input("¿Cuál es tu nombre? ")

username = ask_name()

say_hello(username)
"""

#definir una función que pregunte un sujeto
def ask_subject():
   return input("Escribe un sujeto ")

#definir una funcion que pregunte un verbo
def ask_action():
   return input("Escribe un verbo ")

#definir una función que pregunte un adjetivo
def ask_adjetive():
   return input("Escribe un adjetivo ")

#definir una función que haga una oración
def build_phrase(subject, verb, adjetive):
    return print("El / La " + subject + " " + verb + " " + adjetive)

def play():
   subject = ask_subject()
   verb = ask_action()
   adjetive = ask_adjetive()
   build_phrase(subject, verb, adjetive)
   
play()