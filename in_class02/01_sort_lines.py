def sort_lines(input_file, output_file):
    """This is a function"""
    with open(input_file, 'r') as f:
        lines = f.readlines()

    sorted_lines = sorted(lines, key=lambda line: line[13].lower())

    with open('in_class02/00_results.md', 'w') as f:
        f.writelines(sorted_lines)

input_file = 'md_list_unsorted.md'
output_file = ''

sort_lines 