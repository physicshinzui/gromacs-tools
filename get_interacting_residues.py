#!/usr/bin/env python 
from pymol import cmd 
import argparse

print("""
Description:
    This script is used to view interacting residues of a receptor with another.
    
Usage: 
    pymol -c get_interacting_residues.py -- receptor.pdb binder.pdb 
""")
p = argparse.ArgumentParser()
p.add_argument("-r", "--receptor", type=str, required=True)
p.add_argument("-b", "--binder", type=str, required=True)
p.add_argument("-v", "--view", type=bool, required=False, default=False)
args = p.parse_args()
receptor = args.receptor
binder = args.binder

cmd.load(receptor, "receptor")
cmd.load(binder, "binder")
cmd.do("sele interface, receptor and name ca within 6.0 of binder")
cmd.show("spheres", "interface")
cmd.do("show sticks, byres interface")
#cmd.do("com sele")
residues = []

# Print the residues
ri = []
for atom in cmd.get_model("interface").atom:
    print("Residue:", atom.resn+atom.resi, "Atom Name:", atom.name)
    ri.append(atom.resi)
print("---Gromacs selection---")
print("Copy and paste the following command in the Gromacs shell (gmx make_ndx):") 
print("ri", *ri)
