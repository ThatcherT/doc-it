from chatgpt_wrapper import ChatGPT
import ast

bot = ChatGPT()


def doc_it(file_data):
    """
    Adds docstrings to the functions in the provided Python file.

    Args:
    file_data (str): The contents of a Python file as a string.

    Returns:
    str: The contents of the Python file with added docstrings.

    Note: If the length of the file_data is greater than 15000 characters,
    the function will not add docstrings and instead print a message indicating
    that chunking functionality needs to be implemented.
    """
    if len(file_data) > 15_000:
        print("This is a large file. TODO: implement chunking functionality")

    file_data_documented = bot.ask(
        "Add doc strings to the functions in this Python file \n"
        + "Do not change any of the following things: \n"
        + "Function names \n"
        + "Function parameters \n"
        + "Function return values \n"
        + "Code Logic \n"
        + "Variable names \n"
        + "Variable types \n"
        + "Variable values \n"
        + "Comments \n"
        + "Indentation \n"
        + "Spacing \n"
        + file_data
        + "\n"
        + "Only return the code itself, nothing else. Do not return any explaining text in your response."
    )
    # filtered_documented = remove_extraneous_file_data(file_data, file_data_documented)
    # return filtered_documented
    return file_data_documented


def remove_extraneous_file_data(file_data, file_data_documented):
    """
    Removes extraneous file data from a Python file after the addition of docstrings.

    Args:
    file_data (str): The original contents of a Python file as a string.
    file_data_documented (str): The contents of the Python file after adding docstrings.

    Returns:
    str: The contents of the Python file with extraneous data removed.

    Note: This function is not currently being used.
    """
    original_lines = file_data.split("\n")
    documented_lines = file_data_documented.split("\n")

    # Parse the original code and identify the lines inside docstrings
    docstring_lines_in_code = set()
    module = ast.parse(file_data)
    for node in ast.walk(module):
        # checks for string literals, aka docstrings
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
            # Add the line numbers of the docstring to a set
            docstring_lines_in_code.update(range(node.lineno, node.end_lineno + 1))

    filtered_lines = []
    in_docstring = False
    for i, line in enumerate(documented_lines):
        print(i, line)
        breakpoint()
        if i + 1 in docstring_lines_in_code:
            # This line is part of a docstring, so include it in the filtered output
            filtered_lines.append(line)
            in_docstring = (
                not in_docstring
            )  # Toggle the flag to indicate we're in a docstring
        elif line in original_lines and not in_docstring:
            # This line is in the original code, and we're not currently in a docstring, so include it
            filtered_lines.append(line)

    filtered_text = "\n".join(filtered_lines)
    breakpoint()
    return filtered_text


if __name__ == "__main__":
    # read the contents of this file as a string
    f_name = "utils.py"
    with open(f_name, "r") as f:
        file_data = f.read()
    file_data_documented = doc_it(file_data)
    # write the documented file data to a new file
    with open(f"{f_name.split('.')[0]}_documented.py", "w") as f:
        f.write(file_data_documented)
