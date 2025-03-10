
from dataclasses import asdict, is_dataclass
from datetime import datetime
import json

from mypackage.dc import register_local_dcs

from mypackage.definitions.interface import LocationProperties, Operation, DataDefinition
from mypackage.definitions.data import DCOne, DCTwo
from mypackage.definitions.location import ADLSLocation
from mypackage.definitions.operation import ADLSOperation

register_local_dcs(globals())
