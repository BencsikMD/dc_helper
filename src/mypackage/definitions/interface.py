



from dataclasses import dataclass, field
from mypackage.dc import BaseDC

@dataclass
class LocationProperties(BaseDC):
    """Location properties for a data source or sink."""

@dataclass
class Operation(BaseDC):

    mode: str = field(kw_only=True, default='overwrite')

@dataclass
class DataDefinition(BaseDC):

    location: LocationProperties = field(kw_only=True, default=None)
    operation: Operation = field(kw_only=True, default=None)
