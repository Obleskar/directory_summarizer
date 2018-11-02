from click import command, option
from os import makedirs, path, walk
from pandas import DataFrame
from pprint import pprint


@command()
@option('--directory_path', '-p', help='The path of the directory to be summarized.')
@option('--output_path', '-o', help='Path to where the summary results file should be saved.')
@option('--dry_run', '-n', is_flag=True, help='Preview program output without generating an output file.')


if __name__ == '__main__':
    main()
