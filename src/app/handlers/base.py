from typing import Generic, TypeVar

from src.app.common.interfaces.handler import Handler

RequestType = TypeVar("RequestType")
DTOType = TypeVar("DTOType")


class BaseHandler(Handler, Generic[RequestType, DTOType]):
    async def __call__(self, query: RequestType) -> DTOType:
        return await self.handler(query)
    
    async def handler(self, query: RequestType) -> DTOType:
        ...
