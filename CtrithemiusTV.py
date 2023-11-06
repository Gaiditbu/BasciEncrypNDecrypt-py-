#mã hóa trithemius không có khóa k
#=======================================

class Ctrithemius:
    def __init__(self,p,c,k):
        self.p=p
        self.c=c
        self.k=k
    
#=======================================    
    def MaHoa (self):
        self.c =""

        for i in range(len(self.p)): #i chính là độ lệch vị trí hoặc là key
            c = self.p[i]
            if c != ' ':
                so = ord(c) - ord('!')

                so = (so + (i%65500) )%65500

                self.c = self.c + chr(so + ord('!'))
            else:
                self.c = self.c + ' '
        return self.c

#=======================================

    def GiaiMa(self):
        self.p =""

        for i in range (len(self.c)):
            c = self.c[i]
            if c != ' ':
                so = ord(c) - ord('!')
                so = (so - (i % 65500) + 65500)%65500
                if chr(so+ord('!')) == '￦':
                    self.p = self.p + ('\n')
                else:
                    self.p = self.p + chr(so+ord('!'))

            else:
                self.p = self.p + ' '
        return self.p

#========================================

def run():
    #p=input ("vui lòng nhập chuỗi cần mã hóa: ")
    p="""que huong la chum khe ngot
    cho con treo hai moi ngay
    Quê hương là đường đi học
    Con về rợp bướm vàng bay
    Quê hương là con diều biếc
    Tuổi thơ con thả trên đồng
    Quê hương là con đò nhỏ
    Êm đềm khua nước ven sông"""
    #p='Thanh Thiên'

    cCtrithemius = Ctrithemius(p,'')
    c= cCtrithemius.MaHoa()
    print("chuỗi sau khi mã hóa: ",c)

    s= cCtrithemius.GiaiMa()
    print("chuỗi sau khi giải mã: ",s)

#==================================================

if __name__ == '__main__':
    run()



















        
