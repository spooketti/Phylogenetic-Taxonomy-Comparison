from ete3 import Tree, NodeStyle, TextFace
import matplotlib.pyplot as plt

tree1 = Tree("data/domain/Domain.newick", format=1)
tree2 = Tree("data/phylotree/Phylo.newick", format=1) #phylo on the left

rf, max_rf, common_leaves, parts_t1, parts_t2, discarded_t1, discarded_t2 = tree1.robinson_foulds(
    tree2, unrooted_trees=True, correct_by_polytomy_size=False
)

def extract_leaf_positions(tree, x=0, y_start=0, y_gap=1.0):
    positions = {}
    for i, leaf in enumerate(tree.iter_leaves()):
        positions[leaf.name] = (x, y_start + i * y_gap)
    return positions

def draw_tree(ax, tree, x=0, y_start=0, y_gap=1.0, align_labels="left", fontsize=6, highlight_leaves=None):
    leaf_positions = extract_leaf_positions(tree, x, y_start, y_gap)

    def get_node_y(node):
        ys = [leaf_positions[leaf.name][1] for leaf in node.get_leaves()]
        return sum(ys) / len(ys)

    for node in tree.traverse("postorder"):
        if node.is_leaf():
            x1, y1 = leaf_positions[node.name]
            color = "green" if highlight_leaves and node.name in highlight_leaves else "black"
            ax.text(x1, y1, node.name, ha=align_labels, va="center", fontsize=fontsize, color=color)
            if node.up:
                x0 = x
                y0 = get_node_y(node.up)
                ax.plot([x0, x1], [y0, y1], color="black", linewidth=0.5)
        elif not node.is_root():
            x1 = x
            y1 = get_node_y(node)
            for child in node.get_children():
                x2 = x
                y2 = get_node_y(child)
                ax.plot([x1, x2], [y1, y2], color="black", linewidth=0.5)

    return leaf_positions

num_leaves = max(len(tree1), len(tree2))
y_gap = 0.3
fontsize = max(4, int(10 - 0.1 * num_leaves))
height = max(6, num_leaves * y_gap * 0.7)

fig, ax = plt.subplots(figsize=(7, height))
ax.axis("off")

x_left = 0
x_right = 5

pos1 = draw_tree(ax, tree1, x=x_left, y_gap=y_gap, align_labels="right", fontsize=fontsize, highlight_leaves=common_leaves)
pos2 = draw_tree(ax, tree2, x=x_right, y_gap=y_gap, align_labels="left", fontsize=fontsize, highlight_leaves=common_leaves)

common = set(pos1) & set(pos2)
for name in common:
    x1, y1 = pos1[name]
    x2, y2 = pos2[name]
    ax.plot([x1, x2], [y1, y2], color="gray", linewidth=0.5)

ax.set_xlim(-1, x_right + 1)
ax.set_ylim(-1, num_leaves * y_gap + 1)

plt.title("Tanglegram: Domain vs Phylo", fontsize=12)
plt.tight_layout()
plt.show()
