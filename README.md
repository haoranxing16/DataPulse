# DataPulse

Command-line data cleaning tool supporting CSV, JSON, and XLSX formats.

## Function
 - Function 1 analysis    print all fields of every records
 - Function 2 count    Count the occurrences of values ​​for a specific field (-c) or for all fields (-a)
 - Function 3 fieldana    Analyze a specific field
 - Function 4 dedup     Remove duplicate records
 - Function 5 nullvalue    Handling null values ​​(deleting key-value pairs / deleting entire rows / filling with default values)
 - Function 6 delspace    Remove spaces (leading/trailing / all)
 - Function 7 numconvert    Converting Between Numeric and String Types

 ## Requirements
Python 3.11+

 ## Install
 ```powershell
 git clone https://github.com/haoranxing16/DataPulse.git
 cd datapulse
 python -m venv .venv
 ./.venv/scripts/activate
 pip install -e .
 ```

 ## Used
 ```powershell
 ./.venv/scripts/activate
 datapulse [-h|--help]
 datapulse analysis <filepath>
 datapulse count [-c|--count] <fieldname> <filepath>
 datapulse count [-a|--count-all] <filepath>
 datapulse fieldana <filepath> <fieldname>
 datapulse dedup <filepath>
 datapulse nullvalue [-p|--depairs] <filepath>
 datapulse nullvalue [-l|--delines] <filepath>
 datapulse nullvalue [-d|--default] <filepath> <--fillvalue>
 datapulse delspace [-s|--strip] <filepath>
 datapulse delspace [-a|--all] <filepath>
 datapulse numconvert [-s|--to-str] <fieldname> <filepath>
 datapulse numconvert [-i|--to-int] <fieldname> <filepath>
 ```

 ## Contribute
 Feel free to submit issues and PRs.

 ## License
 MIT