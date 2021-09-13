# rpi4_gpio_atpg_stuck_at
Raspberry Pi 4 is used to drive ATPG stuck-at patterns to an IC. Python is used to drive the patterns and check for expected levels on the scan_out pins (4 chains in this example). A Perl script is used to parse the ATP pattern data into Python lists (I prefer to parse text files using Perl).

The Python pattern file "complr_patterns.py.gz" needs to be decompressed. The ATP pattern file "scan_patterns/complr.atp.gz" was also compressed to save repository space. The Python pattern file complr_patterns.py was created using the scripts/parse_scan.pl script with the complr.atp file as input.

In this example each chain has a length of about 156 bits. Four chains are driven at once, which gives an effective length of 624 bits. 3503 pattern are used, which comes to about 2.2 million bits. It takes about 8 seconds to run these patterns. It takes much longer to run on a RPi3 (maybe 10 times), but the patterns would need to be divided into chunks as the 1GB RAM on the RPi3 becomes an issue. Just use the RPi4 2GB or higher.

Why run stuck-at patterns on the lab bench? If you need to implement an ATE-to-bench with scan, this is a very low-cost method. If you are supporting a test chip with no ATE support, this is a very low-cost method.

As you look at the gpio_scan.py class, you will see that the scan clock pin is controlled just like all the other gpio pins. As long as your predicted maximum scan clock frequency is less than the effective RPi4 bit-banging of the scan clock pin, you should not need to add any addition delay.

If your patterns are very large, perhaps NumPy could be used to improve my pattern list file so that it fits into less RAM (I believe each bit is presently stored as an integer).
