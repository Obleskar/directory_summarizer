#!/usr/bin/env python
import click
from os import getcwd, path, walk


@click.command()
@click.option('--path', '-p', help='The path of the directory to be summarized..')
def main(path):
    """Summarize the contents of a given directory."""
    print('Reading files...')
    summary = {'name': [],
               'size': [],
               'file_count': [],
               'subdirectories' []}
    for directory, subdirectories, files in walk(top='resources/'):
        summary['name'].append(directory)
        summary['size'].append(path.getsize(directory))
        summary['file_count'].append(len(files))
        summary['subdirectories'].append(', '.join([directory for directory in subdirectories]))


if __name__ == '__main__':
    main()