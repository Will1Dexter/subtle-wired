__author__ = 'Willian Antonio'

from simple_dependency_injector.core.injector import InjectedItem, Injector


def inject(func):
    if func.__name__ == '__init__':

        def init_wrapper(self):
            return InjectedItem.init_wrapper(func, self, Injector())

        return init_wrapper
    else:

        def set_wrapper(self, value):
            raise AttributeError(
                f"Cannot set attribute '{func.__name__}' on '{self.__class__.__name__}'. "
                'This property is read-only (populated by the container)!'
            )

        def get_wrapper(self):
            return InjectedItem.get_wrapper(func, self, Injector())

        return property(fget=get_wrapper, fset=set_wrapper)
