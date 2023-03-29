n = int(input("몇 개의 데이터 처리 : "))
#append 안쓰고 대입하려면 
listex = [0]*n

print('%d개의 데이터 입력 : ' % n)
for k in range(n) : 
    #listex.append(int(input())) #
    listex[k] = int(input())

print('리스트 데이터의 합: %d\n' % sum(listex))
print('리스트 데이터의 평균 : %.2f\n' % (sum/len(listex)))
print('주어진 리스트는 최대값(%d), 최소값(%d)을 가지고 있습니다' %(max(listex), min(listex)))