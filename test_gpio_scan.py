#!/usr/bin/python

from gpio_scan        import gpio_scan
from complr_patterns  import * # this defines pattern_list 

gs = gpio_scan()
gs.load_and_compare_list( pat_name='scan_entry', pattern=list_se, shift=False )

for scan_pat in range(0,3504):
	gs.load_and_compare_list( pat_name=str(scan_pat), pattern=pattern_list[scan_pat], shift=True )

