********
Fixtures
********

.. code-block:: ini

    [app_label.ModelName]
    database = The name of the database (in DATABASES) to use for the fixture.
    file_name = The name of the file at the end of the path..
    group = The name of the group into which the fixture is organized. Used for filtering.
    path = path/to/fixtures
    readonly = yes|no

Suggested Groups

- initial
- examples
