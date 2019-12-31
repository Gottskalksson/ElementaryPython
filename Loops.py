for i in range(5):
    print(i+1)

a=3
b=10

while a<b:
    b = b+a
    a=a*2+2
    print(a)
    print(b)

password = "xxx"
while password != "asdf":
    password = input("Podaj hasło: ")

print("Zalogowano!")
