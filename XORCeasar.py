#thuật toán mã hóa XOR

#=========================================
class CXORCeasar:
    def __init__(self,p,k):
        self.plaintext=p
        self.key=k
        self.ciphertext=''
    #========================
        
    def MaHoa(self):
        self.ciphertext=''

        for c in self.plaintext: #foreach
            so = ord(c) # tính vị trí của ký tự c, vì nếu c = A thì A - A = 0
        
        
            XOR=(so^self.key) % 65500 #luôn dương và xoay vòng
            #print(XOR)
            #chr(-44)

            self.ciphertext= self.ciphertext + chr(XOR) # với key là số nguyên int
            # không cần dùng 65500 vì đây không phải phép toán thay thế thay thế là mã hóa thì + mà giải mã thì - hoặc là làm ngược lại
            # còn XOR là phép toán trên bit, XOR lần 1 là mã hóa, XOR lần 2 là giải mã
            # cho nên khi tính được số so vs A nó sẽ là 1 giá trị, giá trị đó XOR với key (int) nó ra gì kệ nó
            # mình lấy số vừa XOR được + 65 là ra độ chênh lệch (chr) của nó là ra dc ký tự mã hóa
        
        return self.ciphertext

#==========================================
def run():
    #p=input('vui lòng nhập chuỗi cần mã hóa: ')
    #p='Pham Đuc Thanh'
    #p='Trịnh Thanh Thiên'
    p="""que huong la chum khe ngot
    cho con treo hai moi ngay
    Quê hương là đường đi học
    Con về rợp bướm vàng bay
    Quê hương là con diều biếc
    Tuổi thơ con thả trên đồng
    Quê hương là con đò nhỏ
    Êm đềm khua nước ven sông"""

    #k=input('vui lòng nhập khóa k: ')
    k=300
    cCXORCeasar =CXORCeasar(p,k)
    c=cCXORCeasar.MaHoa()
    print('Chuỗi sau khi mã hóa: ',c)
    
    print()
    
    cCXORCeasar =CXORCeasar(c,k)
    s=cCXORCeasar.MaHoa()
    print('Chuỗi sau khi giải mã: ',s)

#============================================
if __name__=='__main__':
    run()
