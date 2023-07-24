def sumex(a: int, b: int, c: int) -> int:
    return a + b + c

print(sumex(1,2,3))

def mathematic():
    if sumex(0,0,0) == False:
        print("zero")

print(mathematic())

def imprimit(nombre: str) -> str:
    return nombre.upper() + " " + nombre.lower()

print(imprimit("hello"))