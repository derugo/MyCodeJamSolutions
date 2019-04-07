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
