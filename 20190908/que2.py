numberN = int(input())
seqAi = list(map(int,input().split()))
benefitBi = list(map(int,input().split()))
increaseCi = list(map(int,input().split()))

# print(numberN)
# print(seqAi)
# print(benefitBi)
# print(increaseCi)

totalBenefit = 0
for k,seq in enumerate(seqAi):

    totalBenefit += benefitBi[seq -1]

    if k == 0:
        continue

    if seq == ( seqAi[k -1] +1 ):
        totalBenefit += increaseCi[seq -2]

print(totalBenefit)
