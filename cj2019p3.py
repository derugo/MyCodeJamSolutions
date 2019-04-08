#Problem
#On the Code Jam team, we enjoy sending each other pangrams, which are phrases that use each letter of the English alphabet at least once.
#One common example of a pangram is "the quick brown fox jumps over the lazy dog". 
#Sometimes our pangrams contain confidential information — for example, 
#CJ QUIZ: KNOW BEVY OF DP FLUX ALGORITHMS — so we need to keep them secure.
#We looked through a cryptography textbook for a few minutes, 
#and we learned that it is very hard to factor products of two large prime numbers, 
#so we devised an encryption scheme based on that fact. First, we made some preparations:
#We chose 26 different prime numbers, none of which is larger than some integer N.
#We sorted those primes in increasing order. 
#Then, we assigned the smallest prime to the letter A, the second smallest prime to the letter B, and so on.
#https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b
#Everyone on the team memorized this list.
#Now, whenever we want to send a pangram as a message, 
#we first remove all spacing to form a plaintext message. 
#Then we write down the product of the prime for the first letter of the plaintext and the prime for the second letter of the plaintext.
#Then we write down the product of the primes for the second and third plaintext letters, 
#and so on, ending with the product of the primes for the next-to-last and last plaintext letters. 
#This new list of values is our ciphertext. The number of values is one smaller than the number of characters in the plaintext message.
#For example, suppose that N = 103 and we chose to use the first 26 odd prime numbers, 
#because we worry that it is too easy to factor even numbers. 
#Then A = 3, B = 5, C = 7, D = 11, and so on, up to Z = 103. 
#Also suppose that we want to encrypt the CJ QUIZ... pangram above, so our plaintext is CJQUIZKNOWBEVYOFDPFLUXALGORITHMS. 
#Then the first value in our ciphertext is 7 (the prime for C) times 31 (the prime for J) = 217; the next value is 1891,
#and so on, ending with 3053.
#We will give you a ciphertext message and the value of N that we used. 
#We will not tell you which primes we used, or how to decrypt the ciphertext. Do you think you can recover the plaintext anyway?

#Input 
#2
#103 31
#217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
#10000 25
#3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543

#Output 
#Case #1: CJQUIZKNOWBEVYOFDPFLUXALGORITHMS
#Case #2: SUBDERMATOGLYPHICFJKNQVWXZ
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
