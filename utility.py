from importlib import import_module

def load_engines():
    return None

def my_import(class_name):
    module_name = class_name.lower()
    module_object = import_module('.' + module_name, package='plugins')
    target_class = getattr(module_object, class_name)
    return target_class