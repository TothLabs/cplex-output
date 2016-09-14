# importing libraries
import pandas as pd
import xml.etree.ElementTree as ET

# Stores the XML tree.
# This can take awhile for large solution files.
solTree = ET.parse("PATH/TO/YOUR_SOLUTION_FILE.sol")

# Stores the "CPLEXSolution" element, which is the root of the XML tree
cpxSol = solTree.getroot()

# Make a dataframe to store solution values
# The dataframe in this simple example has a colume for the
# variable name and a column for its value.
# The variable name we assign to be the index.
valsdf = pd.DataFrame({"Variable":[],"Value":[]}).set_index("Variable")

# Iterates over all elements of type "variable" in the
# "CPLEXSolution" root that we defined earlier as cpxSol
for variable in cpxSol.iter("variable"):
	# Add variable to dataframe
	valsdf.ix[variable.get("name"),:] = float(variable.get("value"))

# Prints the dataframe to a file.
valsdf.to_csv("PATH/TO/YOUR_NEW_OUTPUT_FILE.csv")
