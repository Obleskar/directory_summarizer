#!/usr/bin/env python
import click
from os import getcwd, path, walk
from pprint import pprint


@click.command()
@click.option('--target_path', '-tp', help='The path of the directory to be summarized..')
def main(target_path):
    """Summarize the contents of a given directory."""
    print('Reading files...')
    summary = {'name': [],
               'size': [],
               'file_count': [],
               'subdirectories': []}
    total_size = 0
    for directory, subdirectories, files in walk(top='resources/', topdown=False):
        directory_size = sum(size for size in [path.getsize(file_path)
                                               for file_path in [path.join(directory, file_name)
                                                            for file_name in files]])
        total_size += directory_size
        summary['name'].append(directory)
        summary['size'].append(path.getsize(directory))
        summary['file_count'].append(len(files))
        summary['subdirectories'].append(', '.join([directory for directory in subdirectories]))
    print('Summary:')
    pprint(summary)


if __name__ == '__main__':
    main()