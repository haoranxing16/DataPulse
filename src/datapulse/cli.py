import argparse
import json
import sys
from pathlib import Path
from datapulse.parse import parse, save
from datapulse.dataanalysis import Analysis
from datapulse.cleaning.deduplication import deduplication
from datapulse.cleaning.nullvalue import null_value_delpairs
from datapulse.cleaning.nullvalue import null_value_dellines
from datapulse.cleaning.nullvalue import null_value_default
from datapulse.cleaning.surplusspace import del_strip_spaces
from datapulse.cleaning.surplusspace import del_all_spaces
from datapulse.cleaning.numberconversion import numconvert_to_str
from datapulse.cleaning.numberconversion import numconvert_to_int

def main():
    parser = argparse.ArgumentParser(description = "File tool")
    subparsers = parser.add_subparsers(dest = "command",required = True)

    common = argparse.ArgumentParser(description = "common",add_help = False)
    common.add_argument("path",type = Path,help = "the path of file.")

    p_analysis = subparsers.add_parser("analysis",parents = [common],help = "analysis datas.")
    p_count = subparsers.add_parser("count",parents = [common],help = "count records.")
    g = p_count.add_mutually_exclusive_group(required = True)
    g.add_argument("-c","--count",type = str,help = "count field records that in data.")
    g.add_argument("-a","--count-all",action = "store_true",help = "count all data records.")
    p_fieldana = subparsers.add_parser("fieldana",parents = [common],help = "analysis field.")
    p_fieldana.add_argument("index",type = str)
    p_dedup = subparsers.add_parser("dedup",parents = [common],help = "deduplication.")
    p_nullvalue = subparsers.add_parser("nullvalue",parents = [common],help = "null value.")
    g2 = p_nullvalue.add_mutually_exclusive_group(required = True)
    g2.add_argument("-p","--depairs",action = "store_true")
    g2.add_argument("-l","--delines",action = "store_true")
    g2.add_argument("-d","--default",nargs = "?",const = "/*None*/")
    p_delspace = subparsers.add_parser("delspace",parents = [common],help = "delete spaces.")
    g3 = p_delspace.add_mutually_exclusive_group(required = True)
    g3.add_argument("-s","--strip",action = "store_true",help = "Remove leading and trailing spaces.")
    g3.add_argument("-a","--all",action = "store_true",help = "Remove all spaces.")
    p_convert = subparsers.add_parser("numconvert",parents = [common],help = "number convert.")
    p_convert.add_argument("index",type = str)
    g4 = p_convert.add_mutually_exclusive_group(required = True)
    g4.add_argument("-i","--to-int",action = "store_true")
    g4.add_argument("-s","--to-str",action = "store_true")

    p_analysis.set_defaults(func = dataanalysis)
    p_count.set_defaults(func = count)
    p_fieldana.set_defaults(func = fieldanalysis)
    p_dedup.set_defaults(func = dedup)
    p_nullvalue.set_defaults(func = nullvalue)
    p_delspace.set_defaults(func = delspace)
    p_convert.set_defaults(func = convert)

    args = parser.parse_args()
    try:
        args.func(args)
    except (Exception) as e:
        print(f"Error: {e.args[0]}", file=sys.stderr)
        return 1
    return 0

def count(args):
    data = parse(args.path)
    if args.count is not None:
        Analysis().Count(data,args.count)
    else:
        Analysis().CountAll(data)

def nullvalue(args):
    data = parse(args.path)
    if args.depairs:
        save(args.path,null_value_delpairs(data))
    if args.delines:
        save(args.path,null_value_dellines(data))
    save(args.path,null_value_default(data,args.default))

def delspace(args):
    data = parse(args.path)
    if args.strip:
        save(args.path,del_strip_spaces(data))
    if args.all:
        save(args.path,del_all_spaces(data))

def convert(args):
    data = parse(args.path)
    if args.to_int:
        save(args.path,numconvert_to_int(data,args.index))
    if args.to_str:
        save(args.path,numconvert_to_str(data,args.index))

def fieldanalysis(args):
    data = parse(args.path)
    Analysis().FieldAnalysis(Analysis().FieldConstruction(data,args.index),args.index)

def dataanalysis(args):
    data = parse(args.path)
    Analysis().DataAnalysis(data)

def dedup(args):
    data = parse(args.path)
    result = deduplication(data)
    with open(args.path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


if __name__ == "main":
    sys.exit(main())