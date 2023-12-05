

def obtener_credenciales():
    acces_key = input("Ingresa tu access Key de AWS")
    secret_key = input("Ingresa tu secret Key de AWS")
    return acces_key, secret_key


if __name__ == "__main__":  #EL name VAlida el nombre del archivo principal y lo inicia como main
    print ("Hola! soy tu bot y el dia de hoy te voy a aydar a desplegar infraestructura en AWS")

#Invocando la funcion
acces_key, secret_key = obtener_credenciales()


