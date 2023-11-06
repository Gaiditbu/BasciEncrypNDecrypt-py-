import math
import numpy as ny
import random as rd
#===============
class RSAClass():
    def __init__(self,p = '', c = '', e = 0, d = 0, n = 0):
        self.p = p
        self.c = c
        self.e = e
        self.d = d
        self.n = n
    #===========
    def RandKeyGen(self):
        pQ = RandPQ()
        p = pQ[0]
        q = pQ[1]

        self.n = q*p
        rgPQ = math.gcd(q-1,p-1)
        lcm = ((p-1)*(q-1))//rgPQ

        e = 0
        d = 0
        while e == d:
            eFlag = True
            start = rd.randint(2,lcm-1)
            e = start
            while e < lcm:
                if(math.gcd(e, lcm) == 1):
                    eFlag =False
                    break
                e += 1
            if(eFlag):
                e = start - 1
                while e < lcm:
                    if(math.gcd(e, lcm) == 1):
                        eFlag =False
                        break
                    e -= 1

            k = 1
            d = 0
            #step = 0
            while True:
                #step += 1
                d = (k*lcm+1)/e
                if(d % 1 == 0):
                    break
                k += 1
            d = int(d)
        self.e = e
        self.d = d
    #===========
    def MaHoa(self):
        if(self.n == 0 or self.e == 0):
            self.RandKeyGen()
        ci = []
        for c in self.p:
            m = ord(c)
            kq = pow(m,self.e,self.n)
            ci.append(kq)
        self.c = ci
    #===========
    def GiaiMa(self):
        s = ''
        for c in self.c:
            kq = pow(c,self.d,self.n)
            s+=chr(kq)
        self.p = s
#===============
def UCLN(a, b):
    while 1 < 2:
        if(a % b == 0):
            return b
        a,b = b,a%b
#===============
def CheckPQ(p,q):
    if(p < q):
        max = q + 1
    else:
        max = p + 1
    #check = ny.zeros(max)
    check = ny.full(max, True)
    check[0] = False
    check[1] = False
    for i in range(2, len(check), 1):
        if(check[i]):
            for j in range(2, math.floor(max/i), 1):
                check[j*i] = False
    if(~check[p] & ~check[q]):
        return "P và Q không phải số nguyên tố"
    if(~check[p]):
        return "P không phải số nguyên tố"
    if(~check[q]):
        return "Q không phải số nguyên tố"
    return 1
#===============
def KeyGen():
    while True:
        while True:
            p = int(input("Nhập P (P là số nguyên tố):"))
            q = int(input("Nhập Q (Q là số nguyên tố):"))
            if(p*q > 1000):
                break
            print('P và Q quá nhỏ!')
        ck = CheckPQ(p,q)
        if(ck == 1):
            break
        print(ck)
    
    n = q*p
    rgPQ1 = UCLN(q-1,p-1)
    lcm = int((p-1)*(q-1)/rgPQ1)
    while True:
        st = 'Nhập khóa công khai (1 < e < ' + str(lcm) + ' và UCLN của e và ' + str(lcm) + ' là 1): '
        e = int(input(st))
        cke = UCLN(e, lcm)
        if(cke == 1):
            break
        print("e không hợp lệ!")

    k = 1
    d = 0
    while True:
        d = (k*lcm+1)/e
        if(d % 1 == 0):
            break
        k += 1
    d = int(d)
    return (e,d,n)
#===============
def PrimeMap():
    lenArr = 3000
    map = ny.full(lenArr, True)
    map[0] = False
    map[1] = False
    for i in range(2, len(map), 1):
        if(map[i]):
            for j in range(2, math.ceil(lenArr/i), 1):
                map[j*i] = False

    prMap = []
    for i in range(257, len(map),1):
        if map[i]:
            prMap.append(i)
    return prMap
#===============
def RandPQ():
    prMap = PrimeMap()
    i = rd.randint(0,len(prMap))
    p = prMap[i]
    prMap.pop(i)
    i = rd.randint(0,len(prMap))
    q = prMap[i]
    prMap.pop(i)
    return (p, q)
