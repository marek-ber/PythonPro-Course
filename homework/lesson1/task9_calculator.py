num1 = int(input("Podaj pierwszą liczbę: "))
num2 = int(input("Podaj drugą liczbę: "))

operation = input("Podaj działanie: (+, -, *, /): ")

if operation == "+":
  result = num1 + num2
  print("Wynik: ", result)
 
elif operation == "-":
   result = num1 - num2
   print("Wynik: ", result)
   
elif operation == "*":
    result = num1 * num2
    print("Wynik: ", result)
    
elif operation == "/":
   if num2 != 0:
      
      result = num1 / num2
      print("Wynik: ", result)
   else:
       print("Nie można dzielić przez 0")