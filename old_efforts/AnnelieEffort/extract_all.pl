#!/usr/bin/perl

use warnings;

open(my $INFILE, "<8vmcmc_true/vmcmc_true.txt");
open(my $OUTFILE, ">10analysis/true_prob_trees.txt");
while(<$INFILE>) {
    if($_=~/.+\"Newick".+/){
	my @column=split /\s/, $_;
	print $OUTFILE "$column[5]\n";
    }
    elsif($_=~/.+\"Posterior Distribution".+/){
	my @column=split /\s/, $_;
	print $OUTFILE "$column[6]\t";
    }
}
close $INFILE;
close $OUTFILE;

for (my $count=6; $count>=1; $count--){
    open(my $INFILE1, "<9vmcmc_false/vmcmc_false_$count.txt");
    open(my $OUTFILE1, ">10analysis/false_prob_trees_$count.txt");
    while(<$INFILE1>) {
	if($_=~/.+\"Newick".+/){
	    my @column=split /\s/, $_;
	    print $OUTFILE1 "$column[5]\n";
	}
	elsif($_=~/.+\"Posterior Distribution".+/){
	    my @column=split /\s/, $_;
	    print $OUTFILE1 "$column[6]\t";
	}
    }
    close $INFILE1;
    close $OUTFILE1;
}

open(my $INFILE2, "<10analysis/true_prob_trees.txt");
open(my $OUTFILE2, ">10analysis/true_MAP.newick");
while (<$INFILE2>) {
    my @column = split /\t/, $_;
    if ($.==1){
	print $OUTFILE2 "$column[1]";
    }
}
close $INFILE2;
close $OUTFILE2;

for(my $count=6; $count>=1; $count--){
    open(my $INFILE3, "<10analysis/false_prob_trees_$count.txt");
    open(my $OUTFILE3, ">10analysis/false_MAP_$count.newick");
    while (<$INFILE3>) {
	my @column = split /\t/, $_;
	if ($.==1){
	    print $OUTFILE3 "$column[1]";
	}
    }
    close $INFILE3;
    close $OUTFILE3;
}

for (my $count=7; $count>=1; $count--){
    open(my $INFILE4, "<10analysis/true_prob_trees.txt");
    while (<$INFILE4>) {
	if($.==$count){
	    my @column1 = split /\t/, $_;
	    $trueprob=$column1[0];
	    $findtree=$column1[1];
	}
    }
    close $INFILE4;

    for ($innercount=6; $innercount>=1; $innercount--){
	open(my $INFILE5, "<10analysis/false_prob_trees_$innercount.txt");
	open(my $OUTFILE5, ">>10analysis/probdistr_$innercount");
	while (<$INFILE5>) {
	    my @column2 = split /\t/, $_;
	    my $falseprob=$column2[0];
	    my $thetree=$column2[1];
	    if("$thetree" eq "$findtree"){
		print $OUTFILE5 "$trueprob\t$falseprob\n";
	    }
	}
	close $INFILE5;
	close $OUTFILE5;
    }
}
