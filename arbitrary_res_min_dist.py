from itertools import product
import linalg.norm as LA
import numpy as np
from numpy import linalg as LA
norm = LA.linalg.norm

# split peptides into residue based on the groups of atoms within the residues
res_peptide2 = []
res_peptide1 = []
res_peptide3 = []
for i in range (2,50):
	a = peptide1.select_atoms("name CA and resid %d"%i).positions
	b = peptide2.select_atoms("name CA and resid %d"%i).positions
	c = peptide3.select_atoms("name CA and resid %d"%i).positions
	res_peptide3.append(c)
	res_peptide2.append(b)
	res_peptide1.append(a)

# printed list of the residue position in peptide 2
p2_2, p2_3, p2_4, p2_5, p2_6, p2_7, p2_8, p2_9, p2_10, p2_11, p2_12, p2_13, p2_14, p2_15, p2_16, p2_17, p2_18, p2_19, p2_20, p2_21, p2_22, p2_23, p2_24, p2_25,
p2_26, p2_27, p2_28, p2_29, p2_30, p2_31, p2_32, p2_33, p2_34, p2_35, p2_36, p2_37, p2_38, p2_39, p2_40, p2_41, p2_42, p2_43, p2_44, p2_45, p2_46, p2_47, p2_48, p2_49 = res_peptide2

# finding min distance between an arbitrary residue in peptide 2 and another residues in another peptide
mins = []
for i in range(0, 48):
	m = product(p2_2, eval('p3_%d'% (i+2)))
	m = list(m)
	changes = [abs(a-b) for a,b in m]
	norms = []
	for vector in changes:
		a = norm(vector)
		norms.append(a)
	min_norm = min(norms)
	mins.append(min_norm)
l = enumerate(mins, start=2)
for items in l:
	if item[1] < 7:
		print(items)


changes_x = [abs(item[0]) for item in changes]
changes_y = [abs(item[1]) for item in changes]
changes_z = [abs(item[2]) for item in changes]
non_pbc_x = []
non_pbc_y = []
non_pbc_z = []
for i in changes_x:
	if i > pbc_scale:
            a = dimensions - i
        else:
            a = i
        non_pbc_x.append(a)
for i in changes_y:
	if i > pbc_scale:
            a = dimensions - i
        else:
            a = i
        non_pbc_y.append(a)
for i in changes_z:
	if i > pbc_scale:
            a = dimensions - i
        else:
            a = i
        non_pbc_z.append(a)
non_pbc_vecs = zip(non_pbc_x, non_pbc_y, non_pbc_z)
non_pbc_vecs = list(non_pbc_vecs)
