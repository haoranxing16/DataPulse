class Analysis:
    def DataAnalysis(self,data:list[dict]):
        i = 0
        for dt in data:
            i += 1
            print(f"Group{i}")
            for k,v in dt.items():
                if v == "":
                    v = "/*None*/"
                print(f" {k}: {v}")
            print('\n')
    def Count(self,data:list[dict],index:str)->dict:
        try:
            if index not in [k for k in data[0]]:
                raise KeyError(f"Field '{index}' not found. Available fields: {list(data[0])}")
        except KeyError as e:
            print(e)
            exit(1)
        records = {}
        for dt in data:
            if dt[index] in records: 
                records[dt[index]] += 1
            else:
                records[dt[index]] = 1
        print(records)
        return records
    def CountAll(self,data:list[dict])->list[dict]:
        records = []
        for fst in data[0]:
            records.append({data[0][fst]:1})
        for dt in data[1:]:
            num = 0
            for dv in dt.values():
                if dv in records[num]:
                    records[num][dv] += 1
                else:
                    records[num][dv] = 1
        print(records)
        return records
    def FieldConstruction(self,data:list[dict],index:str)->list:
        field = []
        for dt in data:
            if index in dt:
                field.append(dt[index])
        return field
    def FieldAnalysis(self,field:list,index:str):
        records = []
        sum = 0
        for f in field:
            if isinstance(f,int|float):
                records.append(f)
                continue
            elif isinstance(f,str):
                try:
                    records.append(int(f))
                    continue
                except (ValueError,TypeError):
                    try:
                        records.append(float(f))
                        continue
                    except (ValueError,TypeError):
                        print("the field's type isn't format")
                        exit(1)
        if len(records) == 0:
                    print("the field is empty")
                    exit(1)
        print(f"Analysis the {index} field:")
        for val in records:
            sum += val
        print(f"count: {len(records)}")
        print(f"sum: {sum}")
        print(f"average: {sum / len(records)}")
        print(f"max: {max(records)}")
        print(f"min: {min(records)}")