
def Buratino(a, n):
    dp = [[0]*n for _ in range(n)]
    way = [['']*n for _ in range(n)]

    dp[0][0] = a[0][0]

    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + a[0][j]
        way[0][j] = 'L'

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + a[i][0]
        way[i][0] = 'U'

    for i in range(1, n):
        for j in range(1, n):
            if dp[i][j-1] > dp[i-1][j]:
                dp[i][j] = dp[i][j-1] + a[i][j]
                way[i][j] = 'L'
            else:
                dp[i][j] = dp[i-1][j] + a[i][j]
                way[i][j] = 'U'

    path = []
    i = n - 1
    j = n - 1

    while i > 0 or j > 0:
        path.append((i, j))
        if way[i][j] == 'L':
            j -= 1
        else:
            i -= 1

    path.append((0, 0))
    path.reverse()

    return dp[n-1][n-1], path



n = int(input("Введіть кількість елементів в квадратичній матриці - "))
a = []
print("Введіть кількість монет через пробіл та enter щоб перейти на наступний поверх (shift + enter запуск):")
for i in range(n):
    a.append(list(map(int, input().split())))

s, path = Buratino(a, n)

print("Максимум монет:", s)
print("Шлях:")
for p in path:
    print(p)

