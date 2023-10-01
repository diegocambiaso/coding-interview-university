# la funcion_externa retorna la funcion_interna

print("Parte 2")
print("-"*20)

def funcion_externa():
    print("Codigo de la funcion externa")

    def funcion_interna():
        print("Código de la funcion_interna")
    
    return funcion_interna

funcion_externa()

mi_funcion = funcion_externa()

print("mi_funcion:", mi_funcion())
