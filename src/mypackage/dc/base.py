


from abc import ABC
from dataclasses import dataclass, asdict

import dacite

@dataclass
class BaseDC(ABC):

    def to_dict(self):
        # put customization here
        # dc_dict = asdict(self)
        # # Removes None values before returning dictionary
        # dc_dict = {k: v for k, v in dc_dict.items() if v is not None}
        return asdict(self)


    @classmethod
    def from_dict(cls, d: dict):
        # put customization here
        return dacite.from_dict(cls, d) if isinstance(d, dict) else d
