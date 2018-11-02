from os import path, walk

from pandas import DataFrame


def summarize(directory_path, output_path, dry_run):
    """Summarize the contents and subdirectory sizes of the provided directory."""
    print('Reading directory.')
    summary = {'name': [],
               'size': [],
               'file_count': [],
               'subdirectories': []}
    # Store each subdirectory's size in a dictionary keyed to the subdirectory's name.
    dir_sizes = {}
    for dir_path, subdirs, files in walk_directory(path_to_dir=directory_path):
        # Get total size of all (non-directory) files in the current directory.
        size_files = sum(size for size in [path.getsize(file_path)
                                           for file_path in [path.join(dir_path, file_name)
                                                             for file_name in files]])
        # Get the total size of all subdirectories by the summing the retrieved sizes of each subdirectory.
        size_subdirs = sum([dir_sizes[path.join(dir_path, subdirectory)] for subdirectory in subdirs])
        # Make a size entry for the current directory.
        dir_sizes[dir_path] = size_files + size_subdirs
        # Add the name, size, and file count to the summary.
        summary['name'].append(dir_path)
        summary['size'].append(dir_sizes[dir_path])
        summary['file_count'].append(len(files))
        summary['subdirectories'].append(', '.join([directory for directory in subdirs]))
    print('Formatting size values.')
    summary['size'] = [sizeof_fmt(size) for size in summary['size']]
    # Convert the summary into a dataframe.
    print('Building spreadsheet.')
    dataframe = DataFrame(data=summary)
    if dry_run:
        print(f'Dataframe preview:\n{dataframe.head()}')
        print('This was a dry run. If you\'re pleased with the output above, '
              'then run the same command again without the "-n" option.')
    else:
        print('Writing results to CSV file.')
        # Use the dataframe to write the directory summary to a CSV file.
        with open(path.join(output_path, 'summary.csv'), 'w') as outfile:
            dataframe.to_csv(outfile, index=False)
        print('Your file\'s ready. Look for \"summary.csv\" in the "output" folder.')


def walk_directory(path_to_dir):
    """Traverse the directory tree from the bottom to the top."""
    for directory_path, subdirs, files in walk(top=path_to_dir, topdown=False):
        yield directory_path, subdirs, files


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024
    return "%.1f%s%s" % (num, 'Yi', suffix)
