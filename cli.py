#!/usr/bin/env python
import click
from os import makedirs, path, walk
from pandas import DataFrame
from pprint import pprint


@click.command()
@click.option('--target_path', '-p', help='The path of the directory to be summarized.')
def main(target_path):
    """Summarize the contents of a given directory."""
    print('Verifying internal directory structure.')
    if not path.isdir('output'):
        makedirs('output')
    print('Reading directory.')
    summary = {'name': [],
               'size': [],
               'file_count': [],
               'subdirectories': []}
    # Store each subdirectory's size in a dictionary keyed to the subdirectory's name.
    dir_sizes = {}
    # Traverse the directory tree from the bottom to the top.
    for directory_path, subdirs, files in walk(top=target_path, topdown=False):
        # Get total size of all (non-directory) files in the current directory.
        size_files = sum(size for size in [path.getsize(file_path)
                                           for file_path in [path.join(directory_path, file_name)
                                                             for file_name in files]])
        # Get the total size of all subdirectories by the summing the retrieved sizes of each subdirectory.
        size_subdirs = sum([dir_sizes[path.join(directory_path, subdirectory)] for subdirectory in subdirs])
        # Make a size entry for the current directory.
        dir_sizes[directory_path] = size_files + size_subdirs
        # Add the name, size, and file count to the summary.
        summary['name'].append(directory_path)
        summary['size'].append(dir_sizes[directory_path])
        summary['file_count'].append(len(files))
        summary['subdirectories'].append(', '.join([directory for directory in subdirs]))
    print('Formatting size values.')
    summary['size'] = [sizeof_fmt(size) for size in summary['size']]
    # Convert the summary into a dataframe.
    print('Building spreadsheet.')
    dataframe = DataFrame(data=summary)
    print('Writing results to CSV file.')
    # Use the dataframe to write the directory summary to a CSV file.
    with open(path.join('output', 'summary.csv'), 'w') as outfile:
        dataframe.to_csv(outfile, index=False)
    print('Your file\'s ready. Look for \"summary.csv\" in the current folder.')


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


if __name__ == '__main__':
    main()