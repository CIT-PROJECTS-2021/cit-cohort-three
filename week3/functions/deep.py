from typing import ChainMap


class DeepChainMap(ChainMap):
    'Variant of ChainMap that allows direct updates to inner scopes'

    def __setitem__(self, key, value):
        for scope in self.maps:
            if key in scope:
                scope[key] = value
                return
        raise KeyError(key)

    def __delitem__(self, key):
        for scope in self.maps:
            if key in scope:
                del scope[key]
                return
        raise KeyError(key)

    def __contains__(self, key):
        for scope in self.maps:
            if key in scope:
                return True
        return False


def deep_update(d, u):
    'Update dict d with dict u, recursively'
    for k, v in u.items():
        if isinstance(v, dict):
            d[k] = deep_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def deep_merge(*args):
    'Merge dicts recursively'
    result = {}
    for d in args:
        deep_update(result, d)
    return result


deep_chainmap = DeepChainMap()
deep_chainmap['a'] = 1