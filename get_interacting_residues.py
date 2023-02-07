from pymol import cmd 
import sys

print("""
Description:
    This script is used to print interacting residues between two molecules in two PDB files.
    
Usage: 
    pymol -c get_interacting_residues.py -- protein.pdb ligand.pdb 
""")

cmd.load(sys.argv[1], "protein")
cmd.load(sys.argv[2], "ligand")
cmd.do("sele polymer and name ca within 6.0 of ligand")
cmd.show("spheres", "sele")
residues = []
cmd.iterate("sele", "residues.append((resi, resn))")

# Print the residues
ri = []
for residue in residues:
    print("Residue:", residue[0], "Residue Name:", residue[1])
    ri.append(residue[0])
print("---Gromacs selection---")
print("Copy and paste the following command in the Gromacs shell (gmx make_ndx):") 
print("ri", *ri)