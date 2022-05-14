import os


def add(recipe_path):
    if not os.path.exists(recipe_path):
        raise ValueError('File Does not exist')

    with open(recipe_path) as file:
        print(file.readlines())