def null_value_delpairs(data:list[dict])->list[dict]:
    newdata = []
    for dt in data:
        nwdt = {dt:v for dt,v in dt.items() if v != ""}
        newdata.append(nwdt)
    data[:] = newdata
    return newdata

def null_value_dellines(data:list[dict])->list[dict]:
    return [dt for dt in data if all(v != "" for v in dt.values())]

def null_value_default(data:list[dict],defaultvalue:str|int)->list[dict]:
    for dt in data:
        for k,v in dt.items():
            if v == "":
                dt[k] = defaultvalue
    return data