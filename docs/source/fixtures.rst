********
Fixtures
********

Config File
===========

The ``fixtures/config.ini`` file contains instructions for how fixtures may be exported or imported. Each section represents either an app or a specific model. For example, a customers app is managed with  ``[customers]`` while the customer model would be specified as ``[customers.Customer]``.

Fixture Files
-------------

When a model is specified, the default location of fixtures files is ``<project_root>/fixtures/<app_label>/<model_name>.json``. The ``<model_name>`` is always singular and lower case. If no model is given, the default path is ``<project_root>/fixtures/<app_label>/initial.json``

The ``file_name`` and ``path`` options (below) may be used to override the default.

Additional Options
------------------

Simply specifying a section is enough to dump and load fixture files. However, there are some additional options that may be specified with the section to control these behaviors.

- ``comment``: An optional comment regarding the fixtures.
- ``copy_to``: An absolute or relative path (including the file name) to which the fixture file will be copied. For example, you might use this to copy fixtures to Dropbox, an external drive, or network share.
- ``database``: The name of the database (in DATABASES) to use for the fixture. This may also be specified as ``db``.
- ``file_name``: The name of the fixture file. For example, ``examples.json``.
- ``natural_foreign``: Specified as ``yes`` or ``no``. When ``yes``, the ``--natural-foreign`` switch is passed to the ``dumpdata`` management command. Defaults to ``no``. This may also be specified as ``nfk``.
- ``natural_primary``: Specified as ``yes`` or ``no``. When ``yes``, the ``--natural-primary`` switch is passed to the ``dumpdata`` management command. Defaults to ``no``. This may also be specified as ``npk``.
- ``path``: The path to the fixture file (relative to ``manage.py``). For example: ``local/customers/fixtures``.
- ``readonly``: Specified as ``yes`` or ``no``. When ``yes`` the fixtures may only be loaded, but not dumped. Defaults to ``no``.
- ``settings``: The dotted path to the settings file. This causes the ``--settings``  switch to be passed to both the ``dumpdata`` and ``loaddata`` management commands.

.. tip::
    Settings may also be passed as a switch to the ``fixman`` commannd.

An example ``config.ini`` file:

.. code-block:: ini

    [lookups]
    comment = Validation data.
    readonly = yes

    [customers.Customer]
    file_name = examples.ini
    path = local/customers/fixtures

    [sales.CustomerOrder]
    file_name = examples.ini
    path = local/sales/fixtures

Specifying a Fixture Group
--------------------------

It is possible to specify a logical group into which fixtures are organized. This is done by adding ``:group_name`` to the section. The ``-G`` or ``--group-name`` may be used to filter by group.

Specifying a grouping:

.. code-block:: ini

    [app_label.ModelName:group_name]
    ; ...

This allows fixtures for the same app or model to be specified multiple times for different purposes; defaults, examples, or by deployment environment.
