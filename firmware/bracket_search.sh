#!/bin/bash
perl -ne 'INIT{ $/ = "\0"} chomp; print "$_\n";' sp404mk2_sys_v501/SP404MKII_APP1.bin | perl -wln -e 'print $1 if /([\[<]+[\s\d\w]+[\]>]+)/'

