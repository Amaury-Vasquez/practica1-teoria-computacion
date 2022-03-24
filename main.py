def print_lines(lines):
  count = 0
  for line in lines:
    print(f'[{count}] : {line}')
    count += 1
    
def read_file():
  lines = []
  with open('automata1.txt') as file:
    lines = file.readlines()
  return lines

if __name__ == '__main__':
  lines = read_file()
  first_line = lines[0].split()
  print_lines(first_line)