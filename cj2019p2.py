#https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da
#Problem
#You have just entered the world's easiest maze. You start in the northwest cell of an N by N grid of unit cells,
#and you must reach the southeast cell. You have only two types of moves available: a unit move to the east,
#    and a unit move to the south. You can move into any cell, but you may not make a move that would cause you to leave the grid.
#You are excited to be the first in the world to solve the maze, but then you see footprints. 
#Your rival, Labyrinth Lydia, has already solved the maze before you, using the same rules described above!
#As an original thinker, you do not want to reuse any of Lydia's moves. 
#Specifically, if her path includes a unit move from some cell A to some adjacent cell B,
#your path cannot also include a move from A to B. 
#(However, in that case, it is OK for your path to visit A or visit B, as long as you do not go from A to B.) 
#Please find such a path.
#In the following picture, Lydia's path is indicated in blue, and one possible valid path for you is indicated in orange:

#Input 
#2
#2
#SE
#5
#EESSSESE

#Output 
#Case #1: ES
#Case #2: SEEESSES

import sys
def itera(aa, ways, charr, it, me, n, steps_me, x):
    if it == me:
        if ways[aa] == 'E' and me[0] < n:
            me[0] += 1
            steps_me.append('S')
            return True
        elif ways[aa] == 'S' and me[1] < n:
            me[1] += 1
            steps_me.append('E')
            return True
        else:
            return False
    else:
        if charr == 'S':
            if me[0] < n:
                me[0] += 1
                steps_me.append('S')
                return True
            elif me[1] < n:
                me[1] += 1
                steps_me.append('E')
                return True
            else:
                return False
        else:
            if me[1] < n:
                me[1] += 1
                steps_me.append('E')
                return True
            elif me[0] < n:
                me[0] += 1
                steps_me.append('S')
                return True
            else:
                return False


def blackmagic(ways, charr, n, x):
    steps_me = []
    it = [0, 0]
    me = [0, 0]
    for i, steps in enumerate(ways):
        if itera(i, ways, charr, it, me, n, steps_me, x) == False:
            return False

        if steps == 'E':
            it[1] += 1
        else:
            it[0] += 1
            # print(it, me)
    # print(''.join(steps_me))
    return ''.join(steps_me)


if __name__ == '__main__':
    print(sys.version)
    for i in range(int(input())):
        n = int(input())-1
        x = raw_input()
        ways = list(str(x))
        result = blackmagic(ways, 'E', n, x)
        if result != False:
            print("Case #" + str(i+1) + ": " + result)
        else:
            print("Case #" + str(i+1) + ": " + blackmagic(ways, 'S', n, x))
