def pack(dt:dict)->frozenset:
    return frozenset(dt.items())

def package(data:list[dict])->set[frozenset]:
    mulsets = set()
    for dt in data:
        mulsets.add(pack(dt))
    return mulsets

def unpack(mulset:frozenset)->dict:
    return dict(mulset)

def unpackage(mulsets:set[frozenset])->list[dict]:
    data = []
    for mulset in mulsets:
        data.append(unpack(mulset))
    return data

def deduplication(data:list[dict])->list[dict]:
    return unpackage(package(data))