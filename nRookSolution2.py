from timeit import default_timer as timer
MatrixSize = (8,8)
totalSol = 0
totalSteps = 0
linearLoop = 0
finalSolution = 0
rowAttackDict= {}
columnAttackDict = {}

def createAttackingPosition():
   global rowAttackDict
   global columnAttackDict
   global MatrixSize
   if not rowAttackDict:
      for eachRow in xrange(MatrixSize[0]):
         rowAttackDict[eachRow] = {(eachRow,eachColumn): 0 for eachColumn in xrange(MatrixSize[1])}
         columnAttackDict[eachRow] = {(eachColumn, eachRow): 0 for eachColumn in xrange(MatrixSize[1])}
   global linearLoop
   linearLoop +=1

def nRookProblem(previousAP, row):
   global MatrixSize
   global totalSol
   global totalSteps
   global finalSolution
   rowNo = row
   x,y = MatrixSize
   for i in xrange(y):
      if row == 0:
         finalSolution = {}
         previousAP = {}
         # Make sure to call this only once.
         if not columnAttackDict:
            createAttackingPosition()
      totalSteps += 1
      #try:
      #   if previousAP[(row, i)]:
      #      continue
      #except KeyError:
      #   pass
      # This consumes O(n). Above code optimizes it to
      # O(1) as it throws an key error if it does not exist.

      if (rowNo, i) in previousAP:
         continue
      if row == y-1:
         finalSolution.update({(rowNo, i):0})
         print finalSolution.keys()
         totalSol += 1
         del finalSolution[(rowNo, i)]
      else:
         attackPositionList = dict(previousAP.items() + columnAttackDict[i].items() + rowAttackDict[rowNo].items())
         finalSolution.update({(rowNo, i):0})
         nRookProblem(attackPositionList, row+1)
         del finalSolution[(rowNo, i)]

start = timer()
nRookProblem({}, 0)
end = timer()
print("Total Sol=%s" % totalSol)
print("Total Steps=%s" % totalSteps)
print("Linear Loop=%s" % linearLoop)
print("Total Execution time=%s" % (end-start))	
