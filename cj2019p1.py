
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







