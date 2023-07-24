def hola(x: str)->str:
    return f"hola {x}go."

print(hola("Die"))

x = "javier"
print((lambda x: f"hola {x}.")(x))

a = "Diego"
b = "Javier"
c = "Cambiaso"
d = "Sánchez"

print((lambda a, b, c, d: f"{a} {b} {c} {d}")(a,b,c,d))
print((lambda a, b, c, d: a == "Diego")(a,b,c,d))

remainder = lambda num: num % 2 
print(remainder(5))
print(remainder(8))