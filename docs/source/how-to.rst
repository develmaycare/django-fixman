.. _how-to:

******
How To
******

Scan for Existing Fixtures
==========================

The ``fixman init`` command may be used with the ``-S`` switch to scan for fixture files.

.. important::
    The scan finds the fixture files in the order provided by the operating system and file structure. Due to foreign keys, this is probably *not* the order in which the fixtures should be loaded. Change the order after writing to the ``config.ini`` file.

Specify Settings to Use When Dumping or Loading Fixtures
========================================================

If specific settings are required you may specify them with the ``--settings`` switch. This will cause all fixture operations to occur with those settings.

.. code-block:: bash

    fixman dumpdata --settings=dotted.path.to.alternative.settings

You may also specify settings in the ``config.ini`` file:

.. code-block:: ini

    [lookups]
    settings = main.shared_database_settings

    [todos]
    ; will use default settings

Use Fixture Groups
==================

It is possible to specify a logical group into which fixtures are organized. This is done by adding ``:group_name`` to the section. The ``-G`` or ``--group-name`` switches may be used to filter by group.

Specifying a grouping:

.. code-block:: ini

    [app_label.ModelName:group_name]
    ; ...

This allows fixtures for the same app or model to be specified multiple times for different purposes; defaults, examples, or by deployment environment.
