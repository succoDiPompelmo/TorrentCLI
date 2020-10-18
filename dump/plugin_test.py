import pkgutil
import inspect 
import sys
from pathlib import Path
from importlib import import_module

for (_, name, _) in pkgutil.iter_modules(['./plugins']):
    imported_module = import_module('.' + name, package='plugins')

def dynamic_import(class_name):
    
    module_name = class_name.lower()
    module_object = import_module('.' + module_name, package='plugins')
    target_class = getattr(module_object, class_name)
    return target_class