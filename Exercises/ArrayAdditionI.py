from itertools import combinations

def ArrayAdditionI(arr):
    highest = max(arr)
    temp = sorted(arr)
    temp2 = temp[:len(temp)-1]
    for i in xrange(1, len(temp2)+1):
        combis = list(combinations(temp2,i))
        for c in combis:
            if sum(c) == highest:
                return "true"
    return "false"

print ArrayAdditionI(raw_input())
