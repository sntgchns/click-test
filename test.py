import requests, json


# Se crea una variable para guardar los datos de las rutas de la API, y se guardan en un diccionario.
url = 'https://sntgchns.herokuapp.com/api'.format()
consulta_rutas = requests.get(url).json()['rutas']
# La función ayuda() imprime las rutas válidas formateadas con json.dumps en forma de lista, y se vuelve a pedir la ruta.
def ayuda():
    print('Las rutas válidas son: {}'.format(json.dumps(list(consulta_rutas), sort_keys=False, indent=2, ensure_ascii=False)))
# La función ayuda_datos() imprime los datos válidos formateados con json.dumps en forma de lista, y se vuelve a pedir el dato.
def ayuda_datos():
    print('Los datos válidos son: {}'.format(json.dumps(list(respuesta.keys()), sort_keys=False, indent=2, ensure_ascii=False)))
# La función datos() imprime los datos de la API formateados con json.dumps, y se pregunta si se desea ver los datos de otra ruta.
def datos():
    # Se declaran como globales las variables, para que puedan ser usadas en la función datos().
    global dato_buscado, dato, programa
    dato_buscado = input('Ingresa el dato para ver el valor: '.format(ruta))
    dato = respuesta[dato_buscado]
    # Imprime el dato solicitado junto a su su valor, y se pregunta si se desea consultar otra ruta.
    print(('"{}": '.format(dato_buscado)) + json.dumps(dato, sort_keys=False, indent=2, ensure_ascii=False))
    # Pregunta si se desea consultar otra ruta ó salir.
    print('Desea realizar otra consulta? (s/n)')
    if input() == 'n':
        print('Gracias por usar el programa')
        # Cierre del programa.
        programa = False#

# Comienzo del programa
programa = True

while programa:
    # Se pide la ruta a la que se desea acceder.da
    ruta = input('Ingresa una ruta de la API: ')
    # Intenta obtener de la API la ruta ingresada.
    try:
        url = 'https://sntgchns.herokuapp.com/api/santi/{}'.format(ruta)#
        pedido = requests.get(url)
        respuesta = pedido.json()
        # Si existe, se imprimen los datos de la ruta solicitada.
        print(json.dumps(list(respuesta), sort_keys=False, indent=8, ensure_ascii=False))
        # Se ejeuta la función datos() para preguntar si se desea ver un dato en particular de la ruta.
        
        datos()
    # Cuando la ruta no existe se muestra la ruta ingresada y el error. 
    # Se ejecuta la función ayuda() para mostrar las rutas válidas.
    except json.decoder.JSONDecodeError:
        print('La ruta \'{}\' no existe en /santi/<string:ruta>'.format(ruta))
        ayuda()
    # Cuando la ruta existe pero no tiene el dato solicitado, se muestra la ruta ingresada y el error. 
    # Se ejecuta la función ayuda_datos() para mostrar los datos válidos.
    # Se ejecuta la función datos() para preguntar si se desea ver un dato en particular de la ruta.
    except KeyError:
        print('El dato \'{}\' no se encuentra en la ruta \'{}\''.format(dato_buscado, ruta))
        ayuda_datos()
        datos()