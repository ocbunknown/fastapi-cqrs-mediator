import abc
from typing import Callable, Type, TypeVar

from src.app.common.interfaces.handler import Handler

HandlerType = TypeVar("HandlerType", bound=Handler)
CT = TypeVar("CT")
RT = TypeVar("RT")


class Mediator(abc.ABC):
    def init(self) -> None:
        """Initialize the Mediator object by setting up dependencies dictionary."""
        self._dependencies = {}

    @abc.abstractmethod
    async def __call__(self, query: CT) -> RT:
        """Process the query object and return the result.

        Args:
        ----
            query (CT): The query object to be processed.

        Returns:
        -------
            RT: The result of processing the query.

        """
        raise NotImplementedError

    def register(
        self,
        query: Type[CT],
        handler_factory: Callable[..., HandlerType],
    ) -> None:
        """Register a handler factory for a specific query type.

        Args:
        ----
            query (Type[CT]): The type of query to register the handler for.
            handler_factory (Callable[..., HandlerType]): The factory function that creates a handler for the query type.

        """
        self._dependencies[query] = handler_factory

    @staticmethod
    def _resolve(
        handler_factory: Callable[..., HandlerType],
    ) -> HandlerType:
        """Resolve the handler function for a given query.

        Args:
        ----
            handler_factory (Callable[..., HandlerType]): The factory function that creates a handler instance.

        Returns:
        -------
            HandlerType: The created handler instance.

        """
        return handler_factory()
