# Imports

from configparser import ConfigParser
import logging
import os
from myninjas.utils import smart_cast
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
from .constants import LOGGER_NAME

JSONLexer = get_lexer_by_name("json")
PythonLexer = get_lexer_by_name("python")
TerminalFormatter = get_formatter_by_name("terminal", linenos=True)

log = logging.getLogger(LOGGER_NAME)

# Exports

__all__ = (
    "filter_fixtures",
    "highlight_code",
    "load_fixtures",
    "JSONLexer",
    "PythonLexer",
    "TerminalFormatter",
)

# Functions


def filter_fixtures(fixtures, apps=None, groups=None, models=None, skip_readonly=False):

    _fixtures = list()
    for f in fixtures:
        if apps is not None and f.app not in apps:
            log.debug("Skipping %s app (not in apps list)." % f.app)
            continue

        if models is not None and f.model is not None and f.model not in models:
            log.debug("Skipping %s model (not in models list)." % f.model)
            continue

        if groups is not None and f.group not in groups:
            log.debug("Skipping %s (not in group)." % f.label)
            continue

        if f.readonly and skip_readonly:
            log.debug("Skipping %s (read only)." % f.label)
            continue

        _fixtures.append(f)

    return _fixtures


def highlight_code(string, lexer=None):
    """Highlight (colorize) the given string as Python code.

    :param string: The string to be highlighted.
    :type string: str

    :param lexer: The pygments lexer to use. Default: ``PythonLexer``

    :rtype: str

    """
    if lexer is None:
        lexer = PythonLexer

    return highlight(string, lexer, TerminalFormatter)


def load_fixtures(path, **kwargs):
    """Load fixture meta data.

    :param path: The path to the fixtures INI file.
    :type path: str

    :rtype: list[FixtureFile] | None

    Remaining keyword arguments are passed to the file.

    """
    from .library.files import FixtureFile

    if not os.path.exists(path):
        log.error("Path does not exist: %s" % path)
        return None

    ini = ConfigParser()
    ini.read(path)

    fixtures = list()
    group = None
    for section in ini.sections():
        _kwargs = kwargs.copy()

        _section = section
        if ":" in section:
            _section, group = section.split(":")

        if "." in _section:
            app_label, model_name = _section.split(".")
        else:
            app_label = _section
            model_name = None

        _kwargs['group'] = group
        _kwargs['model'] = model_name

        for key, value in ini.items(section):
            if key == "db":
                key = "database"
            elif key == "nfk":
                key = "natural_foreign"
            elif key == "npk":
                key = "natural_primary"
            else:
                pass

            _kwargs[key] = smart_cast(value)

        fixtures.append(FixtureFile(app_label, **_kwargs))

    return fixtures
