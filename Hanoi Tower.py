def TowerOfHanoi(n , A, B, C):           
    if n == 1:
        print("Move disc 1 from",A,"to",B)
        return
    TowerOfHanoi(n-1, A, C, B)
    print("Move disc",n,"from",A,"to",B)
    TowerOfHanoi(n-1, C, B, A)
 
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')