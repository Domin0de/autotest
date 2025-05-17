import json
import subprocess

from colorama import Fore, init

LENGTH = 80

def line_format(text, prefix=""):
    """Format the text to fit within a specified length."""
    words = text.split()
    output = ""

    new_line = ""
    for word in words:
        if len(new_line) + len(word) + 1 > LENGTH:
            output += f"{prefix} {new_line.strip()}\n"
            new_line = ""

        new_line += f"{word} "

    if new_line:
        output += f"{prefix} {new_line.strip()}\n"
    return output.strip()


def print_format(name, input_val, output=None, expected=None):
    """Format the output for display."""
    if output is None:
        p_name = Fore.GREEN + f"Test passed: {name}"

        return f"""
        {'=' * LENGTH}
        {p_name}
        {"=" * LENGTH}
        """

    p_name = Fore.RED + f"Test failed: {name}"
    input_val = f"Input:\n{Fore.LIGHTYELLOW_EX}{input_val}\n"
    output = f"Got:\n{Fore.LIGHTCYAN_EX}{line_format(output)}\n"
    expected = f"Expected:\n{Fore.LIGHTMAGENTA_EX}{line_format(expected)}\n"

    return f"""
        {'=' * LENGTH}
        {p_name}
        {input_val}
        {'-' * LENGTH}
        {output}
        {expected}
        {'=' * LENGTH}
    """

def main():
    """Main function to run the test cases."""
    init()

    test_cases = json.loads("expects.json")

    for test_case in test_cases:
        expected = test_case["expected"]

        p = subprocess.Popen(
            ["python3", "run.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )

        formatted_input = "\n".join(input_data)
        for input_data in test_case["input"]:
            p.stdin.write(input_data.encode())
            p.stdin.flush()

        stdout, _ = p.communicate()
        output = stdout.strip()

        output_lines = output.split("\n")

        i = 0

        for test_line in output_lines:
            expected_line = expected[i]

            if test_line == expected_line:
                i += 1
                continue

            print(print_format(test_case["name"], formatted_input, output_lines[i:], expected[i:]))
            break

        if i != len(expected):
            print(print_format(test_case["name"], formatted_input, output, expected))
        else:
            print(print_format(test_case["name"], formatted_input))

        p.kill()
        p.stdin.close()

if __name__ == "__main__":
    main()
