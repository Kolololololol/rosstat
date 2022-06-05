
N = int(input())
secoDev=0
firsDev= int(N**(0.5))
for i in range(firsDev,0,-1):
    if (N%i==0):
        firsDev=i
        secoDev=N//firsDev
        break
ans = firsDev+secoDev-2
print(ans)

