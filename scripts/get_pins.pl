#!/usr/bin/perl
@pins = ();
while (<>) {
	if (/^vector/) { @pin_array = / ([a-zA-Z0-9_]+)/g; }
}
foreach $pin (@pin_array) {
	print "$pin\n";
}
