# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 16:49:22 2023

@author: Nicole
"""


#librería
import streamlit as st
from PIL import Image
from Levenshtein import ratio
############ Programando las unidades en quechua #####################

## Las unidades en quechua son independientes. Solo están sometidas a una regla fonológica: si es que esta unidad termina en vocal, se le debe añadir el sufijo -yuq; pero, si termina en consonante, se le debe de añadir -ni y, luego, -yuq. 

## Es por esta razón que, primero, vamos a definir un diccionario para guardar todas las unidades; luego, vamos a crear una función que opere con if y else para condicionar, de acuerdo a si la palabra termina en vocal o consonante,qué sufijos adicionamos. 

## Primero, definimos un diccionario:
D = {0:'', 1:'huk', 2:'iskay', 3:'kimsa', 4:'tawa', 5:'pichqa', 6:'suqta', 7:'qanchis', 8:'pusaq', 9:'isqun', 10:'chunka'}

## Luego, creamos una función con la condición if else para la sufijación: 

## input: string p (el input es el string p, genérico)

def sufijo(p):
    ## Con el [-1] rastreamos si el caracter final del string se  
    ## encuentra en el conjunto de las vocales
    if p[-1] in 'aeiou':
  ## Si el string p termina en vocal, se le sufija -yuq 
        p = p + '-yuq'
    ## Si es no que pertenece al conjunto de las vocales, es una  
    ## consonante, por lo que se sufija -ni + -yuq
    else:
        p = p + '-ni-yuq'
    return p

############## Programando las decenas en quechua #####################

### Las decenas son dependientes; es decir, son el resultado de la adición de una palabra independiente de unidad más la palabra correspondiente a diez(chunka).

############ 10 -19 ##################

## Creamos una función con la condición if / else para rastrear si el número es menor o igual a 10. Si es que mayor a diez, se le agrega chunka. 
## que recibe un entero entre 1 y 99, y entrega su versión en palabras

## input: entero n entre 1 y 99
def quechua(n):
    ## si el número es menor o igual a 10
    if n <= 10:
        ## el output será uno de los elementos del diccionario
        s = D[n]
    ## si el número es mayor a 10
    else:
        s = 'chunka'
      
        ## extraemos la decena y la unidad
        ## extracción del primer dígito
        decena = n//10
        ## extracción del segundo dígito
        unidad = n%10
        
        ## el número es "chunka" más la unidad
        s = s + ' ' + D[unidad]
        
        ## si la decena es mayor a 1
        if decena > 1:
            ## el número será la decena extraída más "chunka"
            s = D[decena] + ' ' + s
            
        ## si la unidad es diferente de 0
        if unidad != 0:
            ## utilizamos la función sufijo(s)
            s = sufijo(s)
    return s

###### Extraemos la centena ####

    
def centena (c):
    ## si el número es menor o igual a 99
    if c <= 99:
        ## usamos la función quechua(c)
        s = quechua(c)
        return s
    ## si el número es mayor a 99
    else:
        ## extracción de la centena
        centena = c // 100
        ## extracción del resto
        resto = c % 100
        s = 'pachak'
        ## si la centena es mayor a 1
        if centena > 1:
            ## el número es la centena extraída más "pachak"
            s = D[centena] + ' ' + s
        
        ## el número será "pachak" más la función quechua(n) sobre el resto extraído
        s = s + ' ' + quechua(resto)
        
        ## verificamos el sufijo
        ## extracción del primer dígito
        decena = resto//10
        ## extracción del segundo dígito
        unidad = resto%10
        ## si la unidad es diferente de 0
        if decena ==0 and unidad != 0:
            ## utilizamos la función sufijo(s)
            s = sufijo(s)
    return s

c = 326
s = centena(c)
print(s)    
    
DM = {0:'', 1:'kiñe', 2:'epu', 3:'küla', 4:'meli', 5:'kechu', 6:'kayu', 7:'regle', 8:'pura', 9:'aylla', 10:'mari', 20:"epu mari", 30:"küla mari", 40:"meli mari", 50:"kechu mari", 60:"kayu mari", 70:"regle mari", 80:'pura mari', 90:'aylla mari', 100: "pataka", 200: "epu pataka", 300: "küla pataka", 400 : "meli pataka", 500:  "kechu pataka", 600: "kayu pataka", 700:  "reqle pataka", 800: "pura", 900: "aylla"}

def mapudungun(n):
    if n in DM:
        return DM[n]

    else:
        unidad = n % 10
        decena = (n // 10) % 10
        ## con esto extraemos la centena :)
        centena = (n // 100) 
        
        ########################
        ## decenas y unidades ##
        ########################
        
        ## si la decena es mayor a uno, 11 es mari kiñe, no kiñe mari kiñe
        ## partimos de una decena string vacío, porque puede ser 0
        d = ""
        
        if decena > 1:
            d = d + DM[decena] + " " + "mari"
        if decena == 1:
            d = d + "mari"
            
        ## unidad
        u = DM[unidad]

        ## juntamos decena y unidad
        s = d + " " + u
        
        ##############
        ## centenas ##
        ##############
        
        if centena > 1: 
            s = DM[centena] + " " + "pataka" + " " + s
        if centena == 1: 
            s = "pataka" + " " + s

        return s
#título
st.title("Números en quechua y mapudungun")

#Descripción de las lenguas
st.write("🐾 Por un lado, las unidades en quechua son independientes. Solo están sometidas a una regla fonológica: si es que esta unidad termina en vocal, se le debe añadir el sufijo -yuq; pero, si termina en consonante, se le debe de añadir -ni y, luego, -yuq. Para la formación de decenas, el número va acompañado de la palabra chunka (10), excepto 1, y la unidad atraviesa la ley fonológica. Para la formación de centenas, el número va acompañado de pachak (100), excepto 1, y se añade lo hecho para las centenas y decenas.")
st.write("🐾 Por otro lado, los números en mapudungun se forman de manera similar, solo que sin la presencia de una regla fonológica, como en quechua. Las unidades son independientes. Pero si queremos formar decenas, usamos la palabra mari. Cuando colocamos una unidad después de la palabra mari esta se suma, por ejemplo, mari kiñe = 10+1. En contraste, si colocamos la unidad antes de mari esta se multiplica, por ejemplo, epu mari kiñe= (2x10)+1 = 21. Lo mismo ocurre con las centenas, solo que ahí se utiliza pataka: epu pataka meli mari kiñe = (2 x 100) + (4x 10) + 1 = 241.")

## librería

i = Image.open('tamipa.jpg')
st.image(i)

## opciones
options = st.multiselect(
    'Elige una o dos lenguas!',
    ['Quechua', 'Mapudungun'])


#opción 2
n_input = st.slider("Elija un número entre 1 y 999 👇", 1, 999, 1)
if "Quechua" in options:

    st.write("El número" + " " + str(n_input) + " " + "en quechua se escribe" + " " + centena(n_input))

if "Mapudungun" in options:
    st.write("El número" + " " + str(n_input) + " " + "en mapudungun se escribe" + " " + mapudungun(n_input))


#Programando la búsqueda de las distancias emtre string 


Dm={}
Dq={}

#Creando un ciclo for 
#número= string
for i in range (1,999):
    Dm [i]= mapudungun (i)
    Dq [i]= centena (i)
    


## Invertimos el diccionario QUECHUA 
inv_Dq= {v: k for k, v in Dq.items()}

## Invertimos el diccionario MAPUDUNGUN
inv_Dm = {v: k for k, v in Dm.items()}


# calculando el porcentaje de similitud

def distancia_quechua(s):
   sq = {}
   for n in inv_Dq.keys():
       sq[n]= ratio(s,n)
   k= max(sq,key=sq.get) ##entrega la máxima similitud
   return inv_Dq[k]

v = st.text_input("🐾Escriba aquí un número en palabras en quechua")

st.write(distancia_quechua(v))
      
def distancia_mapudungun(s):
    sm = {}
    for n in inv_Dm.keys():
        sm[n]= ratio(s,n)
    k= max(sm,key=sm.get) ##entrega la máxima similitud
    return inv_Dm[k]
   
k = st.text_input("🐾Escriba aquí un número en palabras en mapudungun")

st.write(distancia_mapudungun (k))  

#imagen 2
e = Image.open('animalitos.jpg')
st.image(e)
        
    
   