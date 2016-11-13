#!/usr/bin/perl
#
# This script should read a file typically(?) named "<gelmanrubin.txt"
#

use warnings;

while(<>){
    my $burnin=0;
    if ($.==2){
	my @column=split /\s/, $_;
	if ($column[1]<200000){
	    print "CONVERGENCE\n";
	}
    }
}


