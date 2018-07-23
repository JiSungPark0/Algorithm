def checkfence(nfence,fencelen,f0,f1):
    """
    0. f0, f1을 2등분해서 두문제로 나눈다
    1. 재귀를 돌린다
    2. 판자 1개면 자기 자신을 리턴한다
    3. 리턴된 값을 merge 해서 가능한 새 값과 기존 값을 비교한다
    """
    if f0 == f1:
        return fencelen[f0]

    div = int((f1 + f0)/2)
    n1 = checkfence(nfence,fencelen,f0,div)
    n2 = checkfence(nfence,fencelen,div+1,f1)
    n3 = min(fencelen[f0:f1+1])*(f1 - f0 + 1)
    return max([n1,n2,n3])

f = open('.\Divide_and_Conquer\FENCE.txt', 'r')
fw = open('.\Divide_and_Conquer\FENCE_answer.txt', 'w')

k = 0
n = int(f.readline())
while k < n:
    nfence = int(f.readline().split()[0])
    fencelen = list(map(int,f.readline().split()))
    print(nfence,fencelen)
    ret = checkfence(nfence,fencelen,0,nfence-1)
    print(ret)
    k = k + 1
fw.close()
f.close()
