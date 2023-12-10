from typing import List, Dict, Any
from pymongo.cursor import Cursor

def format_list(mongo_result: Cursor) -> List[Dict[str, Any]]:
    new_list = []
    for item in mongo_result:
        new_item = {'id': str(item.pop('_id'))}
        new_item.update(item)
        new_list.append(new_item)
    return new_list

def sanitize_value(value):
    import bleach
    if isinstance(value, str):
        # Sanitizar solo si el valor es una cadena de texto
        return bleach.clean(value, strip=True)
    elif isinstance(value, dict):
        # Recursivamente sanitizar diccionarios anidados
        return sanitize_dict(value)
    elif isinstance(value, list):
        # Recursivamente sanitizar listas
        return [sanitize_value(item) for item in value]
    else:
        # Mantener valores que no son cadenas de texto sin cambios
        return value

def sanitize_dict(input_dict):
    sanitized_dict = {}
    for key, value in input_dict.items():
        sanitized_dict[key] = sanitize_value(value)

    return sanitized_dict

def clean_dict(input_dict: dict):
    if isinstance(input_dict, dict):
        return {k: clean_dict(v) for k, v in input_dict.items() if v is not None}
    else:
        return input_dict
