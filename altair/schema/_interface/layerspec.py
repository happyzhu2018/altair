# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject
from .config import Config
from .data import Data
from .transform import Transform
from .unitspec import UnitSpec


class LayerSpec(BaseObject):
    """Wrapper for Vega-Lite LayerSpec definition.
    
    Attributes
    ----------
    config: Config
        
    data: Data
        
    description: Unicode
        
    layers: List(UnitSpec)
        
    name: Unicode
        
    transform: Transform
        
    """
    config = T.Instance(Config, allow_none=True, default_value=None)
    data = T.Instance(Data, allow_none=True, default_value=None)
    description = T.Unicode(allow_none=True, default_value=None)
    layers = T.List(T.Instance(UnitSpec), allow_none=True, default_value=None)
    name = T.Unicode(allow_none=True, default_value=None)
    transform = T.Instance(Transform, allow_none=True, default_value=None)
    
    def __init__(self, config=None, data=None, description=None, layers=None, name=None, transform=None, **kwargs):
        kwds = dict(config=config, data=data, description=description, layers=layers, name=name, transform=transform)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(LayerSpec, self).__init__(**kwargs)