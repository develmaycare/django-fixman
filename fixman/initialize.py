# Imports

import logging
from .constants import LOGGER_NAME

log = logging.getLogger(LOGGER_NAME)

# Exports

# Functions


def subcommands(subparsers):
    commands = SubCommands(subparsers)
    commands.dumpdata()
    commands.inspect()
    commands.loaddata()

# Classes


class SubCommands(object):
    """A utility class which keeps the ``cli.py`` module clean."""

    def __init__(self, subparsers):
        self.subparsers = subparsers

    def dumpdata(self):
        """Create the dumpdata sub-command."""
        sub = self.subparsers.add_parser(
            "dumpdata",
            aliases=["dd", "dump"],
            help="Export Django fixtures."
        )

        self._add_common_options(sub)

    def inspect(self):
        """Create the inspect sub-command."""
        sub = self.subparsers.add_parser(
            "inspect",
            aliases=["ins"],
            help="Display Django fixtures."
        )

        self._add_common_options(sub)

    def loaddata(self):
        """Create the loaddata sub-command."""
        sub = self.subparsers.add_parser(
            "loaddata",
            aliases=["ld", "load"],
            help="Load Django fixtures."
        )

        sub.add_argument(
            "-S",
            "--script",
            action="store_true",
            dest="to_script",
            help="Export to a bash script."
        )

        self._add_common_options(sub)

    # noinspection PyMethodMayBeStatic
    def _add_common_options(self, sub):
        """Add the common switches to a given sub-command instance.

        :param sub: The sub-command instance.

        """
        sub.add_argument(
            "-A=",
            "--app-name=",
            action="append",
            dest="app_names",
            help="Only work with this app. May be used multiple times."
        )

        sub.add_argument(
            "-D",
            "--debug",
            action="store_true",
            dest="debug_enabled",
            help="Enable debug output."
        )

        sub.add_argument(
            "-G=",
            "--group-name=",
            action="append",
            dest="group_names",
            help="Only work with this group. May be used multiple times."
        )

        sub.add_argument(
            "-M=",
            "--model-name=",
            action="append",
            dest="model_names",
            help="Only work with this model. May be used multiple times."
        )

        sub.add_argument(
            "-P=",
            "--path=",
            default="fixtures/config.ini",
            dest="path",
            help="The path to the fixtures INI file. Default: fixtures/config.ini"
        )

        sub.add_argument(
            "-p",
            "--preview",
            action="store_true",
            dest="preview_enabled",
            help="Preview the commands."
        )

        sub.add_argument(
            "-r=",
            "--project-root=",
            dest="project_root",
            help="The path to the project."
        )

        sub.add_argument(
            "-s=",
            "--settings=",
            dest="settings",
            help="The dotted path to the Django settings file."
        )
