'''
      Christopher Morales - 23003861
      Josué Martínez - 23003956
'''

# CONSTANTES
validOperations = ['+', '-', '*', '/', 'sqroot', 'sqr', 'sen', 'cos', 'tan', 'div', '%', 'factorial!']
letters = [range(65, 91), range(95, 123)]

# SUBRUTINAS
def isNumber( expression ):
      is_number = True
      for operation in validOperations:
            if operation in expression:
                  is_number = False
                  break
      return is_number

# TEXTO A NUMERO
def strToNumber(expression):
      try:
            print(f"'{expression}'")
            num = 0
            for index in expression:
                  if index == ".":
                        num = float(expression)
                        break
            if num == 0:
                  num = int(expression)
            return num
      except ValueError:
            print(expression)
            return 0

# CALCULA LA OPERACION
def calculate(expression):
      # expression: string
      result = 0
      if '(' in expression and ')' in expression:
            expression = expression[1:]
            expression = expression[:-1]
      space1 = expression.find(" ")
      space2 = expression[space1:].find(" ") + (space1 + 2)
      # num1 = strToNumber(expression[:space1 + 1])
      # num2 = strToNumber(expression[space2 + 1:])
      sign = expression[space1 + 1]
      #print(num1)
      # print(num2)
      # print(sign)
      
      # Evaluate and execute operacion
      match sign:
            case '+':
                  sign = expression.find('+')
                  num1 = expression[:sign]
                  num2 = expression[sign + 2:]
                  print(num1, num2)
                  result = num1 + num2
            case '-':
                  result = num1 - num2
            case '*':
                  result = num1 * num2
            case '/':
                  result = num1 / num2

      return result

# FUNCION MAIN
def main():
      exit = False
      while(not exit):
            option = input("Calculadora >> ")
            if option == "q" or option == "quit":
                  print("Saliendo ...\nGracias por usar nuestra calculadora.")
                  exit = True
                  break
            else:
                  answer = str(0)
                  if '(' in option and ')' in option:
                        operation = option[1:]
                        operation = operation[:-1]
                        answer = calculate(operation)
                        # print(operation)
                  else:
                        if isNumber(option):
                              try:
                                    answer = strToNumber(option)
                              except ValueError:
                                    answer = "ERROR! Expresion no válida"
                        else:
                              answer = "ERROR! Expresion no válida"
                  print("respuesta >>", answer)

if __name__ == "__main__":
      main()