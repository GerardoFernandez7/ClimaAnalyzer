# Importar modulos
import weaFunc as f

# Declarar variables
seguir_en_programa = True

# Menú principal
while seguir_en_programa:
    print("")
    print("---> BIENVENIDO <---")
    print("Que desea hacer?")
    print("1. Ver el promedio de la temperatura de un mes")
    print("2. Ver el total de precipitación de un mes")
    print("3. Ver el día en que hubo mayor velocidad de viento")
    print("4. Crear base de datos en un rango de 2 fechas")
    print("5. Salir")
    print("")
    
    opcion = input("Seleccione una opción válida ")
    
    # Hacer que la opción elegida sea un dígito, y si no lo es, volver a ejecutar el menú
    if opcion.isdigit() == False:
        print("Seleccione un tipo de valor válido")
    else:
        opcion = int(opcion)

    if opcion == 1:
        f.temp_mes()
    
    if opcion ==2:
        f.precipitacion()
    
    if opcion == 3:
        f.velocidad_viento()
    
    if opcion == 4:
        f.ingresar_fechas()
    
    if opcion == 5:
        seguir_en_programa = False
        print("Eso ha sido todo, vuelva pronto!")        
    else:
        print("Seleccione una opción válida.")