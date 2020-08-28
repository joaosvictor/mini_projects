

corona = {}

corona['untranslated_region'] = cc[0:265]

corona['orf1a'] = translate(cc[266-1:13483], True)

# cc[266-1+4398*3:13468] = 'TTT_TTA_AAC' aka 'X_XXY_YYZ'
# https://en.wikipedia.org/wiki/Ribosomal_frameshift
# Programmed −1 Ribosomal Frameshifting
# TODO: add this to the translate function with automatic detection
corona['orf1b'] = translate(cc[13468-1:21555], False).strip("*")  # chop off the stop, note this doesn't have a start

# exploit vector, this attaches to ACE2. also called "surface glycoprotein"
# https://www.ncbi.nlm.nih.gov/Structure/pdb/6VYB -- open state
# https://www.ncbi.nlm.nih.gov/Structure/pdb/6VXX -- closed state
# 1273 amino acids
#   S1  = 14-685
#   S2  = 686-1273
#   S2' = 816-1273
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2750777/
corona['spike_glycoprotein'] = translate(cc[21563-1:25384], True)

# Forms homotetrameric potassium sensitive ion channels (viroporin) and may modulate virus release.
corona['orf3a'] = translate(cc[25393-1:26220], True)

# these two things stick out, used in assembly aka they package the virus
corona['envelope_protein'] = translate(cc[26245-1:26472], True)  # also known as small membrane
corona['membrane_glycoprotein'] = translate(cc[26523-1:27191], True)

corona['orf6'] = translate(cc[27202-1:27387], True)

corona['orf7a'] = translate(cc[27394-1:27759], True)
corona['orf7b'] = translate(cc[27756-1:27887], True)  # is this one real?

corona['orf8'] = translate(cc[27894-1:28259], True)

corona['nucleocapsid_phosphoprotein'] = translate(cc[28274-1:29533], True)

corona['orf10'] = translate(cc[29558-1:29674], True)
