from typing import cast

from src.app.mediator.base import CT, RT, Mediator


class CommandMediator(Mediator):
    async def __call__(self, command: CT) -> RT:
        return await self.query(command)

    async def query(self, command: CT) -> RT:
        handler = self._resolve(self._dependencies[type(command)])
        return cast(RT, await handler(command))
