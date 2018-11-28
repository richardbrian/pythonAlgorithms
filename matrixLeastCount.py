from timer import timeit


def getValidNeighbour(currentPos, arrayOrder):
   
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


count=0
def getAllPaths(A, start, stop, order):
   global count
   getNeighbour = getValidNeighbour(start, order)
   for eachCell in getNeighbour:
      if eachCell not in A:
         A[eachCell] = 1
         if eachCell == stop:
            print(A.keys())
            del A[eachCell]
            count += 1
            continue
         getAllPaths(A=A, start=eachCell, stop=stop, order=order)
         del A[eachCell]

pathTable = {}
def lookUpTable(order):
   global pathTable
   (rows, columns) = order
   for eachRow in range(rows):
      for eachColumn in range(columns):
         pathTable[(eachRow, eachColumn)] = getValidNeighbour((eachRow, eachColumn), order)
   return pathTable

def getAllPaths1(A, start, stop, order):
   global count
   global pathTable

   getNeighbour = pathTable[start]
   for eachCell in getNeighbour:
      if eachCell not in A:
         A[eachCell] = 1
         if eachCell == stop:
            print(A.keys())
            del A[eachCell]
            count += 1
            continue
         getAllPaths1(A=A, start=eachCell, stop=stop, order=order)
         del A[eachCell]

@timeit
def main():
   #breakpoint()
   global count
   #test()
   order = (8,8)
   lookUpTable(order)
   start=(0,0)
   stop =(order[0]-1,order[1]-1)

   A={}
   A[start] = 1
   getAllPaths1(A, start, stop, order)
   print("Total paths=%s" % count)

if __name__ == '__main__':
   main()

