from typing import Any, Dict, Optional, Union

import orjson
from pydantic import BaseModel


def _pydantic_serializer(obj: Any) -> Optional[Union[str, Dict[str, Any]]]:
    if isinstance(obj, BaseModel):
        return obj.model_dump(mode="json", exclude_unset=True, exclude_none=True)
    if isinstance(obj, Exception):
        text = obj.args[0] if len(obj.args) > 0 else "Unknown error"
        return f"{type(obj).__name__}: {text}"

    return None


def orjson_dumps(content: Any) -> bytes:
    return orjson.dumps(
        content,
        default=_pydantic_serializer,
        option=orjson.OPT_SERIALIZE_DATACLASS
        | orjson.OPT_SERIALIZE_UUID
        | orjson.OPT_NON_STR_KEYS,
    )
