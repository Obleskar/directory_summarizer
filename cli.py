from click import command, option

from main import summarize, get_ext_breakdown


@command()
@option('--directory_path', '-p', help='The path of the directory to be summarized.')
@option('--output_path', '-o', help='Path to where the summary results file should be saved.')
@option('--dry_run', '-n', is_flag=True, help='Preview program output without generating an output file.')
def get_summary(directory_path, output_path, dry_run):
    """Get a summary of the provided directory."""
    summarize(directory_path=directory_path, output_path=output_path, dry_run=dry_run)


if __name__ == '__main__':
    get_summary()
