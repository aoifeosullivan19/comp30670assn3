# -*- coding: utf-8 -*-

"""Console script for assignment3."""

import click
import sys
click.disable_unicode_literals_warning=True

@click.command()
@click.option("--input", default='input.txt', help="input URI(file or URL)")
def main(input=None): 
	"""Console script for assignment3."""
	print ("input", input)
	N, instructions = parseFile(input)
	ledTester=LEDTester(N)
	for instruction in instructions:
		ledTester.apply(instruction)
	print ('number occupied: ', ledTester.countOccupied())
	return 0


if __name__ == "__main__":
    sys.exit(main())
