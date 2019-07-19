# Imports

from configparser import ConfigParser
import logging
import os
from subprocess import getstatusoutput
# from .library import Fixture
from .library.commands import DumpData, LoadData
from .constants import EXIT_ERROR, EXIT_OK, EXIT_UNKNOWN, LOGGER_NAME

log = logging.getLogger(LOGGER_NAME)

# Functions


def dumpdata(path, apps=None, database=None, groups=None, models=None, natural_foreign=False,
             natural_primary=False, preview_enabled=False, settings=None):

    if not os.path.exists(path):
        log.error("Path does not exist: %s" % path)

    ini = ConfigParser()
    ini.read(path)

    fixtures = list()
    group = None
    for section in ini.sections():
        _section = section
        if ":" in section:
            _section, group = section.split(":")

        if "." in _section:
            app_label, model_name = _section.split(".")
        else:
            app_label = _section
            model_name = None

        kwargs = {
            'database': database,
            'group': group,
            'model': model_name,
            'natural_foreign': natural_foreign,
            'natural_primary': natural_primary,
            'settings': settings
        }

        for key, value in ini.items(section):
            kwargs[key] = value

        fixtures.append(FixtureFile(app_label, **kwargs))

    success = list()
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

        if f.readonly:
            log.debug("Skipping %s (read only)." % f.label)
            continue

        dump = DumpData(
            f.app,
            database=f.database,
            file_name=f.file_name,
            model=f.model,
            natural_foreign=f.natural_foreign,
            natural_primary=f.natural_primary,
            path=f.path,
            settings=f.settings
        )
        if preview_enabled:
            success.append(True)
            print(dump.preview())
        else:
            success.append(dump.run())
            
    if all(success):
        return EXIT_OK

    return EXIT_ERROR


def loaddata(path, apps=None, database=None, groups=None, models=None, preview_enabled=False, settings=None):

    if not os.path.exists(path):
        log.error("Path does not exist: %s" % path)

    ini = ConfigParser()
    ini.read(path)

    fixtures = list()
    group = None
    for section in ini.sections():
        _section = section
        if ":" in section:
            _section, group = section.split(":")

        if "." in _section:
            app_label, model_name = _section.split(".")
        else:
            app_label = _section
            model_name = None

        kwargs = {
            'database': database,
            'group': group,
            'model': model_name,
            'settings': settings
        }

        for key, value in ini.items(section):
            kwargs[key] = value

        fixtures.append(FixtureFile(app_label, **kwargs))

    success = list()
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

        if f.readonly:
            log.debug("Skipping %s (read only)." % f.label)
            continue

        load = LoadData(
            f.app,
            database=f.database,
            file_name=f.file_name,
            model=f.model,
            path=f.path,
            settings=f.settings
        )
        if preview_enabled:
            success.append(True)
            print(load.preview())
        else:
            success.append(load.run())

    if all(success):
        return EXIT_OK

    return EXIT_ERROR


class FixtureFile(object):

    def __init__(self, app, comment=None, database=None, file_name=None, group=None, model=None,
                 natural_foreign=False, natural_primary=False, path=None, readonly=False, settings=None):
        self.app = app
        self.comment = comment
        self.database = database
        self.file_name = file_name
        self.group = group
        self.model = model
        self.natural_foreign = natural_foreign
        self.natural_primary = natural_primary
        self.path = path
        self.readonly = readonly
        self.settings = settings

    def __repr__(self):
        return "<%s %s>" %  (self.__class__.__name__, self.label)

    @property
    def label(self):
        """Get a display name for the fixture.

        :rtype: str

        """
        if self.model is not None:
            return "%s.%s" % (self.app, self.model)

        return self.app

'''

def dumpdata(args):
    """Dump data using a fixtures.ini file."""

    # Make sure the file exists.
    path = args.path
    if not os.path.exists(path):
        logger.warning("fixtures.ini file does not exist: %s" % path)
        return EXIT_INPUT

    # Load the file.
    ini = ConfigParser()
    ini.read(path)

    # Generate the commands.
    for model in ini.sections():
        kwargs = dict()

        if args.full_preview_enabled:
            kwargs['preview'] = True

        if args.settings:
            kwargs['settings'] = args.settings

        for key, value in ini.items(model):
            kwargs[key] = value

        fixture = Fixture(model, "dumpdata", **kwargs)
        if args.app_labels and fixture.app_label not in args.app_labels:
            logger.info("(SKIPPED) %s" % fixture.model)

            continue

        if args.model_name and fixture.model_name.lower() != args.model_name.lower():
            logger.info("(SKIPPED) %s" % fixture.model)

            continue

        if args.groups and fixture.group not in args.groups:
            logger.info("(SKIPPED) %s" % fixture.model)

            continue

        if fixture.is_readonly:
            logger.info("(READONLY) %s (dumpdata skipped)" % fixture.model)
            continue

        if args.preview_enabled or args.full_preview_enabled:
            logger.info("(PREVIEW) %s" % fixture.preview())

            if args.full_preview_enabled:
                fixture.run()
                print(fixture.output)
        else:
            result = fixture.run()
            if result:
                logger.info("(OK) %s" % fixture.model)
            else:
                logger.info("(FAILED) %s %s" % (fixture.model, fixture.output))
                return EXIT_UNKNOWN

    return EXIT_OK


def loaddata(args):
    """Load data using a fixtures.ini file."""

    path = args.path
    if not os.path.exists(path):
        logger.warning("fixtures.ini file does not exist: %s" % path)
        return EXIT_INPUT

    # Load the file.
    ini = ConfigParser()
    ini.read(path)

    # Generate the commands.
    for model in ini.sections():
        kwargs = dict()

        if args.settings:
            kwargs['settings'] = args.settings

        for key, value in ini.items(model):
            kwargs[key] = value

        fixture = Fixture(model, "loaddata", **kwargs)

        if args.app_labels and fixture.app_label not in args.app_labels:
            if args.preview_enabled:
                logger.info("(SKIPPED) %s" % fixture.model)

            continue

        if args.model_name and fixture.model_name.lower() != args.model_name.lower():
            if args.preview_enabled:
                logger.info("(SKIPPED) %s" % fixture.model)

            continue

        if args.groups and fixture.group not in args.groups:
            if args.preview_enabled:
                logger.info("[SKIPPED] %s" % fixture.model)

            continue

        if args.preview_enabled:
            logger.info("(PREVIEW) %s" % fixture.preview())
        else:
            result = fixture.run()
            if result:
                logger.info("(OK) %s %s" % (fixture.model, fixture.output))
            else:
                logger.warning("(FAILED) %s %s" % (fixture.model, fixture.output))
                return EXIT_UNKNOWN

    return EXIT_OK
'''
