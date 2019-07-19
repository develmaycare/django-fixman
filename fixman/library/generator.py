# Imports

import logging
from ..constants import LOGGER_NAME

try:
    # noinspection PyPackageRequirements
    from django.apps import apps as django_apps
except ImportError:
    django_apps = None

log = logging.getLogger(LOGGER_NAME)

# Exports

__all__ = (
    "get_model",
)

# Functions


def get_fields(model):
    """Get the fields for the given model.

    :param model: The model class.
    :type model: django.db.models.Model

    :rtype: list
    :returns: A list of field instances.

    """
    a = list()
    # noinspection PyProtectedMember
    for field in model._meta.fields:
        a.append(field)

    return a


def get_model(name):
    """Get the named model.

    :param name: The name of the model in the form of ``app_label.ModelName``.
    :type name: str

    :rtype: django.db.models.Model | None

    """
    if django_apps is None:
        log.critical("Django is not installed.")
        return None

    try:
        return django_apps.get_model(name, require_ready=False)
    except ValueError as e:
        log.error("Model name must be in the form of app_label.ModelName: %s" % e)
    except LookupError as e:
        log.error("%s refers to a model that has not been installed: %s" % (name, e))
