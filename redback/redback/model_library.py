from inspect import getmembers, isfunction
from . import models

_functions_list = [o for o in getmembers(models) if isfunction(o[1])]
model_dict = {f[0]: f[1] for f in _functions_list}