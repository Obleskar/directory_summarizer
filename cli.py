#!/usr/bin/env python
import click
from os import getcwd, path, walk


@click.command()
@click.option('--path', '-p', help='The path of the directory to be summarized..')
def main(path):
    """Summarize the contents of a given directory."""
    print('Reading files...')
    summary = {}
    # Build a nested dictionary that represents the given directory.
    for directory, subdirectories, files in walk(top='resources/'):
        print(f'Found directory: {directory}')
        print(f'Found subdirectories: {subdirectories}')
        print(f'Found files in directory: {files}')
        print('\n\n')


if __name__ == '__main__':
    main()