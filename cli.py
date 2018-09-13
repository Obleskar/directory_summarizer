#!/usr/bin/env python
import click


@click.command()
@click.option('--path', '-p', help='The path of the directory to be summarized..')
def main(path):
    """Summarize the contents of a given directory."""
    print('Reading files...')


if __name__ == '__main__':
    main()