#key (string)

#==========================================
class CVignere():
    def __init__(self,p,c,k):
        self.p=p
        self.c=c
        self.key=k
    #======================================
    def MaHoa(self):
        self.c=''
        for i in range (len(self.p)):
            c = self.p[i]
            
            vt_key= i % len(self.key)

            if c!= ' ':
                so = ord(c) - ord('!')
                # Lấy ra vị trí của ký tự muốn mã hóa
                so_key = ord(self.key[vt_key]) - ord('!') + 1

                so = (so + so_key) % 65500
                
                self.c = self.c + chr(so + ord('!'))
            else:
                self.c = self.c + self.key[vt_key]
        return self.c

#=====================================
    def GiaiMa(self):
        self.p= ''
        for i in range (len(self.c)): #thực ra leng của cip vs pla luôn luôn bằng nhau do là phép thay thế
            c = self.c[i]
            vt_key = i % len(self.key)
            if c != self.key[vt_key]:  #mình k so sánh vs khoảng trắng vì bản cipher là 1 chuỗi k có khoảng trắng
                so = ord(c) - ord('!')
                so_key=ord(self.key[vt_key]) - ord('!') +1
                so = (so - so_key + 65500) % 65500
                if chr(so+ord('!')) == '￦':
                    self.p = self.p + ('\n')
                else:
                    self.p= self.p + chr(so + ord('!'))
            else:
                self.p = self.p + ' '
        return self.p

#=========================================
def run():
    p = input("Mời nhập chuỗi cần mã hóa: ")
    #p=p.upper() #k cần upper luôn
    p1="""que huong la chum khe ngot
    cho con treo hai moi ngay
    Quê hương là đường đi học
    Con về rợp bướm vàng bay
    Quê hương là con diều biếc
    Tuổi thơ con thả trên đồng
    Quê hương là con đò nhỏ
    Êm đềm khua nước ven sông"""

    #k=input("Vui lòng nhập chuỗi key: ")
    #k = k.upper()
    k='abcabc'
    cCVignere =CVignere(p,'',k)
    
    c = cCVignere.MaHoa()
    print("Chuỗi sau khi mã hóa là: ",c)

    s=cCVignere.GiaiMa()
    print("Chuỗi sau khi giải mã: ",s)

#==========================================
if __name__=="__main__": #entry Point
    run()
    
    
