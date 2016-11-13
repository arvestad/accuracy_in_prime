#!/usr/bin/perl

use warnings;

open(my $INFILE0, "<4GTG_BR/GTG_BR.tree.sdiff");
open(my $OUTFILE0, ">11result/Result.txt");
print $OUTFILE0 "Result\n\nRobinson-Foulds Distance\n";
$count=1;
while(<$INFILE0>){
    my @columns=split /\s/, $_;
    if($count>2){
	print $OUTFILE0 "Start tree\tTrue tree\t$columns[2]\n\n";
    }
    else{
	print $OUTFILE0 "Start tree\tFalse tree $count\t$columns[2]\n";
	$count=$count+1;
    }
}
close $INFILE0;
close $OUTFILE0;

open(my $INFILE1, "<10analysis/true_false.newick.sdiff");
open(my $OUTFILE1, ">>11result/Result.txt");
$count=1;
while(<$INFILE1>){
    if($count<3){
	my @columns=split /\s/, $_;
	print $OUTFILE1 "True tree\tFalse tree $count\t$columns[2]\n";
	$count=$count+1;
    }
}
close $INFILE1;
close $OUTFILE1;

open(my $INFILE2, "<10analysis/true_MAP.newick.sdiff");
open(my $OUTFILE2, ">>11result/Result.txt");
while(<$INFILE2>){
    my @columns=split /\s/, $_;
    print $OUTFILE2 "\nTrue tree\tStart tree\t$columns[2]\n\n";
}
close $INFILE2;
close $OUTFILE2;

open(my $OUTFILE3, ">>11result/Result.txt");
print $OUTFILE3 "Kullback-Leibler\n";
for($count=2; $count>=1; $count--){
    open(my $INFILE3, "<10analysis/probdistr_$count");
    my $index=0;
    my $result=0;
    my @p_array;
    my @q_array;
    my @pq_array;

    while(<$INFILE3>){
	my @columns=split /\t/, $_;

#Must divide with 100 to get percentage
	my $P=$columns[0]/100;
	my $Q=$columns[1]/100;

	$pq_array[$index]=log($P/$Q);

	$result=$result+($pq_array[$index]*($P));

	$index=$index+1;
    }
    print $OUTFILE3 "True tree\tFalse tree $count:\t$result\n";
    close $INFILE3;
}
close $OUTFILE3;

open(my $OUTFILE4, ">>11result/Result.txt");
print $OUTFILE4 "\nVariational distance\n";
for($count=2; $count>=1; $count--){
    open(my $INFILE4, "<10analysis/probdistr_$count");
    my $index=0;
    my $result=0;
    my @pq_array;
    print $OUTFILE4 "True tree - False tree $count\n";
    while(<$INFILE4>){
	my @columns=split /\t/, $_;
	$P=$columns[0]/100;
	$Q=$columns[1]/100;
	$pq_array[$index]=($P-$Q);
	print $OUTFILE4 "$pq_array[$index]\n";
	$result=$result+($pq_array[$index]);
	$index=$index+1;
    }
    print $OUTFILE4 "Total variational distance: $result\n\n";
    close $INFILE4;
}
close $OUTFILE4;
