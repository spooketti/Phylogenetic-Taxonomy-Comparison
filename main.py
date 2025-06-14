# from ete3 import Tree, TreeStyle, NodeStyle, TextFace
# domain = Tree("data/domain/Domain.newick",format=1)
# phylo = Tree("data/phylotree/Phylo.newick",format=1)

# comparison = domain.compare(phylo)
# rf = comparison["rf"]
# max_rf = comparison["max_rf"]
# norm_rf = comparison["norm_rf"]
# eff_tree_size = comparison["effective_tree_size"] 
# refEdgeSource = comparison["ref_edges_in_source"] 
# sourceEdgeRef = comparison["source_edges_in_ref"] 
# sourceSubtree = comparison["source_subtrees"] 
# commonEdge = comparison["common_edges"]
# sourceEdge = comparison["source_edges"]
# refEdge = comparison["ref_edges"]
# treekoDist = comparison["treeko_dist"]
# print(rf)

# ts = TreeStyle()
# ts.show_leaf_name = True
# ts.title.add_face(TextFace("test", fsize=12), column=0)
# domain.show(tree_style=ts)

from ete3 import Tree, TreeStyle, NodeStyle, TextFace

# Load the trees
domain = Tree("data/domain/Domain.newick", format=1)
phylo = Tree("data/phylotree/Phylo.newick", format=1)

# Compare trees
comparison = domain.compare(phylo, unrooted=True)

# Extract edge sets
common_edges = comparison["common_edges"]
source_edges = comparison["source_edges"]
source_only = set(source_edges) - set(common_edges)

# Function to get node from bipartition
def get_nodes_by_bipartitions(tree, bipartitions):
    nodes = []
    for node in tree.traverse("postorder"):
        if not node.is_leaf():
            if frozenset(node.get_leaf_names()) in bipartitions:
                nodes.append(node)
    return nodes

# Highlight common edges (green)
for node in get_nodes_by_bipartitions(domain, set(common_edges)):
    nstyle = NodeStyle()
    nstyle["fgcolor"] = "green"
    nstyle["hz_line_color"] = "green"
    nstyle["vt_line_color"] = "green"
    nstyle["hz_line_width"] = 2
    nstyle["vt_line_width"] = 2
    node.set_style(nstyle)

# Highlight source-only edges (red)
for node in get_nodes_by_bipartitions(domain, source_only):
    nstyle = NodeStyle()
    nstyle["fgcolor"] = "red"
    nstyle["hz_line_color"] = "red"
    nstyle["vt_line_color"] = "red"
    nstyle["hz_line_width"] = 2
    nstyle["vt_line_width"] = 2
    node.set_style(nstyle)

# TreeStyle
ts = TreeStyle()
ts.show_leaf_name = True
ts.title.add_face(TextFace("Green: Shared edges | Red: Unique to Domain", fsize=12), column=0)

# Show tree
domain.show(tree_style=ts)
