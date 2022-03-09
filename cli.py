#!/usr/bin/env python
import click

@click.group()
def cli():
    print("cli")
    
# python cli.py hola
@cli.command()
def hola():
    print("Hola mundo!")

if __name__ == '__main__':
    cli()