def get_accept_states(line):
  return [int(x) for x in line.split()]

def get_transitions(arr, start):
  transitions = []
  for i in range(start, len(arr)):
    transitions.append([int(x) for x in arr[i].split()])
  return transitions

def print_lines(lines):
  count = 0
  for line in lines:
    print(f'[{count}] : {line}')
    count += 1
    
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
  print(alphabet, accept_states, transitions, '\n')
  # Algoritmo
  ## Lanza una excepcion en caso de que la cadena no sea valida
  try:
    current_state = 0
    for element in string:
      index = alphabet.index(element)
      current_state = transitions[current_state][index]
      print(index, current_state)
  except:
    print("La cadena ingresada no esta incluida en el abecedario")
    return False
  return current_state in accept_states
  
  
if __name__ == '__main__':
  # Se espera que la tabla de transicion tenga el formato especificado
  file_name = input("Ingresa nombre del archivo que contiene la tabla de transicion: ")
  string = input("Ingrese cadena a evaluar: ")
  print(eval_string(file_name, string))  