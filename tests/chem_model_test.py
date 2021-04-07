from chem import RacemicMixture, Enantiomer

r_form = Enantiomer(id='CHEBI:61917',
                    enantiomer_form_of='CHEBI:74947',
                    absolute_configuration='R')
l_form = Enantiomer(id='CHEBI:61918',
                    enantiomer_form_of='CHEBI:74947',
                    absolute_configuration='S')
rm = RacemicMixture(id='',
                    has_left_enantiomer=l_form,
                    has_right_enantiomer=r_form)


