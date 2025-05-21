__version__ = '1.0.0'
__author__ = 'Willian Antonio'

from .container import factory, singleton
from .injection import inject, inject_property

__all__ = [
    'singleton',
    'factory',
    'inject',
    'inject_property',
]
