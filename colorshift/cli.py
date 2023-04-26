# -*- coding: utf-8 -*-

"""Console script for colorshift."""
import sys
import click

import colorshift


@click.command()
def main(args=None):
    """Console script for colorshift."""
    click.echo("Replace this message by putting your code into "
               "colorshift.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    colorshift.loop()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
