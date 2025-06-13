from ete3 import Tree
domain = Tree("data/domain/Domain.newick")
phylo = Tree("data/phylotree/Phylo.newick",format=1)

phylo.show()