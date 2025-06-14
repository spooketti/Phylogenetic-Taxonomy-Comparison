from ete3 import Tree, TreeStyle, NodeStyle, TextFace

# Load trees
domain = Tree("data/domain/Domain.newick", format=1)
phylo = Tree("data/phylotree/Phylo.newick", format=1)

# Compare
comparison = domain.compare(phylo, unrooted=True)

# Extract edge sets
common_edges = set(comparison["common_edges"])
source_edges = set(comparison["source_edges"])
ref_edges = set(comparison["ref_edges"])

def style_tree(tree, unique_bipartitions):
    for node in tree.traverse():
        if not node.is_leaf():
            # Check if the bipartition of this node is in the unique bipartitions set
            bip = node.get_leaf_names()
            bip = frozenset(bip)
            if bip in unique_bipartitions or (frozenset(tree.get_leaf_names()) - bip) in unique_bipartitions:
                # Mark different splits in red
                nstyle = NodeStyle()
                nstyle["fgcolor"] = "red"
                nstyle["size"] = 10
                nstyle["vt_line_color"] = "red"
                nstyle["hz_line_color"] = "red"
                node.set_style(nstyle)
            else:
                # Common splits in green
                nstyle = NodeStyle()
                nstyle["fgcolor"] = "green"
                nstyle["size"] = 5
                node.set_style(nstyle)

# Style each tree
style_tree(domain, parts_tree1)
style_tree(phylo, parts_tree2)
ts = TreeStyle()
ts.show_leaf_name = True
ts.title.add_face(TextFace("Domain Tree vs Phylo Comparison", fsize=14, bold=True), column=0)
ts.scale = 120


# Show tree
domain.render("domain_vs_phylo.png", tree_style=ts, w=800)
domain.show(tree_style=ts)