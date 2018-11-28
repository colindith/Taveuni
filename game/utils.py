import logging
import importlib

from django.core.cache import cache

logger = logging.getLogger(__name__)


def load_class(classpath):
    try:
        module_name, class_name = classpath.rsplit('.', 1)
        cls = getattr(importlib.import_module(module_name), class_name)
    except Exception as e:
        logger.error(
            f'Object has an invalid processor or processor '
            f'implementation. Given classpath is {classpath}. {e}'
        )
        return None

    return cls
