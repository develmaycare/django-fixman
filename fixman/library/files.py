# Imports

import os

# Classes


class FixtureFile(object):

    def __init__(self, app, comment=None, copy_to=None, database=None, file_name=None, group=None, model=None,
                 natural_foreign=False, natural_primary=False, path=None, project_root=None, readonly=False,
                 settings=None):
        self.app = app
        self.comment = comment
        self.copy_to = copy_to
        self.database = database
        self.file_name = file_name or "initial.json"
        self.group = group
        self.model = model
        self.natural_foreign = natural_foreign
        self.natural_primary = natural_primary
        self.readonly = readonly
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
            self.path = os.path.join("fixtures", app)

        if project_root is not None:
            self._full_path = os.path.join(project_root, self.path, self.file_name)
        else:
            self._full_path = os.path.join(self.path, self.file_name)

    def __repr__(self):
        return "<%s %s>" %  (self.__class__.__name__, self._full_path)

    def get_path(self):
        """Get the path to the fixture file (without the file).

        :rtype: str

        """
        return os.path.dirname(self._full_path)

    def get_full_path(self):
        """Get the full path to the fixture file.

        :rtype: str

        """
        return self._full_path

    @property
    def label(self):
        """Get a display name for the fixture.

        :rtype: str

        """
        if self.model is not None:
            return "%s.%s" % (self.app, self.model)

        return self.app
