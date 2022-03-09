import requests, json

# rutas de la URL de la API
    # url = 'https://sntgchns.herokuapp.com/api'
    #     {
    #     "API": [
    #         "/santi", 
    #             [
    #             "/datos", 
    #             "/contacto", 
    #             "/educacion", 
    #             "/idiomas", 
    #             "/habilidades", 
    #             "/intereses", 
    #             "/social"
    #             ]
    #         ], 
    #     "Mensaje": "Gracias por conectarte!"
    #     }
programa = True
while programa:
    def ayuda():
        print('Las rutas válidas son: {}'.format(rutas))
    print('Para obtener ayuda de la API, ingrese \'ayuda\' en la terminal, ó \'salir\' para salir del programa.')
    ruta = input('Ingresa una ruta de la API: ')
    rutas = {'datos', 'contacto', 'educacion', 'idiomas', 'habilidades', 'intereses', 'social'}
    ingreso = ruta.split()
    try:
        if any(ruta in rutas for ruta in ingreso):
            url = 'https://sntgchns.herokuapp.com/api/santi/{}'.format(ruta)
            pedido = requests.get(url)
            respuesta = pedido.json()
            print(respuesta)
            dato_buscado = input('Ingresa un dato a buscar en /{}: '.format(ruta))
            dato = respuesta[dato_buscado]
            print(dato)
            programa = True
        elif ruta == 'ayuda':
            ayuda()
        elif ruta == 'salir':
            programa = False
        else:
            print('La ruta \'{}\' no se encuentra.'.format(ruta))
            ayuda()
    except KeyError:
        print('El dato \'{}\' no se encuentra en la ruta \'{}\''.format(dato_buscado, ruta))
        ayuda()