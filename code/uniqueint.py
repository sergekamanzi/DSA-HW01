import os

def uniqueint(inputFilePath):
    """
    Read a list of integers from an input file, generate an output file
    containing a sorted list of unique integers from the input file, and
    store the output file in the 'sample_results' directory within the 'hw01' directory.

    Parameters:
    inputFilePath (str): The full path of the input file to be processed.

    Returns:
    None
    """
    parentDirectory = 'dsa'
    hw01 = os.path.join(parentDirectory, 'hw01')
    sample_results = os.path.join(hw01, 'sample_results')

    inputFileName = os.path.basename(inputFilePath)
    outputFileName = os.path.splitext(inputFileName)[0] + '_results.txt'
    outputFilePath = os.path.join(sample_results, outputFileName)

    with open(inputFilePath, 'r') as inputFile:
        integers = []
        for line in inputFile:
            line = line.strip()
            for num in line.split():  
                if num.lstrip('-').isdigit():  
                    integers.append(int(num))

    unique_integers = set(integers)
    sorted_unique_integers = sorted(unique_integers, key=lambda x: (x >= 0, x))

    with open(outputFilePath, 'w') as outputFile:
        for integer in sorted_unique_integers:
            outputFile.write(str(integer) + '\n')

    print(f"Unique integers from '{inputFileName}' have been written to '{outputFilePath}'.")

inputFilePath = r"C:\Users\HP\Desktop\ALU\dsa\hw01\sample_inputs\sample_02.txt"
uniqueint(inputFilePath)
# inputFilePath = input("Enter the full path of the input file: ")
# uniqueint(inputFilePath)
