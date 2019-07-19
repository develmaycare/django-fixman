# Imports

from configparser import ConfigParser
import logging
import os
from subprocess import getstatusoutput
from ..constants import EXIT_INPUT, EXIT_OK, EXIT_UNKNOWN, LOGGER_NAME

log = logging.getLogger(LOGGER_NAME)

# Classes


class DumpData(object):

    def __init__(self, app, database=None, file_name=None, model=None, natural_foreign=False,
                 natural_primary=False, path=None, settings=None):
        self.app = app
        self.database = database
        self.file_name = file_name or "initial.json"
        self.model = model
        self.natural_foreign = natural_foreign
        self.natural_primary = natural_primary
        self.settings = settings

        if model is not None:
            self.export = "%s.%s" % (app, model)

            if file_name is None:
                self.file_name = "%s.json" % model.lower()
        else:
            self.export = app

        if path is not None:
            self.path = path
        else:
            self.path = os.path.join("local", app, "fixtures")

        self._full_path = os.path.join(self.path, self.file_name)

    def get_command(self):
        a = list()

        a.append("(cd source && ./manage.py dumpdata")

        if self.database is not None:
            a.append("--database=%s" % self.database)

        a.append("--indent=4")

        if self.natural_foreign:
            a.append("--natural-foreign")

        if self.natural_primary:
            a.append("--natural-primary")

        if self.settings is not None:
            a.append("--settings=%s" % self.settings)

        a.append("%s > %s)" % (self.export, self._full_path))

        return " ".join(a)

    def preview(self):
        return self.get_command()

    def run(self):
        command = self.get_command()

        status, output = getstatusoutput(command)

        if status > EXIT_OK:
            return False

        return True


class LoadData(object):

    def __init__(self, app, database=None, file_name=None, model=None, path=None, settings=None):
        self.app = app
        self.database = database
        self.file_name = file_name or "initial.json"
        self.model = model
        self.path = path
        self.settings = settings

        if model is not None and file_name is None:
            self.file_name = "%s.json" % model.lower()

        if path is not None:
            self.path = path
        else:
            self.path = os.path.join("local", app, "fixtures")

        self._full_path = os.path.join(self.path, self.file_name)

    def get_command(self):
        a = list()

        a.append("(cd source && ./manage.py loaddata")

        if self.database is not None:
            a.append("--database=%s" % self.database)

        if self.settings is not None:
            a.append("--settings=%s" % self.settings)

        a.append("%s)" % self._full_path)

        return " ".join(a)

    def preview(self):
        return self.get_command()

    def run(self):
        command = self.get_command()

        status, output = getstatusoutput(command)

        if status > EXIT_OK:
            return False

        return True

'''
class Fixture(object):

    def __init__(self, model, operation, **kwargs):
        self.app_label, self.model_name = model.split(".")
        self.database = kwargs.pop("database", None)
        self.group = kwargs.pop("group", "defaults")
        self.is_readonly = kwargs.pop("readonly", False)
        self.model = model
        self.operation = operation
        self.output = None
        self.settings = kwargs.pop("settings", None)
        self.status = None
        self._preview = kwargs.pop("preview", False)

        default_path = os.path.join(self.app_label, "fixtures", self.model_name.lower())
        self.path = kwargs.pop("path", default_path)

    def __repr__(self):
        return "<%s %s.%s>" % (self.__class__.__name__, self.app_label, self.model_name)

    def get_command(self):
        if self.operation == "dumpdata":
            return self._get_dumpdata_command()
        elif self.operation == "loaddata":
            return self._get_loaddata_command()
        else:
            raise ValueError("Invalid fixture operation: %s" % self.operation)

    def preview(self):
        return self.get_command()

    def run(self):
        command = self.get_command()
        status, output = getstatusoutput(command)

        self.output = output
        self.status = status

        if status > EXIT_OK:
            return False

        return True

    def _get_dumpdata_command(self):
        a = list()

        a.append("(cd source && ./manage.py dumpdata")

        if self.settings is not None:
            a.append("--settings=%s" % self.settings)

        if self.database is not None:
            a.append("--database=%s" % self.database)

        # args.full_preview_enabled = True
        if self._preview:
            a.append("--indent=4 %s)" % self.model)
        else:
            a.append("--indent=4 %s > %s)" % (self.model, self.path))

        return " ".join(a)

    def _get_loaddata_command(self):
        a = list()
        a.append("(cd source && ./manage.py loaddata")

        if self.settings is not None:
            a.append("--settings=%s" % self.settings)

        if self.database is not None:
            a.append("--database=%s" % self.database)

        a.append("%s)" % self.path)

        return " ".join(a)
'''
