import dendropy

t1 = dendropy.Tree.get(path="data/phylotree/Hypocreales.newick", schema="newick")
t2 = dendropy.Tree.get(path="=data/phylotree/Corynebacterium.newick",schema="newick")

rf = t1.robinson_foulds_distance(t2)
print(rf)