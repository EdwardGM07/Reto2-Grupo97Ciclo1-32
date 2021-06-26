# Identificar
a)	¿Cuál es el problema?
Se necesita un generador de correos.
b)	¿Quiénes son los interesados?
El jefe de sistemas de la misión tic.
c)	¿Cuál es el objetivo?
Construir un correo dependiendo de la opción que se elija. 
d)	¿Existen restricciones?
Nombre, Apellido y año de nacimiento debe tener solamente caracteres alfanuméricos.
La opción debe ser un valor
entre 1 y 3, (Incluidos).
# Definir
a)	¿Qué conozco?
Nombre, Apellido, año de nacimiento y la opción elegida por el jefe de sistemas.

b)	¿Qué debo conocer?
Las condiciones para realizar la funcion debe dar 3 opciones para crear el correo.
c)	¿Dividir el problema en subproblemas?
1. Solicitar Nombre, Apellido, Año de nacimiento y opcion.
2. Crear el correo segun la opción elegida por el jefe de sistemas.
3. Imprimir el correo creado.
# Estrategia
a)	Ejemplos particulares 
--Requisito 1--
Nombre: Edward 
Apellido: Gonzalez
Año de Nacimiento: 1999
Opcion:
1. debe retornar eg@misiontic.com.
2. debe retornar edwca@misiontic.com.
3. debe retornar edwez1999@misiontic.com.

# Algoritmo
a)	Escribir algoritmo para cada requisito
--Requisito 1--
Entrada: nombre, apellido, ano_nacimiento y opción.
Proceso: Evaluar con condicionales segun la opcion.
Salida: nuevo_correo.

# Logro --> Programa