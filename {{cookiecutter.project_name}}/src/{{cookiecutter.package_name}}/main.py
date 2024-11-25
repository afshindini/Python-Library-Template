"""Run the main code for {{cookiecutter.project_name}}"""

import logging

import click

from {{cookiecutter.package_name}} import __version__
from {{cookiecutter.package_name}}.logging import config_logger


logger = logging.getLogger(__name__)


@click.command()
@click.version_option(version=__version__)
@click.option("-l", "--log_path", type=str, help="Path to save log file")
@click.option("-v", "--verbose", count=True, help="Shorthand for info/debug/warning/error loglevel (-v/-vv/-vvv/-vvvv)")
def {{cookiecutter.package_name}}_cli(log_path: str, verbose: int) -> None:
    """{{ cookiecutter.project_description }} """
    if verbose == 1:
        log_level = 10
    elif verbose == 2:
        log_level = 20
    elif verbose == 3:
        log_level = 30
    else:
        log_level = 40
    config_logger(log_level, log_path)

    click.echo("Run the main code.")
