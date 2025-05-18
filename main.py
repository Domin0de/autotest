# DO NOT MODIFY THIS FILE
import json
import subprocess

from colorama import Fore, init

LENGTH = 80

def clean_output(output: list):
    """Clean output list by removing empty string."""
    if output == [""]:
        return []
    return output

def line_format(words: list, prefix=""):
    """Format the text to fit within a specified length."""
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
        p_name = Fore.GREEN + f"Test passed: {name}\n"

        print(
            p_name + \
            Fore.RESET + \
            '=' * LENGTH
        )
        return

    p_name = Fore.RED + f"Test failed: {name}\n\n"
    input_val = f"Input:\n{Fore.LIGHTYELLOW_EX}{input_val if input_val else '<No value>'}\n"
    output = f"Got:\n{Fore.LIGHTRED_EX}{line_format(output) if output and len(clean_output(output)) != 0 else '<No value>'}\n"
    expected = f"Expected:\n{Fore.LIGHTGREEN_EX}{line_format(expected) if expected and len(expected) != 0 else '<No value>'}\n"

    print(
        p_name + \
        Fore.RESET + \
        input_val + \
        Fore.RESET + \
        '-' * LENGTH + "\n" + \
        output + \
        Fore.RESET + "\n" + \
        expected + \
        Fore.RESET + \
        '=' * LENGTH
    )

def main():
    """Main function to run the test cases."""
    init()

    with open("expects.json", "r", encoding="utf-8") as t:
        test_cases = json.load(t)
    with open("config.json", "r", encoding="utf-8") as c:
        config = json.load(c)

    print('=' * LENGTH)

    for test_case in test_cases:
        expected = test_case["expected"]

        with subprocess.Popen(
            config['run_args'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        ) as p:
            printed = False

            formatted_input = "\n".join(test_case["input"])
            for input_data in test_case["input"]:
                p.stdin.write(input_data)
                p.stdin.flush()

            output, _ = p.communicate()
            output_lines = output.split("\n")

            i = 0

            for test_line in output_lines:
                test_line = test_line if test_line else None
                expected_line = expected[i] if i < len(expected) else None

                if str(test_line) == str(expected_line):
                    i += 1
                    continue

                print_format(
                    test_case["name"],
                    formatted_input,
                    output_lines[i:],
                    expected[i:] if i < len(expected) else None
                )
                printed = True
                break

            if printed:
                continue

            if i < len(expected):
                print_format(test_case["name"], formatted_input, output_lines, expected)
            else:
                print_format(test_case["name"], formatted_input)

if __name__ == "__main__":
    main()
