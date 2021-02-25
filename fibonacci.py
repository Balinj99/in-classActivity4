def fib(x):
    arr = []

    if(x < 0):
        print("\nError, value must be greater than 0.\n")
        return 0

    else:
              
        for i in range(0, (x+1)):
            if(i == 0):
                arr.insert(0, 0)

            elif(i == 1):
                 arr.insert(1, 1)

            else:
                f1 = arr[i-1]
                f2 = arr[i-2]
                result = f1 + f2
                arr.insert(i, result)
        
        return arr[x]

def fac(x):
 
    if(x < 0):
        print("\nError, value must be greater than 0.\n")
        return 0

    else:

        if(x == 0):
            return 1

        else:
            result = x
            
            for i in range(x, 0, -1):

                if (i == x):
                    result = result * 1

                else:
                    result = result * (x-i)

            return result
