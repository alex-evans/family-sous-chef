import click

from . import __version__
from .recipe_db import add as addRecipe


@click.command()
@click.version_option(version=__version__)
@click.option('--add-recipe', type=click.Path(), help='Recipe filepath to load')
def main(add_recipe):
    '''Family Sous Chef'''
    if add_recipe:
        addRecipe(add_recipe)
    else:
        click.echo('What you want to eat!?!')
