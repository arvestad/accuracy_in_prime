#!/usr/bin/perl

use warnings;

open(my $INFILE, "<burninfile.txt");
open(my $OUTFILE, ">burninvalues.txt");

while(<$INFILE>){
my $burnin=0;
if ($_=~/.*\"DuplicationRate".*\d+/){
my @column=split /\s/, $_;
print $OUTFILE "$column[12]\n";
}
elsif($_=~/.*\"LossRate".*\d+/){
my @column=split /\s/, $_;
print $OUTFILE "$column[12]\n";
}
elsif($_=~/.*\"EdgeRateMean".*\d+/){
my @column=split /\s/, $_;
print $OUTFILE "$column[12]\n";
}
}
close $INFILE;
close $OUTFILE;

open(my $INFILE2, "<burninvalues.txt");
open(my $OUTFILE2, ">burnin.txt");
my $burnin=0;
while(<$INFILE2>){
if($_>$burnin){
$burnin=$_;
}
}
print $OUTFILE2 $burnin;
close $INFILE2;
close $OUTFILE2;