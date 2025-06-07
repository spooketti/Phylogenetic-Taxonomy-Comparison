import re

def extract_species_names(newick_path):
    with open(newick_path, 'r') as file:
        newick = file.read()

    labels = re.findall(r'[\(\),]([^\(\):,]+)', newick)

    species_set = set()
    for label in labels:
        words = label.strip().split()
        if len(words) >= 2:
            species = f"{words[0]} {words[1]}"
            species_set.add(species)

    return sorted(species_set)

species_list = extract_species_names("data/domain/Domain.newick")
for species in species_list:
    print(species)
