# -*- coding: utf-8 -*-

"""Console script for assignment3."""

import click


@click.command()
@click.option("--input", default=None, help="input URI(file or URL)")
def main(args=None):
    """Console script for assignment3."""
	print ("input", input)
	return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())