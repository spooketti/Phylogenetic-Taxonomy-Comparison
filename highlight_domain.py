from ete3 import Tree, TreeStyle, NodeStyle, TextFace, faces
import json
from pathlib import Path

# Load trees
domain = Tree("data/domain/Domain.newick", format=1)

family_colors = {
    "Bionectriaceae": "#1f77b4",   
    "Clavicipitaceae": "#ff7f0e",    
    "Cordycipitaceae": "#2ca02c",    
    "Hypocreaceae": "#d62728",        
    "Nectriaceae": "#9467bd",       
    "Ophiocordycipitaceae": "#8c564b", 
    "Sarocladiaceae": "#e377c2",    
    "Stachybotryaceae": "#7f7f7f",    
}

BASE_DIR = Path(__file__).parent

taxon_family = {}


with open(BASE_DIR / "data/domain/highlight.json", 'r',encoding="utf-8") as file:
    taxon_family = json.load(file)

for leaf in domain.iter_leaves():
    leaf_name = leaf.name
    matched = False
    for family_name, species_list in taxon_family.items():
        if leaf_name in species_list:
            color = family_colors.get(family_name, "black")
            style = NodeStyle()
            style["fgcolor"] = color
            style["size"] = 8 
            style["vt_line_color"] = color
            style["hz_line_color"] = color
            style["vt_line_width"] = 2
            style["hz_line_width"] = 2
            leaf.set_style(style)
            matched = True
            break
    if not matched:
        style = NodeStyle()
        style["fgcolor"] = "gray"
        leaf.set_style(style)

ts = TreeStyle()
ts.show_leaf_name = True
ts.title.add_face(TextFace("Leaf coloring by family (based on taxon name)", fsize=12), column=0)\

for family, color in family_colors.items():
    color_face = faces.RectFace(width=10, height=10, fgcolor=color, bgcolor=color)
    text_face = TextFace("  " + family, fsize=10)
    ts.legend.add_face(color_face, column=0)
    ts.legend.add_face(text_face, column=1)

domain.show(tree_style=ts)