
import logging

import inspect
from dataclasses import is_dataclass
from typing import Type, Dict

from dacite import (
    from_dict,
    Config,
    MissingValueError,
    WrongTypeError,
    UnionMatchError,
    UnexpectedDataError
)

logger = logging.getLogger(__name__)

_REGISTERED_DC: Dict[str, Type] = {}

def register_dc(dc: Type):
    """Register a Dataclass in order to auto identify it."""
    _REGISTERED_DC.update({dc.__name__: dc})

def register_local_dcs(module):
    """Register all Dataclasses in a module."""
    # dataclasses = []
    if not isinstance(module, dict):
        module = dict(inspect.getmembers(module))
    for _, obj in module.items():
        if inspect.isclass(obj) and is_dataclass(obj):
            register_dc(obj)

def identify_dc(d: dict) -> Type | dict:
    """Identify a Dataclass type from a dictionary."""
    for _, dc in _REGISTERED_DC.items():
        try:
            from_dict(dc, d,Config(strict=True, strict_unions_match=True))
            return dc
        except (MissingValueError, WrongTypeError, UnionMatchError, UnexpectedDataError) as e:
            if e.__class__.__name__ == 'MissingValueError':
                logger.debug('MissingValueError: %s', e)

    return d
