obj = {"a":{"b":{"c":"d"}}}
key = "a/b/c"

def getValue(obj, key):
    keys = key.split('/')
    for k in keys:
        try: 
            obj = obj.get(k,{})
        except KeyError:
            return None
    return obj

result = getValue(obj, key)
print(result)
