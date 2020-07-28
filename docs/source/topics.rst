.. _topics:

******
Topics
******

Fixture Files
=============

When ``app_name.Model`` is specified as the config section, the default location of fixtures files is:

``<project_root>/fixtures/<app_label>/<model_name>.json``

.. note::
    The ``<model_name>`` in the path is always singular and lower case.

If no model is given, the default path is:

``<project_root>/fixtures/<app_label>/initial.json``

The ``file_name`` and ``path`` options may be used to override the default.

Configuration
=============

Each section in the ``config.ini`` file represents a fixture. For example, ``[todos]`` refers to the todos app. ``[todos.Todo]`` refers to the Todo model within the todos app.

Simply specifying a section is enough to dump, load and inspect fixture files. However, there are some additional options that may be specified with the section to control these behaviors.

Simply specifying a section is enough to dump and load fixture files. However, there are some additional options that may be specified with the section to control these behaviors.

- ``comment``: An optional comment regarding the fixtures.
- ``copy_to``: An absolute or relative path (including the file name) to which the fixture file will be copied after dumpdata is executed. For example, you might use this to copy fixtures to Dropbox, an external drive, or network share.
- ``database``: The name of the database (in DATABASES) to use for the fixture. This may also be specified as ``db``.
- ``file_name``: The name of the fixture file. For example, ``examples.json``.
- ``natural_foreign``: Specified as ``yes`` or ``no``. When ``yes``, the ``--natural-foreign`` switch is passed to the ``dumpdata`` management command. Defaults to ``no``. This may also be specified as ``nfk``.
- ``natural_primary``: Specified as ``yes`` or ``no``. When ``yes``, the ``--natural-primary`` switch is passed to the ``dumpdata`` management command. Defaults to ``no``. This may also be specified as ``npk``.
- ``path``: The path to the fixture file (relative to ``manage.py``). For example: ``local/customers/fixtures``.
- ``readonly``: Specified as ``yes`` or ``no``. When ``yes``, the fixtures may only be loaded, but not dumped. Defaults to ``no``.
- ``settings``: The dotted path to the settings file. This causes the ``--settings``  switch to be passed to both the ``dumpdata`` and ``loaddata`` management commands.

.. tip::
    Settings may also be passed as a switch to the ``fixman`` commannd.

An example ``config.ini`` file:

.. code-block:: ini

    [lookups]
    comment = Validation data. Stored globally.
    path = ../deploy/fixtures
    readonly = yes

    [customers.Customer]
    file_name = examples.ini
    path = local/customers/fixtures

    [sales.CustomerOrder]
    file_name = examples.ini
    path = local/sales/fixtures

