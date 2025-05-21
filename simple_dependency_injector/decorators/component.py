__author__ = "Willian Antonio"

from simple_dependency_injector.core.component import ContainerConfig


def singleton(is_lazy: bool = False):
    def inner_singleton(cls):
        @classmethod
        def container_config(cls) -> ContainerConfig:
            return {
                "injected_type": "singleton",
                "is_lazy": is_lazy,
            }

        cls.container_config = container_config
        return cls

    return inner_singleton


def factory():
    def inner_factory(cls):
        @classmethod
        def container_config(cls) -> ContainerConfig:
            return {
                "injected_type": "factory",
                "is_lazy": False,
            }

        cls.container_config = container_config
        return cls

    return inner_factory
