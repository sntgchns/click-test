import requests, json

programa = True
while programa:
    ruta = input('Ingresa una ruta de la API: ')
    try:
        url = 'https://sntgchns.herokuapp.com/api/santi/{}'.format(ruta)
        dato_buscado = input('Ingresa un dato a buscar en /{}: '.format(ruta))
        print(requests.get(url).json()[dato_buscado])
        programa = True        
    except KeyError:
        print('El dato \'{}\' no existe en la ruta \'{}\''.format(dato_buscado, ruta))
    except json.decoder.JSONDecodeError:
        print('La ruta \'{}\' no existe'.format(ruta))