import subprocess
import sys
from pathlib import Path

from .__init__ import __version__
from .display import print_observer_error


def get_python_version():
    return (
        subprocess.check_output(f"{sys.executable} --version", shell=True)
        .strip()
        .decode("utf-8")
    )


def get_observer_version():
    return __version__


def run_file(command):
    cmd = [sys.executable, *command]

    return subprocess.run(cmd)


def resolve_path(path):
    return Path(path).resolve()


def check_for_errors(file_path):
    path = Path(file_path)

    errors = {
        # fmt: off
        not path.is_file():     f"'{file_path}' does not exist",
        path.is_dir():          f"'{file_path}' is a directory, expected a file",
        # fmt: on
    }

    for condition, message in errors.items():
        if condition:
            print_observer_error(message)
