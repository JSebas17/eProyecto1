def saludo(nombre: str) -> str:
    return f"Hola, {nombre} !Biewnvenido a Git, guapo¡"

if __name__ == "__main__":
    nombre =  input("¿Tu nombre?")
    print(saludo(nombre))
