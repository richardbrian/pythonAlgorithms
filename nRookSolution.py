from timeit import default_timer as timer
MatrixSize = (8,8)
totalSol = 0
totalSteps = 0
linearLoop = 0
finalSolution = 0
rowAttackDict= {}
columnAttackDict = {}
completePosition = {}

def createAttackingPosition():
    global rowAttackDict
    global columnAttackDict
    global MatrixSize
    global completePosition
    global linearLoop

    if not rowAttackDict:
       for eachRow in xrange(MatrixSize[0]):
          rowAttackDict[eachRow] = {(eachRow,eachColumn): 0 for eachColumn in xrange(MatrixSize[1])}
          columnAttackDict[eachRow] = {(eachColumn, eachRow): 0 for eachColumn in xrange(MatrixSize[1])}

    completePosition = {}
    for x in xrange(MatrixSize[0]):
       for y in xrange(MatrixSize[1]):
          completePosition[(x,y)] = {}
          completePosition[(x,y)].update(rowAttackDict[x])
          completePosition[(x,y)].update(columnAttackDict[y])
          linearLoop +=1

def nRookProblem(previousAP, row):
    global MatrixSize
    global totalSol
    global totalSteps
    global finalSolution
    global completePosition
    x,y = MatrixSize
    if row == 0:
        finalSolution = {}
        previousAP = {}
    for i in xrange(y):
       totalSteps += 1
       if (row, i) in previousAP:
          continue
       if row == y-1:
          finalSolution.update({(row, i):0})
          print finalSolution.keys()
          totalSol += 1
          del finalSolution[(row, i)]
       else:
          attackPositionList = {}
          attackPositionList.update(previousAP)
          attackPositionList.update(completePosition[(row,i)])
          finalSolution.update({(row, i):0})
          nRookProblem(attackPositionList, row+1)
          del finalSolution[(row, i)]

start = timer()
createAttackingPosition()
nRookProblem({}, 0)

end = timer()
print("Total Sol=%s" % totalSol)
print("Total Steps=%s" % totalSteps)
print("Linear Loop=%s" % linearLoop)
print("Total Execution time=%s" % (end-start))	
