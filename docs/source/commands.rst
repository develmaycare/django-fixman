.. _commands:

********
Commands
********

.. important::
    If is assumed that the ``fixman`` command is executed from project root.

dumpdata
========

Dump fixture data.

.. code-block:: text

    usage: fixman dumpdata [-h] [-A= APP_NAMES] [-D] [-G= GROUP_NAMES] [-M= MODEL_NAMES] [-P= PATH] [-p] [-r= PROJECT_ROOT] [-s= SETTINGS]

    optional arguments:
      -h, --help            show this help message and exit
      -A= APP_NAMES, --app-name= APP_NAMES
                            Only work with this app. May be used multiple times.
      -D, --debug           Enable debug output.
      -G= GROUP_NAMES, --group-name= GROUP_NAMES
                            Only work with this group. May be used multiple times.
      -M= MODEL_NAMES, --model-name= MODEL_NAMES
                            Only work with this model. May be used multiple times.
      -P= PATH, --path= PATH
                            The path to the fixtures INI file. Default: deploy/fixtures/config.ini
      -p, --preview         Preview the commands.
      -r= PROJECT_ROOT, --project-root= PROJECT_ROOT
                            The path to the project.
      -s= SETTINGS, --settings= SETTINGS
                            The dotted path to the Django settings file.


init
====

Initialize fixture configuration.

.. code-block:: text

    usage: fixman init [-h] [-D] [-p] [-r= PROJECT_ROOT]

    optional arguments:
      -h, --help            show this help message and exit
      -D, --debug           Enable debug output.
      -p, --preview         Preview the commands.
      -r= PROJECT_ROOT, --project-root= PROJECT_ROOT
                            The path to the project.


inspect
=======

Display fixtures.

.. code-block:: text

    usage: fixman inspect [-h] [-A= APP_NAMES] [-D] [-G= GROUP_NAMES] [-M= MODEL_NAMES] [-P= PATH] [-p] [-r= PROJECT_ROOT] [-s= SETTINGS]

    optional arguments:
      -h, --help            show this help message and exit
      -A= APP_NAMES, --app-name= APP_NAMES
                            Only work with this app. May be used multiple times.
      -D, --debug           Enable debug output.
      -G= GROUP_NAMES, --group-name= GROUP_NAMES
                            Only work with this group. May be used multiple times.
      -M= MODEL_NAMES, --model-name= MODEL_NAMES
                            Only work with this model. May be used multiple times.
      -P= PATH, --path= PATH
                            The path to the fixtures INI file. Default: deploy/fixtures/config.ini
      -p, --preview         Preview the commands.
      -r= PROJECT_ROOT, --project-root= PROJECT_ROOT
                            The path to the project.
      -s= SETTINGS, --settings= SETTINGS
                            The dotted path to the Django settings file.


loaddata
========

Load fixture data.

.. code-block:: text

    usage: fixman loaddata [-h] [-S] [-A= APP_NAMES] [-D] [-G= GROUP_NAMES] [-M= MODEL_NAMES] [-P= PATH] [-p] [-r= PROJECT_ROOT] [-s= SETTINGS]

    optional arguments:
      -h, --help            show this help message and exit
      -S, --script          Export to a bash script.
      -A= APP_NAMES, --app-name= APP_NAMES
                            Only work with this app. May be used multiple times.
      -D, --debug           Enable debug output.
      -G= GROUP_NAMES, --group-name= GROUP_NAMES
                            Only work with this group. May be used multiple times.
      -M= MODEL_NAMES, --model-name= MODEL_NAMES
                            Only work with this model. May be used multiple times.
      -P= PATH, --path= PATH
                            The path to the fixtures INI file. Default: deploy/fixtures/config.ini
      -p, --preview         Preview the commands.
      -r= PROJECT_ROOT, --project-root= PROJECT_ROOT
                            The path to the project.
      -s= SETTINGS, --settings= SETTINGS
                            The dotted path to the Django settings file.
