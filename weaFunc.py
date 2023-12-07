# Importar modulos
import pandas as pd

# Funciones
def temp_mes():
    df = pd.read_csv('weather.csv')
    df['date'] = pd.to_datetime(df['date'])
    mes = input("Ingrese el numero del mes del cual desea ver el promedio: ")
    df = df[df['date'].dt.month == int(mes)]
    promedio = df['temperature'].mean()
    print("")
    print(f"El promedio de la temperatura de ese mes es: {promedio} ")
    print("")

def precipitacion():
    df = pd.read_csv('weather.csv')
    df['date'] = pd.to_datetime(df['date'])
    mes = input("Ingrese el mes del cual desea ver el total de precipitacion: ")
    df = df[df['date'].dt.month == int(mes)]
    total = df['precipitation'].sum()
    print("")
    print(f"El total de precipitacion del mes {mes} fue: {total}")
    print("")

def velocidad_viento():
    df = pd.read_csv('weather.csv')
    df['date'] = pd.to_datetime(df['date'])
    indice_maxima_velocidad = df['wind_speed'].idxmax()
    velocidad = df['wind_speed'].max()
    dia_maxima_velocidad = df.loc[indice_maxima_velocidad, 'date'].date()
    print("")
    print(f"El dia que hubor mayor velocidad de viento fue: {dia_maxima_velocidad}")
    print("")

def ingresar_fechas():
    print("")
    print("Las fechas deben estar en formato YYYY-MM-DD")
    fecha_inicial = input("fecha inicial: ")
    fecha_final = input("fecha final: ")

    # Crear una lista de fechas usando date_range()
    lista_fechas = pd.date_range(start = fecha_inicial, end = fecha_final).strftime('%Y-%m-%d').tolist()

    # Escribir la lista en un archivo llamado "sample.csv"
    with open('sample.csv', 'w') as f:
        f.writelines('\n'.join(lista_fechas))
    
    print("")
    print("Su base de datos en un rango de 2 fechas se ha creado exitosamente!")
    print("")