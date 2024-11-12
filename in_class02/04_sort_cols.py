def sf_columns(input_file, output_file, primary_index=0, secondary_index=0, delimeter='', reverse=False):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    header = lines[:2]
    body = lines[2:]

    # tuple
    sorted_body = sorted(
        body,
        key=lambda line: (
            line.split(delimeter)(primary_index).lower()
            line.split(delimeter)(secondary_index).lower()
        ),
        reverse=reverse
    )

    sorted_lines = header + sorted_body

    with open(output_file, 'w') as f:
        f.writelines(sorted_lines)

input_file = 'test.md'
output_file = 'test.md'
    

