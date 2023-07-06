import os

def generate_file_tree_md(directory, indent=''):
    tree_md = ''
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            tree_md += f'{indent}├── {item}\n'
            subdirectory = os.path.join(directory, item)
            tree_md += generate_file_tree_md(subdirectory, indent + '│   ')
        else:
            tree_md += f'{indent}└── {item}\n'
    return tree_md

root_directory = input("Please Enter Your Directory：")
md_content = generate_file_tree_md(root_directory)
with open('file_tree.md', 'w', encoding='utf-8') as file:
    file.write(md_content)
