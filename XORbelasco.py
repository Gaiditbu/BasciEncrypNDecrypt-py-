#thuật toán mã hóa XOR

#=========================================
class CXORBelasco:
    def __init__(self,p,k):
        self.plaintext=p
        self.key=k
        self.ciphertext=''

    #=====================================
    def MaHoa(self):
        self.ciphertext=''

        for i in range(len(self.plaintext)): #for i
            c=self.plaintext[i]
            if(c == ' '):
                self.ciphertext= self.ciphertext + ' '
            else:
                so = ord(c) - ord('!') # tính vị trí của ký tự c, vì nếu c = A thì A - A = 0
                vt_key=i%len(self.key)
                so_key=ord(self.key[vt_key])-ord('!') #vì khóa cũng có thể là ký tự có dấu nên mình - cho ! luôn

                XOR=(so^so_key) %36864
                if chr((XOR)+ord('!'))=='逊':
                    self.ciphertext= self.ciphertext +"\n"
                elif chr((XOR)+ord('!'))=='瀊':
                    self.ciphertext= self.ciphertext +"\n"
                else:
                    self.ciphertext= self.ciphertext + chr((XOR)+ord('!')) # với key là số nguyên int
            # không cần dùng 65500 vì đây không phải phép toán thay thế thay thế là mã hóa thì + mà giải mã thì - hoặc là làm ngược lại
            # còn XOR là phép toán trên bit, XOR lần 1 là mã hóa, XOR lần 2 là giải mã
            # cho nên khi tính được số so vs A nó sẽ là 1 giá trị, giá trị đó XOR với key (int) nó ra gì kệ nó
            # mình lấy số vừa XOR được + 65 là ra độ chênh lệch (chr) của nó là ra dc ký tự mã hóa
            
        return self.ciphertext

#==========================================
def run():
    #p=input('vui lòng nhập chuỗi cần mã hóa: ')
    #p='Pham Đuc Thanh'
    p1='Trịnh Thanh Thiên'
    p="""que huong la chum khe ngot
    cho con treo hai moi ngay
    Quê hương là đường đi học
    Con về rợp bướm vàng bay
    Quê hương là con diều biếc
    Tuổi thơ con thả trên đồng
    Quê hương là con đò nhỏ
    Êm đềm khua nước ven sông"""

    #k=input('vui lòng nhập khóa k: ')
    k='abc'

    cCXORBelasco=CXORBelasco(p,k)
    c=cCXORBelasco.MaHoa()
    print('Chuỗi sau khi mã hóa: ',c)
    
    print()
    cCXORBelasco=CXORBelasco(c,k)
    s=cCXORBelasco.MaHoa()
    print('Chuỗi sau khi giải mã: ',s)

#============================================
if __name__=='__main__':
    run()
