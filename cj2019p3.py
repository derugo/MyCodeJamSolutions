def primeFactors(n):
    list1 = []
    while n % 2 == 0:
        list1.append(2)
        n = n / 2
    for j in range(3, int(n ** (0.5)) + 1, 2):
        while n % j == 0:
            list1.append(j)
            n = n / j
    if n > 2:
        list1.append(n)
    return list1


if __name__ == '__main__':
    for ii in range(int(input())):
        p = input()
        x = str(input())

        num = x.split(" ")
        # print(primeFactors(int(num[0])),primeFactors(int(num[len(num)-1])))
        ini = primeFactors(int(num[0]))
        list1 = []
        for i, val in enumerate(num[:-1]):
            if int(num[i + 1]) % ini[0] == 0:
                if i == 0:
                    list1.append(ini[1])
                #list1.append(ini[1])
                list1.append(ini[0])
                ini[1] = int(num[i + 1]) / ini[0]
            else:
                if i == 0:
                    list1.append(ini[0])
                #list1.append(ini[0])
                list1.append(ini[1])
                ini[0] = ini[1]
                ini[1] = int(num[i + 1]) / ini[1]

        list1.append(int(num[len(num) - 1]) / list1[len(list1) - 1])


        alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        dict1 = dict(zip((sorted(set(list1))), alpha))
        #print(list1)
        #print((len(set(list1))))
        #print(dict1)
        list2 = []
        for xx in list1:
            list2.append(dict1[xx])
        # print("Case #" + str(i + 1) + ": " + result)
        dict1.clear()
        print("Case #" + str(ii + 1) + ": " + ''.join(list2))
