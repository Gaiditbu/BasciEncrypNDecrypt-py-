#thuật toán mã hóa XOR

#=========================================
class CXORVignere:
    def __init__(self,p,k):
        self.plaintext=p
        self.key=k
        self.ciphertext=''

    def MaHoa(self):
        self.ciphertext=''

        for i in range(len(self.plaintext)): #for i
            c=self.plaintext[i]
            vt_key = i % len(self.key)

            # khóa là str
            # khoảng trắng k cần phân biệt khoảng trắng tẹo nó XOR lại là cũng về lại như cũ
            
            so = ord(c) - ord('A') # tính vị trí của ký tự c, vì nếu c = A thì A - A = 0
            #print(so)
            so_key=ord(self.key[vt_key])-ord('A')+1

            # so = (so + so_key)%26 #mình so sánh với 65500 bản chất là mình so sánh với ! và mình giới hạn là 65500 ký tự mình + rồi - thì nó lại ban đầu
            # còn XOR thì mình XOR đi rồi XOR về chứ không phải là + rồi -
            # nên số này giới hạn trong 26 ký tự là được rồi vì đây bản chất chỉ là độ chênh lệch thôi
            # trường hơp mình mà dùng so này để XOR thì nó cứ tăng lên tăng lên chứ không quay lại như cũ nữa
            # thuật toán XOR là số XOR số => thay vì + thì mình sẽ ^ đẻ XOR nó lại
            # vignere bình thường thì lấy so + 65 nữa là xong mã hóa xíu - đi là giải mã


            XOR=(so ^ so_key)
            #print(XOR)

            self.ciphertext= self.ciphertext + chr(XOR+ ord('A'))
            # với key là số nguyên int
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
    k='abcdfeg'
    # điều kiện ràng buộc là phải nhập vào chuỗi là tổng hợp của 26 ký tự aphabet

    cCXORTrithemius=CXORVignere(p,k)
    c=cCXORTrithemius.MaHoa()
    print('Chuỗi sau khi mã hóa: ',c)
    
    print()

    cCXORTrithemius=CXORVignere(c,k)
    s=cCXORTrithemius.MaHoa()
    print('Chuỗi sau khi giải mã: ',s)

#============================================
if __name__=='__main__':
    run()
