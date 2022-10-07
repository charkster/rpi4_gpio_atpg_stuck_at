#!/usr/bin/perl
$start_pattern = 0;
$pattern_count = 0;
$pin_count     = 0;
$pattern_list = "list_0";

while(<>) {
	if (/^vector/) { @pin_name_array = / ([a-zA-Z0-9_]+)/g; } # this is an array containing 
	if (/^ >/) { @pin_values = / ([HLX10]{1})/g;              # all pattern data begins with this
		$start_pattern = 1; 
		push @pin_value_array, [@pin_values]; # using square brackets ensures that an array is pushed into the array
	}
	elsif (/^\/\/\"pattern ([0-9]+)\"/ && $start_pattern == 1) {
		$start_pattern = 0;
		$pattern_count = $1 - 1;
		if ( $pattern_count == -1 ) { $pattern_count = "se"; }
		print "#Pattern $pattern_count\n";
		$pin_count = 0;
		foreach my $pin_name (@pin_name_array) {
			print sprintf("%-20s", "list_" . $pin_name . "_" . $pattern_count); print " = [ ";
			$first_comma = 1;
			foreach my $pin_values (@pin_value_array) {
				if ($first_comma == 0) { print ", "; }
				$first_comma = 0;
				if ((@$pin_values[$pin_count] ne '0') && (@$pin_values[$pin_count] ne '1')) { print "\'@$pin_values[$pin_count]\'"; }
				else {                                                                        print  " @$pin_values[$pin_count] ";   }
			}
			print " ]\n";
            $pin_count = $pin_count + 1;
		}
		@pin_value_array = ();
		print sprintf("%-20s", "list_" . $pattern_count); print " = [ ";
		foreach my $pin (@pin_name_array) {
			print "list_" . $pin . "_" . $pattern_count . ", "; }
		print " ]\n";
		if ($pattern_count != "se") { $pattern_list .= ", list_" . $pattern_count; }
	}
}
print "\npattern_list = [ " . $pattern_list . " ]\n";
print "import json\n";
print "with open('pattern_list.json', 'w') as filehandle:\n";
print "    json.dump(pattern_list, filehandle)";
