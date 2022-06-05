
############################################################################################################111111111111111111111111111111####################################################################################################################################



#def isprime(n):
#  if n == 1:
#   return True
#  for d in range(2, n//2):
#    if n % d == 0:
#      return False
#  return True
#Count = 0
#list_input = []
#for x in range(1,18):
# if isprime(x) == True:
#  list_input.append(x)
#  Count += 1
#list_input.pop(3)
#Count-=1
#print(list_input)
#print("Total:", Count)
#ansver=0
#ans1=[]
#ans2=[]
#ans3=[]
#for i in range(1000,10000):
#    for k in range(len(list_input)):
#     if((i//1000)+(i//100%10)==list_input[k] ):
#        ans1.append(i)
#
#     if ( (i // 10 % 10) + (i % 10) == list_input[k]):
#         ans2.append(i)
#
#for f in ans1:
#    for g in ans2:
#        if f == g:
#            ans3.append(f)
#            ansver+=1
#            break
#l=ansver+(((ansver-1)//3)*10)+120
#print(l)
#print(ans3)
#print(ansver)

####################################################################################################333333333333333333####################################################################################################################################



name=input()
NUM=int(input())
data=int(input())
dataM=int(input())
al=32
t=1
saum=0
if (name[0] == "А"):
    saum = t * 1 - 1
if (name[0] == "Б"):
    saum = t * 2 - 1
if (name[0] == "В"):
    saum = t * 3 - 1
if (name[0] == "Г"):
    saum = t * 4 - 1
if (name[0] == "Д"):
    saum = t * 5 - 1
if (name[0] == "Е"):
    saum = t * 6 - 1
if (name[0] == "Ж"):
    saum = t * 7 - 1
if (name[0] == "З"):
    saum = t * 8 - 1
if (name[0] == "И"):
    saum = t * 9 - 1
if (name[0] == "Й"):
    saum = t * 10 - 1
if (name[0] == "К"):
    saum = t * 11 - 1
if (name[0] == "Л"):
    saum = t * 12 - 1
if (name[0] == "М"):
    saum = t * 13 - 1
if (name[0] == "Н"):
    saum = t * 14 - 1
if (name[0] == "О"):
    saum = t * 15 - 1
if (name[0] == "П"):
    saum = t * 16 - 1
if (name[0] == "Р"):
    saum = t * 17 - 1
if (name[0] == "С"):
    saum = t * 18 - 1
if (name[0] == "Т"):
    saum = t * 19 - 1
if (name[0] == "У"):
    saum = t * 20 - 1
if (name[0] == "Ф"):
    saum = t * 21 - 1
if (name[0] == "Х"):
    saum = t * 22 - 1
if (name[0] == "Ц"):
    saum = t * 23 - 1
if (name[0] == "Ч"):
    saum = t * 24 - 1
if (name[0] == "Ш"):
    saum = t * 25 - 1
if (name[0] == "Щ"):
    saum = t * 26 - 1
if (name[0] == "Ъ"):
    saum = t * 27 - 1
if (name[0] == "Ы"):
    saum = t * 28 - 1
if (name[0] == "Ь"):
    saum = t * 29 - 1
if (name[0] == "Э"):
    saum = t * 30 - 1
if (name[0] == "Ю"):
    saum = t * 31 - 1
if (name[0] == "Я"):
    saum = t * 32 - 1
P=len(name)
for i in range(P-1):
   t= ((t*data)+dataM)%al
   if (name[i+1] == "А"):
       saum += t * 1-1
   if (name[i+1] == "Б"):
         saum += t * 2-1
   if (name[i+1] == "В"):
         saum += t * 3-1
   if (name[i+1] == "Г"):
         saum += t * 4-1
   if (name[i+1] == "Д"):
         saum += t * 5-1
   if (name[i+1] == "Е"):
         saum += t * 6-1
   if (name[i+1] == "Ж"):
         saum += t * 7-1
   if (name[i+1] == "З"):
         saum += t * 8-1
   if (name[i+1] == "И"):
         saum += t * 9-1
   if (name[i+1] == "Й"):
         saum += t * 10-1
   if (name[i+1] == "К"):
         saum += t * 11-1
   if (name[i+1] == "Л"):
         saum += t * 12-1
   if (name[i+1] == "М"):
         saum += t * 13-1
   if (name[i+1] == "Н"):
         saum += t * 14-1
   if (name[i+1] == "О"):
         saum += t * 15-1
   if (name[i+1] == "П"):
         saum += t * 16-1
   if (name[i+1] == "Р"):
         saum += t * 17-1
   if (name[i+1] == "С"):
         saum += t * 18-1
   if (name[i+1] == "Т"):
         saum += t * 19-1
   if (name[i+1] == "У"):
       saum += t * 20 - 1
   if (name[i+1] == "Ф"):
       saum += t * 21 - 1
   if (name[i+1] == "Х"):
       saum += t * 22 - 1
   if (name[i+1] == "Ц"):
       saum += t * 23 - 1
   if (name[i+1] == "Ч"):
       saum += t * 24 - 1
   if (name[i+1] == "Ш"):
       saum += t * 25 - 1
   if (name[i+1] == "Щ"):
       saum += t * 26 - 1
   if (name[i+1] == "Ъ"):
       saum += t * 27 - 1
   if (name[i+1] == "Ы"):
       saum += t * 28 - 1
   if (name[i+1] == "Ь"):
       saum += t * 29 - 1
   if (name[i+1] == "Э"):
       saum += t * 30 - 1
   if (name[i+1] == "Ю"):
       saum += t * 31 - 1
   if (name[i+1] == "Я"):
       saum += t * 32 - 1
ans=(saum*NUM)%10000
print(ans)