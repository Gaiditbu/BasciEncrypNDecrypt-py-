# mã hóa belasco dùng khóa là chuỗi ký tự
# khóa mình có quy định là chữ không hay là chấp hết
#  mình dùng khóa là tiếng việt nữa 

#=============================================
class CBelasco:
    def __init__(self,p,c,k):
        self.p=p
        self.c=c
        self.key=k

    #=========================================
    def MaHoa(self):
        self.c=""
        #plantext=plaintext.upper()

        for i in range(len(self.p)):
            c = self.p[i]
            if c != ' ':
                # xác định vị trí khóa so với !
                khoa = ord(self.key[i%len(self.key)]) - ord('!')
                # xác định VBGoc = văn abrng ốc
                VBG = ord(c) - ord('!')
                # tính độ chênh lệch vị trí, tính khóa
                so = (khoa + VBG)%65500
                self.c = self.c + chr(so+ord('!'))
            else:
                self.c = self.c + ' '
        return self.c

    #=========================================
    def GiaiMa(self):
        self.p=''
    
        for i in range(len(self.c)):
            c = self.c[i]
            if c != ' ':
                # xác định vị trí khóa so với !
                khoa = ord(self.key[i%len(self.key)]) - ord('!')
                # xác định vị trí của VBMHoa
                VBMH = ord(c)-ord('!')
                # tính khóa
                so = (VBMH-khoa+65500) % 65500
                if chr(so+ord('!')) == '￦':
                    self.p = self.p + ('\n')
                else:
                    self.p = self.p + chr(so+ord('!'))
            else:
                self.p = self.p + ' '
        return self.p

    #===========================================

def run():
    p= input("vui lòng nhập chuỗi cần mã hóa: ")
    p1="""que huong la chum khe ngot
    cho con treo hai moi ngay
    Quê hương là đường đi học
    Con về rợp bướm vàng bay
    Quê hương là con diều biếc
    Tuổi thơ con thả trên đồng
    Quê hương là con đò nhỏ
    Êm đềm khua nước ven sông"""
    
    #key= input("vui lòng  nhập chuỗi khóa key: ")
    key='abc'

    cCBelasco=CBelasco(p,'',key)
    
    c= cCBelasco.MaHoa()
    print("Chuỗi sau khi được mã hóa: ",c)

    s=cCBelasco.GiaiMa()
    print("Chuỗi sau khi được giải mã: ",s)

#===========================================
if __name__=='__main__':
    run()









            
