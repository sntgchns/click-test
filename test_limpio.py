import requests, json

programa = True

while programa:
    ruta = input('Ingresa una ruta de la API: ')
    try:
        url = 'https://sntgchns.herokuapp.com/api/santi/{}'.format(ruta)
        respuesta = requests.get(url).json()        
        print(json.dumps(list(respuesta), sort_keys=False, indent=4, ensure_ascii=False))
        dato_buscado = input('Ingresa un dato a buscar en /{}: '.format(ruta))
        dato = respuesta[dato_buscado]
        print(json.dumps(dato, sort_keys=False, indent=2, ensure_ascii=False))
        print('Desea realizar otra consulta? (s/n)')
        if input() == 'n':
            print('Gracias por usar el programa')
            programa = False#
    except:
        continue
