

from dataclasses import dataclass

from mypackage.definitions.interface import Operation




@dataclass
class ADLSOperation(Operation):

    keys: list = None
    format: str = 'binary'
