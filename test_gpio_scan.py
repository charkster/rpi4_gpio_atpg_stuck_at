#!/usr/bin/python
import json
from gpio_scan                       import gpio_scan
from complr_patterns_scan_entry_only import * 

with open('pattern_list.json', 'r') as filehandle:
	pattern_list = json.load(filehandle)

gs = gpio_scan()
gs.load_and_compare_list( pat_name='scan_entry', pattern=list_se, shift=False )

for scan_pat in range(0,len(pattern_list)):
	gs.load_and_compare_list( pat_name=str(scan_pat), pattern=pattern_list[scan_pat], shift=True )
