#!/usr/bin/perl

use warnings;

open(my $INFILE, "<gelmanrubin.txt");

while(<$INFILE>){
my $burnin=0;
if ($.==2){
my @column=split /\s/, $_;
if ($column[1]<200000){
print "CONVERGENCE\n";
}
}
}
close $INFILE;

