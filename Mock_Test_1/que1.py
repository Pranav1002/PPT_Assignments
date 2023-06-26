def moveZeroes(arr):
        
    z = 0

    for nz in range(len(arr)):
        if arr[nz]!=0 and arr[z]==0:
            arr[nz], arr[z] = arr[z], arr[nz]

        if arr[z]!=0:
            z+=1

    print(arr)

arr = [0,1,0,3,12]

moveZeroes(arr)