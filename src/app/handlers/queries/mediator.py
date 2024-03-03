from typing import cast

from src.app.mediator.base import CT, RT, Mediator


class QueryMediator(Mediator):
    async def __call__(self, query: CT) -> RT:
        return await self.query(query)

    async def query(self, query: CT) -> RT:
        handler = self._resolve(self._dependencies[type(query)])
        return cast(RT, await handler(query))
