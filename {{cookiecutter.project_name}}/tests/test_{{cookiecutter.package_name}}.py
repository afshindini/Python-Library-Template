"""Package level tests"""

from {{cookiecutter.package_name}} import __version__


def test_version() -> None:
    """Unit test for checking the version of the code"""
    assert __version__ == "{{ cookiecutter.version }}"
