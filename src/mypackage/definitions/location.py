

from dataclasses import dataclass

from mypackage.definitions.interface import LocationProperties



@dataclass
class ADLSLocation(LocationProperties):
    
    adls_resource_name: str
    adls_container: str
    adls_path: str = None
    adls_file_name: str = None
    encoding: str = 'utf-8'
