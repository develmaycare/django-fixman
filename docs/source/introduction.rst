.. _introduction:

************
Introduction
************

Overview
========

The Django Fixture Manager, or *fixman*, is a command line tool for more easily managing large numbers of fixtures across an entire project. Developers or admins may use the tool to more easily load or dump Django fixtures under various circumstances.

Fixtures may be located globally for a project, within a project's apps, or both. Additionally, fixtures may organized into groups such as "examples" or "defaults" to help with development and deployments.

Concepts
========

A fixture configuration defines how fixtures may be loaded or dumped and is the primary means of managing fixtures using the ``fixman`` command.

The ``fixman`` command loads the configuration to dump, load or inspect fixtures based on the options you've provided.

The ``deploy/fixtures/config.ini`` file contains instructions for how fixtures may be exported or imported. Each section represents either an app or a specific model. For example, a customers app is managed with  ``[customers]`` while the customer model would be specified as ``[customers.Customer]``.

See :ref:`getting-started` and :ref:`how-to`.

License
=======

Django Fixman is released under the MIT license.
