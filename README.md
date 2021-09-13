# rpi4_gpio_atpg_stuck_at
Raspberry Pi 4 is used to drive ATPG stuck-at patterns to an IC. Python is used to drive the patterns and check for expected levels on the scan_out pins (4 chains in this example). A Perl script is used to parse the ATP pattern data into Python lists (I prefer to parse text files using Perl).
