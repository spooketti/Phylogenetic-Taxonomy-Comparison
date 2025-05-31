# from ete4 import Tree

# # t1 = dendropy.Tree.get(path="data/phylotree/Hypocreales.newick", schema="newick")
# t1 = Tree("data/phylotree/Hypocreales.newick")
# t1.show()

from ete3 import Tree
# from ete3.tree import unrooted_robinson_foulds
t1 = Tree("data/phylotree/Hypocreales.newick")
t2 = Tree("data/phylotree/aiden.newick")
clade_sizes = [len(node.get_leaves()) for node in t1.traverse() if not node.is_leaf()]
print("Average clade size:", sum(clade_sizes) / len(clade_sizes))
t1.show()