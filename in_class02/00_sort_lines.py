with open('in_class02/md_list.md', 'r') as f:
    lines = f.readlines()

sorted_lines = sorted(lines, key=lambda line: line[0].lower())

with open('in_class02/00_results.md', 'w') as f:
    f.writelines(sorted_lines)