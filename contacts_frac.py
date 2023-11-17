import MDAnalysis as mda

# define our universe and the NI01 peptide
u = mda.Universe("step5_0.gro", "step5_0.xtc")
peptide = u.atoms[0:836]

from MDAnalysis.analysis import contacts
import numpy as np
import pandas as pd

# define what constitutes a contact between residues
def contacts_within_cutoff(u, group_a, group_b, radius=10):
	timeseries = []
	for ts in u.trajectory:
		# calculate distances between group_a and group_b
		dist = contacts.distance_array(group_a.positions, group_b.positions)
		# determine which distances <= radius
		n_contacts = contacts.contact_matrix(dist, radius).sum()
		timeseries.append([ts.frame, n_contacts])
	return np.array(timeseries)


	res1 = 4
	res2 = list(range(2,50))
	l = []
	for item in res2:
		saltbridge1 = "(resid %d) and (name CA)"%res1
		saltbridge2 = "(resid %d) and (name CA)"%item
		bridge2 = peptide.select_atoms(saltbridge1)
		bridge3 = peptide.select_atoms(saltbridge2)
		a = 8
		ca = contacts_within_cutoff(u, bridge2, bridge3, radius=a)
		x,y = zip(*ca)
		s = []
		for i in y:
			if i > 0:
				s.append(i)
		frac = len(s)/len(y)
		r = "res{a}+res{b}".format(a=res1, b=item)
		n = (r, frac)
		l.append(n)
np.savetxt("res{a}_contacts_{c}A.txt".format(a=res1,c=a), l, fmt='%s')



