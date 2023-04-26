'''
      Christopher Morales Acuña - 23003861
      Mario Josué Martínez Olivares - 23003956
'''
from math import sqrt, radians, pi, sin, cos, tan

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
            #print(f"'{expression}'")
            num = 0
            for index in expression:
                  if index == ".":
                        num = float(expression)
                        break
            if num == 0:
                  num = int(expression)
            return num
      except ValueError:
            expression = expression[1: -1]
            return calculate(expression)
      
def evaluateOperation(operationSign, num1, num2):
      result = 0

      match operationSign:
                  case '+':
                        result = num1 + num2
                  case '-':
                        result = num1 - num2
                  case '*':
                        result = num1 * num2
                  case '/':
                        result = num1 / num2
                  # TODO: Pending 8 valid operations

      return result

# CALCULA LA OPERACION
def calculate(expression):
      # expression: string
      result = 0
      if '(' in expression and ')' in expression:
            startNewExpression = expression.find("(")
            endNewExpression = expression[startNewExpression:].find(")") + (startNewExpression)
            newExpression = expression[startNewExpression + 1:endNewExpression]
            if startNewExpression == 0:
                  num1 = calculate(newExpression)
                  num2 = strToNumber(expression[endNewExpression + 4:])
                  sign = expression[endNewExpression + 2: endNewExpression + 3]
            else:
                  num1 = strToNumber(expression[:startNewExpression - 2])
                  num2 = calculate(newExpression)
                  sign = expression[startNewExpression - 2: startNewExpression - 1]
            result = evaluateOperation(sign, num1, num2)
      elif validOperations[4] in expression:
            # sqroot
            pos = expression.find(validOperations[4])
            num = strToNumber(expression[pos + 7:])
            result = sqrt(num)
      elif validOperations[5] in expression:
            # sqr
            pos = expression.find(validOperations[5])
            num = strToNumber(expression[pos + 4:])
            result = pow(num, 2)
      elif validOperations[6] in expression:
            # sen
            pos = expression.find(validOperations[6])
            num = strToNumber(expression[pos + 4:])
            result = sin(radians(num))
      elif validOperations[7] in expression:
            # cos
            pos = expression.find(validOperations[7])
            num = round(radians(strToNumber(expression[pos + 4:])), 2)
            result = round(cos(num), 6)
      elif validOperations[8] in expression:
            # tan
            pos = expression.find(validOperations[8])
            num = round(radians(strToNumber(expression[pos + 4:])), 2)
            result = round(tan(num), 6)
      elif validOperations[9] in expression:
            # div
            space1 = expression.find(" ")
            space2 = expression[space1:].find(" ") + (space1 + 2)
            num1 = strToNumber(expression[:space1 + 1])
            num2 = strToNumber(expression[space2 + 1:])
            sign = '/'
            result = evaluateOperation(sign, num1, num2)
      else:
            space1 = expression.find(" ")
            space2 = expression[space1:].find(" ") + (space1 + 2)
            num1 = strToNumber(expression[:space1 + 1])
            num2 = strToNumber(expression[space2 + 1:])
            sign = expression[space1 + 1]
            
            # Evaluate and execute operacion
            result = evaluateOperation(sign, num1, num2)

      return result

# FUNCION MAIN
def main():
      exit = False
      while(not exit):
            option = input("Calculadora >> ")
            if option == "q" or option == "Q" or option == "quit":
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