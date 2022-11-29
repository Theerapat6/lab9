
def line_bin_sea(ninja,sea):
#binary
    low=0
    high=len(ninja)
   
    while(low <= high):
      mid = (low + high) // 2
      if(ninja[mid] == sea):
         return mid
      elif(sea < ninja[mid]):
         high = mid - 1
      elif(sea > ninja[mid]):
         low = mid + 1
    return -1
#linear
    for x in range(len(ninja)):
        if ninja[x] == sea:
            return x

ninja = [7,10,12,14,16,20,29,37]

print("index 14 is",line_bin_sea(ninja,14))
print("index 29 is",line_bin_sea(ninja,29))