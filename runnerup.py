if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    max1 = -102
    max2 = -101
    for i in arr:
        if max1<i:
            max2 = max1
            max1 = i
        elif max1!=i and max2<i:
            max2 = i
    print (max2)