print("digite um número")
num1=int(input())
print("digite outro número")
num2=int(input())
print("digite outro número")
num3=int(input())
print("digite outro número")
num4=int(input())

media=(num1+num2+num3+num4)/4
print(f"A média aritmética é:{media }")

print("Números menores que a média:")

if num1<media and num2<media and num3<media and num4<media:
  print(f"{num1}")
  print(f"{num2}")
  print(f"{num3}")
  print(f"{num4}")
elif num1>media and num2<media and num3<media and num4<media:
  print(f"{num2}")
  print(f"{num3}")
  print(f"{num4}")
elif num1>media and num2>media and num3<media and num4<media:
  print(f"{num3}")
  print(f"{num4}")
elif num1>media and num2>media and num3>media and num4<media:
 print(f"{num4}")

print("Números maiores ou igual a média:")
if num1>=media and num2>=media and num3>=media and num4>=media:
  print(f"{num1}")
  print(f"{num2}")
  print(f"{num3}")
  print(f"{num4}")
  if num1<media and num2>=media and num3>=media and num4>=media:
    print(f"{num2}")
    print(f"{num3}")
    print(f"{num4}")
  if num1<media and num2<media and num3>=media and num4>=media:
    print(f"{num3}")
    print(f"{num4}")
    if num1<media and num2<media and num3>media and num4>=media:
        print(f"{num4}")
