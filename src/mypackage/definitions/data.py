



from dataclasses import dataclass, field

from mypackage.definitions.interface import DataDefinition
from mypackage.definitions.location import ADLSLocation
from mypackage.definitions.operation import ADLSOperation


@dataclass
class DCOne(DataDefinition):

    h: int
    i: int
    location: ADLSLocation = field(kw_only=True, default=None)
    operation: ADLSOperation = field(kw_only=True, default=None)

@dataclass
class DCTwo(DataDefinition):

    x: int
    y: int
    location: ADLSLocation = field(kw_only=True, default=None)
    operation: ADLSOperation = field(kw_only=True, default=None)
