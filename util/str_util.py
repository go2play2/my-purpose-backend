# str_util.py

def get_value(obj, key):
    return '' if obj.get(key) is None else obj.get(key)


def custom_json_set(obj):
    if isinstance(obj, set):
        return list(obj)
    return obj
