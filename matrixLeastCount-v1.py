from timer import timeit

def getValidNeighbour(currentPos, arrayOrder):
   def upper():
      #Upper valid
      (row, column) = currentPos
      if   (row-1) >= 0:
         return (row-1, column)
      else:
         #print("Negative row")
         return None

   def lower():
      #Lower valid
      (row, column) = currentPos
      if   arrayOrder[0] > (row+1) :
         return (row+1, column)
      else:
         #print("Outside matrix")
         return None

   def right():
      #Right valid
      #Lower valid
      (row, column) = currentPos
      if   arrayOrder[1] > (column+1) :
         return (row, column+1)
      else:
         #print("Outside matrix")
         return None

   def left():
      (row, column) = currentPos
      if   (column-1) >= 0:
         return (row, column-1)
      else:
         #print("Negative column")
         return None

   allPathsTemp = [left(), right(), lower(), upper()]
   allPaths = []
   for eachPath in allPathsTemp:
      if eachPath:
         allPaths.append(eachPath)
      
   return allPaths

def getValidNeighbour1(currentPos, arrayOrder):
   
   allPaths = []
   (row, column) = currentPos

   #Upper
   if   (row-1) >= 0:
      allPaths.append((row-1, column))

   #Lower valid
   if   arrayOrder[0] > (row+1) :
      allPaths.append((row+1, column))

   #right
   if   arrayOrder[1] > (column+1) :
      allPaths.append((row, column+1))

   #left
   if (column-1) >= 0:
      allPaths.append((row, column-1))

   return allPaths


def test():
   print("getValidNeighbour((0,0), (3,3))")
   getValidNeighbour((0,0), (3,3))

   print("getValidNeighbour((2,2), (3,3))")
   getValidNeighbour((2,2), (3,3))

   print("getValidNeighbour((2,0), (3,3))")
   getValidNeighbour((2,0), (3,3))

   print("getValidNeighbour((0,2), (3,3))")
   getValidNeighbour((0,2), (3,3))

def createRandomList(order):
   import random
   (rows, columns) = order
   array = []
   for eachrow in range(rows):
      rowArray = []
      for eachColumn in range(columns):
         rowArray.append(random.randint(1,99))
      array.append(rowArray)  

   return array


def printArray(A, order):
   (rows, columns) = order 
   for eachRow in range(rows):
      for eachColumn in range(columns):
         print(A[eachRow][eachColumn], end=" ")
      print("\n") 

   for eachRow in range(rows):
      for eachColumn in range(columns):
         value = ",".join([str(eachRow), str(eachColumn)])
         print(value,  end=" ")
      print("\n")

count=0
def getAllPaths(A, start, stop, order):
   global count
   getNeighbour = getValidNeighbour(start, order)
   for eachCell in getNeighbour:
      if eachCell not in A:
         A.append(eachCell)
         if eachCell == stop:
            print(A)
            A.pop()
            count += 1
            return A
         getAllPaths(A=A, start=eachCell, stop=stop, order=order)
         A.pop()

def getAllPaths1(A, start, stop, order):
   global count
   getNeighbour = getValidNeighbour1(start, order)
   for eachCell in getNeighbour:
      if eachCell not in A:
         A[eachCell] = 1
         if eachCell == stop:
            print(A.keys())
            del A[eachCell]
            count += 1
            return A
         getAllPaths1(A=A, start=eachCell, stop=stop, order=order)
         del A[eachCell]
 
@timeit
def main():
   #breakpoint()
   global count
   #test()
   order = (3,3)
   #array = createRandomList(order)
   #printArray(array, order)
   start=(0,0)
   stop =(order[0]-1,order[1]-1)
   #A=[start]
   #getAllPaths(A, start, stop, order)

   A={}
   A[start] = 1
   getAllPaths1(A, start, stop, order)
   print("Total paths=%s" % count)

if __name__ == '__main__':
   main()   
   
