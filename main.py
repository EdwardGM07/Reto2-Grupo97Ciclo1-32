"""
 Edward Camilo Gonzalez Monje, 
edwardcamilo2020@gmail.com 
Grupo 97 - ciclo 1,
"""

#======================Funcion 1==================================
def generar_correo(nombre, apellido, ano_nacimiento, opcion):
  #Funcion que genera usuarios de correo dependiendo de 3 opciones

    nuevo_correo = str
    alfanumerico = False
    #Variables inicializadas

    for i in (nombre, apellido, ano_nacimiento):
      #recorre 3 variables caracter por caracter
      if i.isalnum() == True:
          #comprueba si la variable tiene caracter alfanumericos
            alfanumerico = True      
      else:
      #si hay almenos una que no es alfanumerico envía error
        nuevo_correo = "error"
    

    if opcion > 0 and opcion < 4 and alfanumerico == True:
      #restriccion de solo 3 opciones para crear el usuario de correo y si nombre, apellido y ano_nacimiento es alfanumerico
        if opcion == 1:
          #opcion donde es la primera letra del nombre, la primera letra del apellido y el @ de la compañia
            nuevo_correo = nombre[0:1]
            nuevo_correo = nuevo_correo + apellido[0:1]
            nuevo_correo = nuevo_correo + "@misiontic.com"
        elif opcion == 2:
          #opcion donde es las tres primeras letras del nombre, las dos primeras letras del apellido y el @ de la compañia
            nuevo_correo = nombre[0:3]
            nuevo_correo = nuevo_correo + apellido[0:2]
            nuevo_correo = nuevo_correo + "@misiontic.com"
        elif opcion == 3:
          #opcion donde es las tres primeras letras del nombre,un punto, las dos ultimas letras del apellido, un punto y el @ de la compañia
            nuevo_correo = nombre[0:3]
            nuevo_correo = nuevo_correo + apellido[-2:]
            nuevo_correo = nuevo_correo + ano_nacimiento
            nuevo_correo = nuevo_correo + "@misiontic.com"
    else:
      #es error si no elige una opcion de 1 a 3
        nuevo_correo = "error"

    return nuevo_correo.lower()
    #convierte todo el correo en minusculas 

#==================================================================

#ejemplo de como correr la funcion 
result= generar_correo("juan","tamayo","19", 1) 

# ejemplo para imprimir lo que la funcion me retorna
print(result) 






