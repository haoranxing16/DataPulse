intdict = { "1":1,"2":2,"3":3,"4":4,"5":5,
               "6":6,"7":7,"8":8,"9":9,"0":0 }

def is_exchange_number(module) -> bool:
    return isinstance(module, str) and module != "" and all(ch in intdict for ch in module)

def exchange_to_number(module:str)->int:
    try:
        if not isinstance(module,str):
            raise TypeError("The type of arrgument is not str")
    except TypeError as e:
        print(e)
    if "." not in module:
        return int(module)
    else:
        return float(module)
def numconvert_to_str(data:list[dict],index:str)->list[dict]:
    for dt in data:
        if isinstance(dt[index],int):
            dt[index] = str(dt[index])
    return data

def numconvert_to_int(data:list[dict],index:str)->list[dict]:
    for dt in data:
        if is_exchange_number(dt[index]):
            dt[index] = exchange_to_number(dt[index])
    return data