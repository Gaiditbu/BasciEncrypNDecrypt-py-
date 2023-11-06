#=====================================================================================
# FFFC - 0021 = FFDB = 65499 + 1
# 65532 - 33 = 65499 + 1 = 65500

class CCeasar():
    def __init__(self,p,c,k):
        self.p=p
        self.c=c
        self.key=k
        
    #====================================
    #mã hóa
    def MaHoa (self):
        self.c=''
        #plaintext=plaintext.upper()
        # viết hoa xử lý tại Server - tránh đưa quyền quyết định cho người dùng - tránh numeric attack
        for c in self.p:
            if c!=' ':
                so = ord(c) - ord('!')
                # hàm ord lấy giá trị Unicode của ký tự
                so = (so + self.key) % 65500
                # xoay vòng, giới hạn nhỏ hơn 26 ký tự, có khi k ngta cho lớn hơn 26 thì + số nào cũng luôn lớn hơn 26
                # do k mình k giới hạn có độ lớn khóa k là bao nhiêu nên mình phải % 26 để nó nằm trong khoảng 26 ký tự
                self.c = self.c + chr(so + ord('!'))
            else:
                self.c=self.c + c
        return self.c

    #====================================== 
    #giải mã
    def GiaiMa (self):
        self.p =''
        #ciphertext=ciphertext.upper()
        for c in self.c:
            if c!= ' ':
                so = ord(c) - ord('!')
                so = (so - self.key + 65500)%65500
                if chr(so+ord('!')) == '￦':
                    self.p = self.p + ('\n')
                else:
                    self.p = self.p + chr(so+ord('!'))
            else:
                self.p = self.p +c
        return self.p          

#=========================================
def run():
    #p = input(" Mời nhập chuỗi cần mã hóa: ")
    
    p1="""Que huong la chum khe ngot
cho con treo hai moi ngay
Quê hương là đường đi học
Con về rợp bướm vàng bay
Quê hương là con diều biếc
Tuổi thơ con thả trên đồng
Quê hương là con đò nhỏ
Êm đềm khua nước ven sông"""

    #key = int(input("mời nhập key: "))
    key=5

    cCCeasar=CCeasar(p1,'',key)
    
    c=cCCeasar.MaHoa()
    #cipher = c.upper()
    print("Sau khi mã hóa: ",c)
    
    s=cCCeasar.GiaiMa()
    print("Sau khi giải mã: ",s)

#=========================================

if __name__=="__main__": #entry Point
    run()
    
