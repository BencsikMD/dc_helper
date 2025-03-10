

from dataclasses import asdict, is_dataclass, fields
from datetime import datetime
import json
from typing import Any, Literal

import dacite

from mypackage.dc._internal import identify_dc

SENTINEL = Literal['SENTINEL']

def _dict_factory(obj: list[tuple[str, Any]]):
    """Convert a list of tuples to a dictionary."""
    # Removes None values before returning dictionary

    # for k, v in obj:
    #     if is_dataclass(v)
    #     if v is not None and is_dataclass(v):

    # print(obj)
    return {k: v for k, v in obj if v is not None}

def _encode_json(obj: object):
    """Returns a serializable object.
    
    Takes in an object that cannot be converted using
    the standard JSON encoder. 
    """
    if is_dataclass(obj):
        # return obj.to_dict() if hasattr(obj, 'to_dict') else asdict(obj, dict_factory=_dict_factory)
        # dc_dict = asdict(obj, dict_factory=_dict_factory)
        # for field in fields(obj):
        #     # if field.type
        #     if field.default == dc_dict.get(field.name, SENTINEL):
        #         del dc_dict[field.name]
        # return dc_dict
        return asdict(obj, dict_factory=_dict_factory)
    if isinstance(obj, datetime):
        return obj.isoformat()

    raise TypeError(f'No option to JSON serialze type: {type(obj).__name__}.')

def dumps(data: dict, indent: int = 4) -> str:
    """Package helper method to convert a dictionary to a JSON string."""
    return json.dumps(data, default=_encode_json, indent=indent)

def _decode_json(obj: object):
    """Called for every object encountered.
    
    Return a specific object or pass the dictionary through.
    """
    dc = identify_dc(obj)
    if is_dataclass(dc):
        return obj.from_dict() if hasattr(obj, 'from_dict') else dacite.from_dict(dc, obj)

    return obj

def loads(s: str):
    """Package helper method to convert a JSON string to a Dictionary."""
    return json.loads(s, object_hook=_decode_json)
