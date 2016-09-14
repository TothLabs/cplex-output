# Import libraries
import pandas as pd

# make template for output df
valsdf = pd.DataFrame({"Variable":[],"Value":[]}).set_index("Variable")

# indicator for whether we are in the variable section of the file
inVars = False
with open("PATH/TO/YOUR_SOLUTION_FILE.sol",'r') as f:
    for line in f:
        # if not inVars before but entering now, change the value on the toggle
        if not(inVars) and (line[3] == 'v' and line[4:6] == "ar"):
            inVars = True
        # if toggle still negatory, skip the line
        if not(inVars):
            continue
        # toggle flipped, heads up for the end of the section now
        if line[2] == '/':
            inVars == False
            break
        # found a variable. store its info
        # first, variable name
        varstart = line.find('name="')+6
        varend = line.find('"',varstart)
        var = line[varstart:varend]
        # next, variable value
        valend = line.rfind('"')
        valstart = line.rfind('"',0,valend-1)+1
        val = line[valstart:valend]
        # store in output dataframe
        valsdf.ix[var,:] = float(val)
f.closed
# Write dataframe to file
valsdf.to_csv("PATH/TO/YOUR_NEW_OUTPUT_FILE.csv")
