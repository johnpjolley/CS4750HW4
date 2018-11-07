class Variable:
    def __init__(self, numVariables):
        self.__value = 0
        self.__zero = False
        self.__one = False
        
    def setValue(self, value):
        self.__value = value
        
    def getValue(self):
        return self.__value
        
    def setZero(self, zero):
        self.__zero = zero
        
    def setOne(self, one):
        self.__one = one
        
    def getDomain(self):
        if self.__zero == False:
            return 0
        elif self.__one == False:
            return 1
        else:
            return 2

def backtracking(variables, number):
    if(variable.getDomain() == 0):
        variables[number].setZero(True)
        return variables, number
    elif(variable.getDomain() == 1):
        variables[number].setOne(True)
        return variables, number
    else:
        number = number - 1
        return variables, number
    
        
def forwardchecking(variables, number, clauses, numClauses, zeroValues, oneValues, master, nodes):
    variable = variables[number] #get variable object
    zeroSatasfied = zeroValues[number]
    oneSatasfied = oneValues[number]
    if (number != 0):
        last = master[number - 1]
    else:
        last = [False] * numClauses
    latest = [False] * numClauses
    if(variable.getDomain() == 0):
        varVal = 0
    elif(variable.getDomain() == 1):
        varVal = 1
    else:
        variables, number = backtracking(variables, number)
        forwardchecking(variables, number, clauses, numClauses, zeroValues, oneValues, master, nodes)
        return nodes, variables, master
    for i in range(numClauses):
        clause = clauses[i]
        length = len(clause)
        for j in range(length - 1):
            if ((number / clause[j]) == 1 or (number / clause[j]) == -1):
                clause[length - 1] = clause[length - 1] + 1
        if (clause[length - 1] == length - 1):
            variables, number = backtracking(variables, number)
            forwardchecking(variables, number, clauses, numClauses, zeroValues, oneValues, master, nodes)
            break
        if (varVal == 0):
            latest[i] = zeroSatasfied[i] or last[i]
        else:
            latest[i] = oneSatasfied[i] or last[i]
    master.append(latest)
    variables[number] = variable
    if(False in latest):
        nodes = nodes + 1
        return nodes, variables, master
    else:
        return nodes, variables, master
    
def readInput():
    #https://www.pythonforbeginners.com/dictionary/python-split
    f = open('example4.txt', 'r')
    line = f.readline()
    line.split()
    a,b,numVars,numClauses = line.split()
    clause = []
    clauses = []
    for line in f.readlines():
        clause = line.split()
        clause = list(map(int, clause)) #https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
        clauses.append(clause)
    f.close()
    return numVars, numClauses, clauses

def setVariable(number, numClauses, clauses, zeroValues, oneValues):
    zeroResults = [False] * numClauses #initialize list, https://stackoverflow.com/questions/13382774/initialize-list-with-same-bool-value
    oneResults = [False] * numClauses
    negNumber = number * -1
    index = 0 #indexes go from 0 to numVariables - 1
    for clause in clauses:
        length = len(clause)
        for i in range(length - 1):
            if (number / clause[i]) == 1:
                oneResults[index] = True #setting the variable to one makes this clause true
            elif (negNumber / clause[i]) == 1:
                zeroResults[index] = True #setting the variable to zero make this clause true
        index = index + 1
    zeroValues.append(zeroResults)
    oneValues.append(oneResults)

numVars, numClauses, clauses = readInput()
numClauses = int(numClauses)
numVars = int(numVars)
nodes = 0
zeroValues = []
oneValues = []
variableHolder = []
master = []
for i in range(numVars):
    setVariable((i + 1), numClauses, clauses, zeroValues, oneValues)
for i in range(numVars):
    variable = Variable(numVars)
    variable.setValue(i + 1)
    variableHolder.append(variable)
    
for number in range(numVars):
    nodes, variableHolder, master = forwardchecking(variableHolder, number, clauses, numClauses, zeroValues, oneValues, master, nodes)
    
print(nodes)    
for j in range(numVars):
    print(variableHolder[j].getValue())
    if(variableHolder[j].getDomain() == 0):
        print(0)
    elif(variableHolder[j].getDomain() == 1):
        print(1)
    else:
        print("No Solution")