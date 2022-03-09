import click

@click.command()
@click.argument('nombre')
@click.option('--numero', type=int, help='Número de veces que se repetirá el mensaje')
def cli(nombre, numero):
    '''
    Mensaje de ayuda
    '''
    for i in range(numero):
        print(f'Hola {nombre}!')

if __name__ == '__main__':
    cli()