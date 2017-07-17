

MatrixSize = (6,6)
totalSol = 0
totalSteps = 0
linearLoop = 0

def getAttackingPosition(matrixSize, currentPosition):
   x,y = currentPosition
   global linearLoop
   (files, rank) = matrixSize
   attackingPosition = {}
   #0,0
   for i in xrange(files):
      attackingPosition.update({str((i, y)):0, str((x, i)):0})
      linearLoop +=1
   #print attackingPosition
   #import pdb;pdb.set_trace()
   return attackingPosition

def getAttackingPosition1(matrixSize, currentPosition):
   x,y = currentPosition
   (files, rank) = matrixSize
   attackingPosition = []
   #0,0
   for i in xrange(files):
      attackingPosition.append((i, y))
   for i in xrange(rank):
      attackingPosition.append((x, i))
   #print attackingPosition
   #import pdb;pdb.set_trace()
   return attackingPosition



def nRookProblem(previousAP, MatrixSize, row, finalSolution, deepth):
   global totalSol
   global totalSteps
   rowNo = row
   x,y = MatrixSize
   #import pdb;pdb.set_trace()
   for i in range(y):
      if deepth == 0:
         finalSolution = {}
         previousAP = {}
      totalSteps += 1
      if str((rowNo, i)) in previousAP:
         continue
      if deepth == y-1:
         finalSolution.update({str((rowNo, i)):0})
         #print finalSolution.keys()
         totalSol += 1
         del finalSolution[str((rowNo, i))]
      else:
         attackPositionList = dict(previousAP.items()  + getAttackingPosition(MatrixSize,(rowNo, i)).items())
         #finalSolution.append((rowNo, i))
         finalSolution.update({str((rowNo, i)):0})
         nRookProblem(attackPositionList, MatrixSize, row+1, finalSolution, deepth+1)
         del finalSolution[str((rowNo, i))]

def working():
   solution = []
   attackPositionList = []
   for i1 in range(3):
      row0= 0
      attackPositionList = getAttackingPosition1( MatrixSize, (row0, i1))    
      for j1 in range(3):
         row1= 1
         if (row1, j1) in attackPositionList:
            continue
         attackPositionList = attackPositionList + getAttackingPosition1(MatrixSize,(row1, j1))
         for k1 in range(3):
            row2 = 2
            if  (row2, k1) in attackPositionList:
               continue
            finalSolution =  [(row0, i1),(row1, j1), (row2, k1)]
            print finalSolution

nRookProblem({}, (8,8), 0, {}, 0)
print("Total Sol=%s" % totalSol)
print("Toral Steps=%s" % totalSteps)
print("Linear Loop=%s" % linearLoop)
#print "working"
#working()
