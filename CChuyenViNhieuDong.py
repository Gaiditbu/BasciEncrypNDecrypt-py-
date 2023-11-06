print('Mã Hóa Nhiều Dòng - Customize')
print('iluvPython')

#print('Path cai dat Python: C:\Users\admin\AppData\Local\Programs\Python\Python311')

import numpy as np
import math
import random

class CChuyenvinhieudong():
    def __init__(self,p,c,num,key):
        self.p=p #plaintext
        self.c=c #ciphertext
        self.key=[]
        self.key=key #key
        self.num=num
        
        
    #==============================================================
    def TimViTriX(self,x): #truyền vào với x và key dị x xíu gọi hàm sao ta
                            # nghĩa là chỉ cần self thì mình có thể dùng tất cả các phần tử của class
                            # còn muốn thêm thì tự add vào
                            # hoặc muốn gọi thì phải khai báo bên ngoài class?
        
        for i in range((self.num)):
            if self.key[i] == x:
                return i
        return -1; #len(key)

    #==============================================================
    def RandomVT(self):
        numberRD=[]

        #không cần khởi tạo hàm random

        #phân phối giá trị
        for i in range(0,self.num,1):
            numberRD.append(i)
            #print(numberRD[i]) #xuất thử phân phối
        # value 0 1 2 3 4 5 6
        # index 0 1 2 3 4 5 6
 
        n=len(numberRD)-1
    
        #temp=0 #-> biến để test
        GTLN=self.num-1 #Giá trị lớn nhất
    
        for i in range(self.num,0,-1):
            # giá trị từ k -1 -> 1 > 0 -> stop -> 7 lần rd -> vì có 7 slot cột

            # 6 5 4 3 2 1
        
            number =random.randint(0,GTLN) # rd lấy cả 2 mốc đầu và cuối nên mình phải -1
            GTLN=GTLN-1 #Giá trị lớn nhất
            #print('rd :', number) #xuất thử giá trị rd -> từ gtri rd ta so vị trí vs list numberRD
        
            #print('nmberrd[rd] :', numberRD[number]) # lấy giá trị từ list numberRD
            self.key.append(numberRD[number])
            # không có method kq[i].append -> truy cập bằng index, nhưng gán thì k gán giá trị theo index
    
            #print('kq[',temp,'] :' , kq[temp]) #in test
            #temp= temp+1 # biêns test

            while(number<n):
                numberRD[number]=numberRD[number+1]
                #print('numberRD[number]',numberRD[number])
                number=number+1
            n=n-1

    #for i in range(0,len(kq),1):
        #print(kq[i])
        return self.key

    #==============================================================
    def MaHoa (self):
        print(self.key)
        # số cột = len(key)
        #soCot =len(ey)
        soCot=self.num
        soDong = math.ceil(len(self.p)/soCot)
        tam = []
        k = 0
    
        # phân phối các ký tự vào mảng (ma trận)
        for i in range(soDong):
            row = []
            for j in range (soCot):
                if k >= len(self.p): #nếu đã hết dữ liệu plaintext thì những ô còn trống còn lại t gán *
                    # ta gán sao để có giải mã thì nó biết * là khoảng trống để nó điền
                    # nếu ta mà bỏ khoảng trắng lúc giải mã nó không có dấu hiệu để biết chỗ đó là khoảng trắng mà nó fill lại vào ô trong ma trận sao cho đúng thứ tự
                    
                    row= row + ['*']
                    continue
                row = row + [self.p[k]]
                k =k+1
            tam= tam + [row]
        self.c =""

        for i in range(len(tam)):
            print(tam[i])
        
        for i in range (0, self.num,1):
            vTC = self.TimViTriX(i) #VTC = vị trí cột
            for r in tam:
                self.c = self.c + r[vTC]
    
        return self.c

    #================================================================
    def GiaiMa(self):
        print(self.key)
        soCot=(self.num)
        soDong = math.ceil(len(self.c)/soCot)
        tam = np.zeros((soDong,soCot)) #ma trận 2 chiều
        i=0
    
        for k in range(0,(self.num),1):
            vTC= self.TimViTriX(k)
            for r in range(soDong):
                tam[r][vTC] = ord(self.c[i])
                i =i +1
        self.p=''

    
        for r in tam:
            for c in r:
                self.p = self.p + chr(int(c))
        return self.p.rstrip('*')

    #===================================================================
def run():
    #p=input('mời nhập chuỗi: ')
    #p='dataencryptionstrings'
    p='Trịnh Thanh Thiên'
    p1="""Đi dọc Việt Nam theo bánh con tàu quay
Qua đèo Hải Vân mây bay đỉnh núi
Nhớ khi xưa qua đèo qua núi
Mà lòng anh mơ tàu qua núi cao
Ngày hôm nay thênh thang con đường lớn
"""

    k=[]
    cCChuyenvinhieudong =CChuyenvinhieudong(p1,'',7,[])
    
    k=cCChuyenvinhieudong.RandomVT()

    cCChuyenvinhieudong =CChuyenvinhieudong(p1,'',7,k)

    #k = [3,5,6,7,2,1,4]
    c=cCChuyenvinhieudong.MaHoa()
    
    print("\nsau khi mã hóa: ",c)

    s=cCChuyenvinhieudong.GiaiMa(
        )
    print("sau khi giải mã: ",s)

#=======================================================================
if __name__== '__main__':
    run()
                















                 
