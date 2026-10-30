def del_strip_spaces(data:list[dict])->list[dict]:
    for dt in data:
        for k,v in dt.items():
            if isinstance(v,str):
                 dt[k] = v.strip()
    return data

def del_all_spaces(data:list[dict])->list[dict]:
    for dt in data:
            for k,v in dt.items():
                if isinstance(v,str):
                    dt[k] = "".join(s for s in v if not s==" ")
    return data