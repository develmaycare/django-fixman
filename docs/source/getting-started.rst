.. _getting-started:

***************
Getting Started
***************

System Requirements
===================

Python 3.6 or later is required. It is assumed that a Django project is set up and configured.

Install
=======

To install:

.. code-block:: bash

    pip install git+https://github.com/develmaycare/django-fixman

Configuration
=============

To initialize a fixture configuration, go to your project's root and run: ``fixman init``

Examples
========

Fixtures to be managed with fixman are specified in ``deploy/fixtures/config.ini``. Each section of the INI represents a different fixture.

A minimal fixture requires only a section, like ``[app_name]``. This will work with all models in the app. To specify specific models, the section takes the form of ``[app_name.ModelName]``.

See :ref:`topics` for more information.

Next Steps
==========

1. Explore the various sub-commands using ``-h``. See :ref:`commands`.
2. Check out the various configuration options. See :ref:`topics`.

Resources
=========

- Django document on `providing initial data for models`_.

.. _providing initial data for models: https://docs.djangoproject.com/en/stable/howto/initial-data/

FAQs
====

Have a question? `Just ask`_!

.. _Just ask: https://develmaycare.com/contact/?support=1&product=Fixman
