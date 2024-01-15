"""A sample CLI."""

import click
import gradle_analysis


@click.command()
@click.argument('path')
def main(path: str):
    try:
        java_version = gradle_analysis.analyze_java_version(path)
        click.echo(java_version)
    except Exception as e:
        click.echo(e)

if __name__ == '__main__':  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
