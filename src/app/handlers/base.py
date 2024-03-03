import abc
from typing import Generic, TypeVar

from src.app.common.interfaces.handler import Handler

QueryType = TypeVar("QueryType")
ResultType = TypeVar("ResultType")


class BaseHandler(Handler, Generic[QueryType, ResultType]):
    async def __call__(self, query: QueryType) -> ResultType:
        return await self.handle(query)

    @abc.abstractmethod
    async def handle(self, query: QueryType) -> ResultType:
        raise NotImplementedError
