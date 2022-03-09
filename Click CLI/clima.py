import click

@click.command()
@click.option('--clima', type=click.Choice(['soleado', 'nublado', 'lluvioso', 'nevado']))
def clima(clima):
    print(f'Me gusta cuando está {clima}')
    '''
    Mensaje de ayuda
    '''
    # if clima == 'soleado':
    #     print('El clima es soleado')
    # elif clima == 'nublado':
    #     print('El clima es nublado')
    # elif clima == 'lluvioso':
    #     print('El clima es lluvioso')
    # elif clima == 'nevado':
    #     print('El clima es nevado')
    # else:
    #     print('No se ha ingresado un clima válido')

if __name__ == '__main__':
    clima()