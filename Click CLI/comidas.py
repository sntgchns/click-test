import click

@click.group()
def comidas():
    pass

@comidas.group()
def almuerzo():
    pass

@comidas.group()
def cena():
    pass

@click.command()
def hamburguesa():
    print(f'Disfruta tu Hamburguesa!')

almuerzo.add_command(hamburguesa)
cena.add_command(hamburguesa)

if __name__ == '__main__':
    comidas()