#===============
def RandKeyGen():
    pQ = RandPQ()
    p = pQ[0]
    q = pQ[1]
    print(p," ",q)

    n = q*p
    rgPQ1 = math.gcd(q-1,p-1)
    lcm = int((p-1)*(q-1)/rgPQ1)
    
    e = 0
    d = 0
    while e == d:
        eFlag = True
        start = rd.randint(2,lcm-1)
        e = start
        while e < lcm:
            if(math.gcd(e, lcm) == 1):
                eFlag =False
                break
            e += 1
        if(eFlag):
            e = start - 1
            while e < lcm:
                if(math.gcd(e, lcm) == 1):
                    eFlag =False
                    break
                e -= 1

        k = 1
        d = 0
        #step = 0
        while True:
            #step += 1
            d = (k*lcm+1)/e
            if(d % 1 == 0):
                break
            k += 1
        d = int(d)
    #print('d1: ',d)
    #print('step of way1: ',step)

    #d = 2
    #step = 0
    #loop = True
    #while loop:
    #    step += 1
    #    if((int(d*e))%lcm == 1):
    #        break
    #    d += 1
    #print('d2: ',d)
    #print('step of way2: ',step)
    return (e,d,n)
#===============
def MaHoa(p,e,n):
    ci = []
    for c in p:
        m = ord(c)
        kq = pow(m,e,n)
        ci.append(kq)
    return ci
#===============
def GiaiMa(ci,d,n):
    s = ''
    for c in ci:
        kq = pow(c,d,n)
        s+=chr(kq)
    return s
#===============
def handleKeypress(event):
    pressedKey = event.char
    return pressedKey
#===============
def Run():
    print('Start')

    #mangEDN = KeyGen()
    #mangEDN = RandKeyGen()
    #print(mangEDN[0],mangEDN[1],mangEDN[2])
    #p = input('Nhập chuỗi văn bản: ')
    #c = MaHoa(p, mangEDN[0], mangEDN[2])
    #print('Văn bản đã mã hóa: ', c)
    #p1 = GiaiMa(c, mangEDN[1], mangEDN[2])
    #print('Văn bản đã giải mã: ', p1)

    print('----RSA Encruption----')
    while True:
        print('Press "1" : Mã hóa Văn Bản.')
        print('Press "2" : Giải mã Văn Bản.')
        fst = input()
        try:
            fst = int(fst)
            if(fst == 1 or fst == 2):
                break
        except:
            fst = ''

    p = ''
    c = ''
    e = 0
    d = 0
    n = 0

    if fst == 1:
        print('Nhập thông tin (nếu thông tin khóa không hợp lệ, hệ thống sẽ tự tạo khóa mới)')
        p = input('Văn bản gốc: ')
        try:
            e = int(input('Khóa công khai (không bắt buộc): '))
            if e <= 1:
                e = 0
        except:
            e = 0
        try:
            n = int(input('số N (không bắt buộc): '))
            if n <= 1:
                n = 0
        except:
            n = 0
        if e > n:
            e = 0
            n = 0
    elif fst == 2:
        print('Nhập thông tin')
        loop = True
        while loop:
            loop = False
            c = input('Văn bản mã hóa: ')
            cArray = c.split(', ')
            for i in range(0, len(cArray),1):
                try:
                    cArray[i] = int(cArray[i])
                except:
                    print('Vãn bản mã không hợp lệ!')
                    loop = True
                    break
        while True:
            while True:
                try:
                    d = int(input('Khóa riêng tư (bắt buộc): '))
                    if d > 1:
                        break
                    print('Khóa bí mật không hợp lệ!')
                except:
                    print('Khóa bí mật phải là số nguyên dương!')
            while True:
                try:
                    n = int(input('số N (bắt buộc): '))
                    if n > 1:
                        break
                    print('số N phải không hợp lệ!')
                except:
                    print('số N phải là số nguyên dương!')
            if d < n:
                break
            print('Khóa không hợp lệ!')
        

    rsaObj = RSAClass(p, cArray, e, d, n)

    if fst == 1:
        rsaObj.MaHoa()
        print(rsaObj.e,', ',rsaObj.d,', ',rsaObj.n,', ')
        print('Văn bản mã hóa', end = ': ')
        for ci in rsaObj.c:
            print(ci, end = ', ')
    elif fst == 2:
        rsaObj.GiaiMa()
        print('Văn bản mã hóa: ', rsaObj.p)
#273635 ,  343115 ,  4564501
#2302192, 1499859, 825855, 130210, 1353218, 1640336, 4067162, 4149356


if __name__ == '__main__':
    Run()