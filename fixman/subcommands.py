# Imports

from configparser import ConfigParser
import logging
from subprocess import getstatusoutput

from myninjas.utils import read_file
import os
from .library.commands import DumpData, LoadData
from .constants import EXIT_ERROR, EXIT_OK, EXIT_UNKNOWN, LOGGER_NAME
from .utils import filter_fixtures, highlight_code, load_fixtures, JSONLexer

log = logging.getLogger(LOGGER_NAME)

# Functions


def dumpdata(path, apps=None, database=None, groups=None, models=None, natural_foreign=False,
             natural_primary=False, preview_enabled=False, project_root=None, settings=None):

    fixtures = load_fixtures(
        path,
        database=database,
        natural_foreign=natural_foreign,
        natural_primary=natural_primary,
        project_root=project_root,
        settings=settings
    )
    if not fixtures:
        return EXIT_ERROR

    success = list()
    _fixtures = filter_fixtures(fixtures, apps=apps, groups=groups, models=models, skip_readonly=True)
    for f in _fixtures:

        # if apps is not None and f.app not in apps:
        #     log.debug("Skipping %s app (not in apps list)." % f.app)
        #     continue
        #
        # if models is not None and f.model is not None and f.model not in models:
        #     log.debug("Skipping %s model (not in models list)." % f.model)
        #     continue
        #
        # if groups is not None and f.group not in groups:
        #     log.debug("Skipping %s (not in group)." % f.label)
        #     continue
        #
        # if f.readonly:
        #     log.debug("Skipping %s (read only)." % f.label)
        #     continue

        log.info("Dumping fixtures to: %s" % f.get_full_path())

        dump = DumpData(
            f.app,
            database=f.database,
            export=f.export,
            natural_foreign=f.natural_foreign,
            natural_primary=f.natural_primary,
            path=f.get_full_path(),
            settings=f.settings
        )
        if preview_enabled:
            success.append(True)
            if not os.path.exists(f.get_path()):
                print("mkdir -p %s" % f.get_path())

            print(dump.preview())

            if f.copy_to is not None:
                print("cp %s %s" % (f.get_full_path(), f.copy_to))
        else:
            if not os.path.exists(f.get_path()):
                os.makedirs(f.get_path())

            if dump.run():
                success.append(dump.run())

                if f.copy_to is not None:
                    getstatusoutput("cp %s %s" % (f.get_full_path(), f.copy_to))
            else:
                log.error(dump.get_output())
            
    if all(success):
        return EXIT_OK

    return EXIT_ERROR


def inspect(path, apps=None, groups=None, models=None, project_root=None):
    fixtures = load_fixtures(path, project_root=project_root)
    if not fixtures:
        return EXIT_ERROR

    exit_code = EXIT_OK
    _fixtures = filter_fixtures(fixtures, apps=apps, groups=groups, models=models)
    for f in _fixtures:
        try:
            content = read_file(f.get_full_path())
        except FileNotFoundError as e:
            exit_code = EXIT_UNKNOWN
            content = str(e)

        print("")
        print(f.label)
        print("-" * 120)
        print(highlight_code(content, lexer=JSONLexer))
        print("-" * 120)

    return exit_code


def loaddata(path, apps=None, database=None, groups=None, models=None, preview_enabled=False,
             project_root=None, settings=None, to_script=False):

    fixtures = load_fixtures(path, database=database, project_root=project_root, settings=settings)
    if not fixtures:
        return EXIT_ERROR

    if to_script:
        script = list()
        script.append("!# /usr/bin/env bash")
        script.append("")

    success = list()
    _fixtures = filter_fixtures(fixtures, apps=apps, groups=groups, models=models)
    for f in _fixtures:
        log.info("Loading fixtures from: %s" % f.get_full_path())

        load = LoadData(
            f.app,
            database=f.database,
            path=f.get_full_path(),
            settings=f.settings
        )

        if to_script:
            # noinspection PyUnboundLocalVariable
            script.append(load.preview())
            continue

        if preview_enabled:
            success.append(True)
            print(load.preview())
        else:
            if load.run():
                success.append(load.run())
            else:
                log.error(load.get_output())

    if to_script:
        script.append("")
        print("\n".join(script))
        return EXIT_OK

    if all(success):
        return EXIT_OK

    return EXIT_ERROR

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
