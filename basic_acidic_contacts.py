# finding contacts between acidic and basic residues in NI01

sel_basic = "(resname ALA ALA) and (name CA CA)"
sel_acidic = "(resname ALA LEU) and (name CA CA)"

acidic = u.select_atoms(sel_acidic)
basic = u.select_atoms(sel_basic)

ca1 = contacts.Contacts(u,
                        selection=(sel_acidic, sel_basic),
                        refgroup=(acidic, basic),
                        radius=10,
                        method='hard_cut').run()

ca1_df = pd.DataFrame(ca1.timeseries,
                      columns=['Frame',
                               'Contacts from first frame'])

np.savetxt("contacts_frac_test_10A.txt", ca1_df)
