def funcion_externa(x):
    def funcion_interna(y):
        return y + 1
    return funcion_interna(x) * 2

uno = funcion_externa(0)
dos = uno(2)
print(dos)
print(type(uno))