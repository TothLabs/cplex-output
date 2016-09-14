# cplex-output
Use this repository as a place to store code snippets used in parsing and manipulating CPLEX output. 

### Parsing `.sol` files
The CPLEX output used most frequently is `.sol` files, which store solution information such as objective function value and optimality, but also variable names and values. The latter is often of primary concern.
The `parseSingleSolFile_*.py` scripts extract variable values from a `.sol` file. The difference is the means of extraction.
- `parseSingleSolFile_xml.py` parses the XML that the solution data is stored in. This is more exact. However, for large solution files, this can take too long to make it worth it.
- `parseSingleSolFile_text.py` reads the solution file as text, line-by-line, and uses context to determine when a line contains a variable. While less robust to changes in `.sol` file formatting, this approach is generally much faster.
