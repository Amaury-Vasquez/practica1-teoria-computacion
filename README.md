# Creador de AFD's

El objetivo de este programa es recibir un archivo de texto que incluya la tabla
de transicion de estados de un automata finito determinista para despues crear
un automata que reciba una entrada y evalue si la cadena es aceptada por el automata

## Ingreso de datos

En la primera linea se leen las diferentes entradas que puede recibir el automata, en caso
de ser un automata no determinista se espera que la entrada al final sea 'ε'.
En la segunda linea se leen los estados donde el automata se encuentra en un estado de aceptacion, siempre
dado por valores numericos.
En las siguientes lineas se leen el estado donde se encuentra, y las transiciones que se realizarian
para cada estado, en ese orden, imaginemos el AFD que recibe todas las cadenas que contienen un 1 o un 0,
la tabla de transicion seria la siguiente:

<center>

| Estado | 1   | 0   |
| ------ | --- | --- |
| q0     | q1  | q1  |
| q1     | q1  | q1  |

</center>

Para este AFD, el archivo que define la tabla de transicion deberia de ser como el de este ejemplo:

```
  1 0 // Abecedario del AFD
  0 1 1 // Estado inicial // Transicion // Transicion
  1 1 1 // Estado inicial // Transicion // Transicion
```
