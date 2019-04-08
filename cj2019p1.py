#Problem
#Someone just won the Code Jam lottery, and we owe them N jamcoins! 
#However, when we tried to print out an oversized check, we encountered a problem. 
#The value of N, which is an integer, includes at least one digit that is a 4...
#and the 4 key on the keyboard of our oversized check printer is broken.

#Fortunately, we have a workaround: we will send our winner two checks for positive integer amounts A and B, 
#such that neither A nor B contains any digit that is a 4, and A + B = N. 
#Please help us find any pair of values A and B that satisfy these conditions.
# Sample Input 
#3
#4
#940
#4444

#Output 
  
#Case #1: 2 2
#Case #2: 852 88
#Case #3: 667 3777

def blackmagic(x):
    l = (list(str(x)))
    listofzeros = [0] * len(l)
    for i, val in enumerate(l):

        if val=='4':
            listofzeros[i]=1
            l[i]=3
    num1 = [str(i) for i in listofzeros]
    num2 = [str(i) for i in l]
    return ''.join(num1),''.join(num2)
if __name__ == '__main__':

    for i in range(int(input())):
        num=blackmagic(int(input()))
        print("Case #"+str(i+1)+": "+str(num[0])+" "+str(num[1]))
