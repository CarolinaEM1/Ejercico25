# Pasar de dolares a pesos y viceversa



def pesos_dolares(pesos):
    return pesos*0.58

def dolares_pesos(dolares):
     return dolares*17.13

while True:
    print("""\t.:MENÚ:.
    1.- Pesos a dolares
    2.- Dolares a pesos
    3.- Salir
    """)

    opcion = int(input("Digite una opcion: "))

    print()

    if opcion == 1:
        pesos = float(input("Digite los pesos a convertir -> "))
        print(f"La conversión de pesos a dólares es ${pesos_dolares(pesos):.2f}")
    elif opcion == 2:
        dolares = float(input("Digite los dolares a convertir -> "))
        print(f"La conversión de dólares a pesos es ${dolares_pesos(dolares):.2f}")
    elif opcion == 3:
        break
    else:
        print("La opcion no es correcta, digite otra dentro del menú ")


# Carolina EM



