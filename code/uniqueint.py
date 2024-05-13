import os

def read_integers_from_file(input_file_path):
    """
    Read a list of integers from an input file.

    Parameters:
    input_file_path (str): The full path of the input file to be processed.

    Returns:
    list: A list of integers read from the input file.
    """
    integers = []
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            for num in line.split():
                if num.lstrip('-').isdigit():
                    integers.append(int(num))
    return integers

def write_unique_integers_to_file(integers, output_file_path):
    """
    Write unique integers from a list to an output file.

    Parameters:
    integers (list): A list of integers to be written.
    output_file_path (str): The full path of the output file.

    Returns:
    None
    """
    seen = {}
    for num in integers:
        seen[num] = True
    
    sorted_unique_integers = sorted(seen.keys(), key=lambda x: (x >= 0, x))
    
    with open(output_file_path, 'w') as output_file:
        for integer in sorted_unique_integers:
            output_file.write(str(integer) + '\n')

def uniqueint(input_file_path):
    """
    Read a list of integers from an input file, generate an output file
    containing a sorted list of unique integers from the input file, and
    store the output file in the 'sample_results' directory within the 'hw01' directory.

    Parameters:
    input_file_path (str): The full path of the input file to be processed.

    Returns:
    None
    """
    parent_directory = 'dsa'
    hw01 = os.path.join(parent_directory, 'hw01')
    sample_results = os.path.join(hw01, 'sample_results')

    input_file_name = os.path.basename(input_file_path)
    output_file_name = os.path.splitext(input_file_name)[0] + '_results.txt'
    output_file_path = os.path.join(sample_results, output_file_name)

    integers = read_integers_from_file(input_file_path)
    write_unique_integers_to_file(integers, output_file_path)

    print(f"Unique integers from '{input_file_name}' have been written to '{output_file_path}'.")

input_file_path = r"C:\Users\HP\Desktop\ALU\dsa\hw01\sample_inputs\sample_02.txt"
uniqueint(input_file_path)
# input_file_path = input("Enter the full path of the input file: ")
# uniqueint(input_file_path)
