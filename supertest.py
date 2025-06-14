from ete3 import Tree, TreeStyle, NodeStyle, TextFace

def style_tree(tree, uniquea, common):
    all_leaves = set(tree.get_leaf_names())
    for node in tree.traverse():
        if not node.is_leaf():
            clade = frozenset(node.get_leaf_names())
            # clade = node.get_leaf_names()
            complement = frozenset(all_leaves - clade)
            # complement = all_leaves-clade

            if clade in uniquea or complement in uniquea:
                # unique bipartition
                nstyle = NodeStyle()
                nstyle["fgcolor"] = "red"
                nstyle["size"] = 10
                nstyle["vt_line_color"] = "red"
                nstyle["hz_line_color"] = "red"
                nstyle["vt_line_width"] = 2
                nstyle["hz_line_width"] = 2
                node.set_style(nstyle)
            elif clade in common or complement in common:
                # shared bipartition
                nstyle = NodeStyle()
                nstyle["fgcolor"] = "green"
                nstyle["size"] = 10
                nstyle["vt_line_color"] = "green"
                nstyle["hz_line_color"] = "green"
                nstyle["vt_line_width"] = 2
                nstyle["hz_line_width"] = 2
                node.set_style(nstyle)
            else:
                # neither somehow???
                nstyle = NodeStyle()
                nstyle["fgcolor"] = "purple"
                nstyle["size"] = 5
                node.set_style(nstyle)
        else:
            # leaf node
            nstyle = NodeStyle()
            nstyle["fgcolor"] = "blue"
            nstyle["size"] = 5
            node.set_style(nstyle)


def highlight():
    tree1 = Tree("data/domain/Domain.newick", format=1)
    tree2 = Tree("data/phylotree/Phylo.newick", format=1)
    drfp = tree1.robinson_foulds(tree2, unrooted_trees=True)
    prfd = tree2.robinson_foulds(tree1,unrooted_trees=True)

    rf_distance =drfp[0]
    max_rf = drfp[1]
    common_bipartitions = drfp[2]
    parts_tree1 = drfp[3]
    parts_tree2 = prfd[3]
    rf_distance = tree1.compare(tree2)["rf"]


    print(f"robinson-foulds distance: {rf_distance}")
    print(f"maximum rf distance: {max_rf}")
    print(f"common bipartitions: {len(common_bipartitions)}")
    print(f"unique bipartitions in domain: {len(parts_tree1)}")
    print(f"unique bipartitions in phylo: {len(parts_tree2)}")

    style_tree(tree1, parts_tree1, common_bipartitions)
    style_tree(tree2, parts_tree2, common_bipartitions)

    ts1 = TreeStyle()
    ts1.show_leaf_name = True
    ts1.title.add_face(TextFace("Domain Tree", fsize=20), column=0)

    ts2 = TreeStyle()
    ts2.show_leaf_name = True
    ts2.title.add_face(TextFace("Phylo Tree (that doesn't work???)", fsize=20), column=0)

    tree1.show(tree_style=ts1)
    tree2.show(tree_style=ts2)

highlight()
