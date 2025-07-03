from ete3 import Tree, TreeStyle, NodeStyle, faces, TextFace

domain = Tree("data/domain/Domain.newick", format=1)
phylo = Tree("data/phylotree/Phylo.newick", format=1)

rf, max_rf, common_leaves, parts_t1, parts_t2, discarded_t1, discarded_t2 = domain.robinson_foulds(
    phylo, unrooted_trees=True, correct_by_polytomy_size=False)


def highlight_common_leaves(tree, common_leaves,color):
    for leaf in tree:
        if leaf.name in common_leaves:
            nstyle = NodeStyle()
            nstyle["fgcolor"] = "green"
            nstyle["size"] = 6
            leaf.set_style(nstyle)

            face = TextFace(leaf.name, fsize=10, fgcolor=color)
        else:
            face = TextFace(leaf.name, fsize=10)
        leaf.add_face(face, column=0)

highlight_common_leaves(domain, common_leaves,"green")
highlight_common_leaves(phylo, common_leaves,"green")

highlight_t1 = NodeStyle()
highlight_t1["fgcolor"] = "red"
highlight_t1["hz_line_width"] = 4
highlight_t1["vt_line_width"] = 4

highlight_t2 = NodeStyle()
highlight_t2["fgcolor"] = "blue"
highlight_t2["hz_line_width"] = 4
highlight_t2["vt_line_width"] = 4

def mark_splits(tree, parts, style):
    for node in tree.traverse("postorder"):
        if not node.is_leaf():
            leafset = frozenset(leaf.name for leaf in node.get_leaves())
            if leafset in parts:
                node.set_style(style)


highlight_common_leaves(domain, parts_t2,"red")
highlight_common_leaves(phylo, parts_t2,"red")


ts1 = TreeStyle()
ts1.show_leaf_name = False
ts1.title.add_face(TextFace("Domain - Red Unique splits", fsize=12), column=0)

ts2 = TreeStyle()
ts2.show_leaf_name = False
ts2.title.add_face(TextFace("Phylo - Blue Unique splits", fsize=12), column=0)

domain.show(tree_style=ts1)
phylo.show(tree_style=ts2)