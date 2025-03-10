
import logging

from mypackage.dc._internal import identify_dc, register_local_dcs
from mypackage.dc.base import BaseDC
from mypackage.dc.serial import dumps, loads

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
