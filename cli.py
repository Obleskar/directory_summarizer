#!/usr/bin/env python
import click
from os import path, walk
from pandas import DataFrame
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
    dir_sizes = {}
    for directory_path, subdirs, files in walk(top=target_path, topdown=False):
        size_files = sum(size for size in [path.getsize(file_path)
                                               for file_path in [path.join(directory_path, file_name)
                                                            for file_name in files]])
        size_subdirs = sum([dir_sizes[path.join(directory_path, subdirectory)] for subdirectory in subdirs])
        dir_sizes[directory_path] = size_files + size_subdirs
        summary['name'].append(directory_path)
        summary['size'].append(dir_sizes[directory_path])
        summary['file_count'].append(len(files))
        summary['subdirectories'].append(', '.join([directory for directory in subdirs]))
    summary['size'] = [sizeof_fmt(size) for size in summary['size']]
    print('Summary:')
    pprint(summary)
    dataframe = DataFrame(data=summary)
    with open('summary.csv', 'w') as outfile:
        dataframe.to_csv(outfile, index=False)
    print(dataframe)


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


if __name__ == '__main__':
    main()