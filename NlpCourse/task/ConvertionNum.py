
def f(nx,x1,x):
    #n为待转换的十进制数，x为机制，取值为2-62
    a=['0','1','2','3','4','5','6','7','8','9',
    'a','b','c','d','e','f','g','h','i','j','k',
    'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K',
    'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    nx=str(nx)
    b1=list(nx)
    print (nx,"[",x1,"]==[",x,"] ",end='') 
    b2=[]
    for i in b1:
        for i1 in range(0,62):
            if a[i1]==i:
                b2=b2+[i1]
                if i1>x1:
                    print (i,"错误定义")
    b2.reverse()
    #print(b2)
    n1=0
    n2=1
    for i in b2:
        n1=n1+int(i)*(pow(x1,n2-1))  #pow(x, n)，即计算 x 的 n 次幂函数
        n2=n2+1
        #print (n1,n2)
    n=n1
    #print(n)
    b=[]
    while True:
        s=n//x#商
        y=n%x#余数
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()  #reverse() 函数用于反向列表中元素,由个，十百转为百十个
    bd=""
    for i in b:
        #print(a[i],end='')
        bd=bd+a[i]
    print (bd)
    return bd

chun='zF4mOFpN7A' 
print (chun)
print (f(chun[0:2],62,10)+f(chun[2:6],62,10)+f(chun[6:11],62,10))
for i in range(0,62):
	f(str(i),10,62)
#F(str,str的进制,需要转换的进制)
