#!/usr/bin/perl -w
use strict;
use warnings;
use warnings qw( FATAL utf8 );
use open qw( :encoding(UTF-8) :std );

my $f = $ARGV[0];

open(STR, $f);

while (<STR>) {
		my @ch = split('');
	
		foreach my $c (@ch) {
				print qq|'$c'\t| . sprintf("0x%X", ord($c)) . qq|\n|;
		}
}
close(STR);
