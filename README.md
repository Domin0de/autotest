# Autotester Script

## Format
- main.py - Processes inputs and outputs of program code run
- implementation.py - Allows user to implement program/code with pre-defined run code
- expects.json - Configured inputs and outputs expected from the code
- config.json - General settings to allow modification of code run

## Run
- Ensure dependencies are installed by running ``python -m pip install -r requirements.txt``
- To run, complete relevant implementation in implementation.py, and run main.py using ``python main.py``

## Usage
- Ensure the current directory contains the following:
    - ``main.exe`` - this is the compiled version of main.py which does not require package installation
    - ``config.json`` - this determines what process is run to test against
    - ``expects.json`` - this lists the various test cases with relevant input and outputs expected
    - ``implementation.py`` or alternative process file - this is where the implementation should be completed, and will be the file listed in config.json
- Run the ``main.exe`` file in your terminal
