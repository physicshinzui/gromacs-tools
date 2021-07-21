#!/bin/bash
cat<<EOS

Usage:
    bash $0 [.edr]

EOS

echo 11 | gmx energy -f nvt_prod_weakcoupling_1.edr -o potential & 
echo 12 | gmx energy -f nvt_prod_weakcoupling_1.edr -o kinetic   & 
echo 13 | gmx energy -f nvt_prod_weakcoupling_1.edr -o total     & 
