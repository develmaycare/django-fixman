# Imports

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from myninjas.logging import LoggingHelper
from .constants import EXIT_FAILURE, EXIT_UNKNOWN, LOGGER_NAME
from . import initialize
from . import subcommands

DEBUG = 10

logging = LoggingHelper(colorize=True, name=LOGGER_NAME)
log = logging.setup()

# Commands


def main_command():
    """Work with Django fixtures."""

    __author__ = "Shawn Davis <shawn@develmaycare.com>"
    __date__ = "2019-07-18"
    __help__ = """NOTES

Work with Django fixtures.

    """
    __version__ = "0.5.0-d"

    # Main argument parser from which sub-commands are created.
    parser = ArgumentParser(description=__doc__, epilog=__help__, formatter_class=RawDescriptionHelpFormatter)

    # Access to the version number requires special consideration, especially
    # when using sub parsers. The Python 3.3 behavior is different. See this
    # answer: http://stackoverflow.com/questions/8521612/argparse-optional-subparser-for-version
    parser.add_argument(
        "-v",
        action="version",
        help="Show version number and exit.",
        version=__version__
    )

    parser.add_argument(
        "--version",
        action="version",
        help="Show verbose version information and exit.",
        version="%(prog)s" + " %s %s by %s" % (__version__, __date__, __author__)
    )

    # Initialize sub-commands.
    subparsers = parser.add_subparsers(
        dest="subcommand",
        help="Commands",
        metavar="dumpdata, loaddata"
    )

    initialize.subcommands(subparsers)

    # Parse arguments.
    args = parser.parse_args()

    command = args.subcommand

    # Set debug level.
    if args.debug_enabled:
        log.setLevel(DEBUG)

    log.debug("Namespace: %s" % args)

    exit_code = EXIT_UNKNOWN
    if command in ("dd", "dump", "dumpdata"):
        exit_code = subcommands.dumpdata(
            args.path,
            apps=args.app_names,
            groups=args.group_names,
            models=args.model_names,
            preview_enabled=args.preview_enabled
        )
    elif command in ("ld", "load", "loaddata"):
        exit_code = subcommands.loaddata(
            args.path,
            apps=args.app_names,
            groups=args.group_names,
            models=args.model_names,
            preview_enabled=args.preview_enabled
        )
    else:
        log.error("Unsupported command: %s" % command)

    exit(exit_code)
