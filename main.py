import sys

def get_accept_states(line):
  return [int(x) for x in line.split()]

def get_transitions(arr, start):
  transitions = []
  for i in range(start, len(arr)):
    transitions.append([int(x) for x in arr[i].split()])
  return transitions
    
def read_file(file_name):
  lines = []
  with open(file_name) as file:
    lines = file.readlines()
  return lines

def eval_string(file_name, string):
  # Inicializacion de variables a ocupar
  lines = read_file(file_name)
  alphabet = lines[0].split()
  accept_states = get_accept_states(lines[1])
  transitions = get_transitions(lines, 2)
  # Algoritmo
  ## Lanza una excepcion en caso de que la cadena no sea valida
  try:
    current_state = 0
    for element in string:
      index = alphabet.index(element)
      current_state = transitions[current_state][index]
  except:
    print("\nLa cadena ingresada no esta incluida en el abecedario!\n")
    quit()
  
  return current_state in accept_states
  
  
if __name__ == '__main__':
  # Se espera que la tabla de transicion tenga el formato especificado
  if(len(sys.argv) != 2):
    print('Se esperaba un argumento (nombre del archivo), terminando')
    quit()
  file_name = sys.argv[1]
  string = input("Ingrese cadena a evaluar: ")
  if(eval_string(file_name, string)):
    print(f'\n{string} ES una expresion regular aceptada por el automata\n')
  else:
    print(f'\n{string} NO ES una expresion regular aceptada por el automata\n')  