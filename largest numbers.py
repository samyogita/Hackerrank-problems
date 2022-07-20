def largest(arr, k):
    arr.sort(reverse=True)
    for i in range(k):
        print(arr[i], end = ' ')
arr = [55, 30, 1, 29, 18, 25]
k = 2
largest(arr, k)