__author__ = "Willian Antônio"

from abc import ABC

from simple_dependency_injector.core.component import (
    ContainerComponent,
)
from simple_dependency_injector.core.injector import Injector


class Container(ABC):
    implementations: list[ContainerComponent] = []

    def startup(self):
        for impl in self.__class__.implementations:
            if not hasattr(impl, "container_config"):
                raise AttributeError(
                    f"The class '{impl.__name__}' must be decorated with a singleton or factory to be used in the container!"
                )

            config = impl.container_config()
            Injector().upsert_implementation(
                impl,
                injected_type=config.get("injected_type", "singleton"),
                is_lazy=config.get("is_lazy", False),
            )

        Injector().make_all_instances()
