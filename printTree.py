from ete3 import Tree

domain = Tree("data/domain/Domain.newick", format=1)

leaf_names = [leaf.name for leaf in domain.iter_leaves()]

with open("chopped.txt", "w") as f:
    for name in leaf_names:
        f.write(name + "\n")
