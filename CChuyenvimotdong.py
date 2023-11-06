#==============================================
#thuật toán chuyển vị một dòng
#thuật toán này không phải thuật toán mã hóa thay thế với mã hóa tiếng việt thì dễ hơn
#thuật toán chuyển vị không cần phải nhập khóa k
#==============================================
class Cchuyenvimotdong():
    def __init__(self,p,c,k):
        self.c=c
        self.p=p
        self.k=k
        
    #===================================================================
    def MaHoa(self):
        self.c=(self.p[0])
        # chữ cái đầu tiên trong chuỗi plaintext là giữ nguyên
        for i in range(1,len(self.p),2):
            self.c=self.c + self.p[i]
        for i in range(2,len(self.p),2):
            self.c=self.c + self.p[i]
        return self.c

#==============================================
    def GiaiMa(self):
        # ta dùng mảng để lưu trữ các ký tự theo chẵn lẻ trừ ký tự đầu tiên
        # ta có chuỗi ciphertext => duyệt lần lượt tịnh tiến và gán vào vị trí chẵn lẻ
        # 0 1 2 3 4 5 6 7 8 9 10 11
        # H A E G O D Y V A O D  A => len(ciphert) = len(plaintext)
        # H A   E   G   O   D    Y <==== gán vào vị trí số lẻ
        #     V   A   O   D   A    <==== gán vào vị trí số chẵn
        # H A V E A G O O D D A  Y <==== kết quả
        # 0 1 2 3 4 5 6 7 8 9 10 11
        # ta dùng chuỗi để ghi lại các số này khi duyệt
        # cuối cùng nối lại thành plaintext


        # tạo mảng kết quả để lưu lại các ký tự được xuất ra từ chuỗi ciphertext
        self.p = list(self.c) # list = list array = array = mảng
        k=1
        self.p[0]=self.c[0]
        # sao bỏ ký tự thứ 0 mà vẫn ra kết quả ta
        for i in range(1,len(self.c),2):
            # print(k,plaintext[k],i)
            # cipher[k] A E G O D Y
            # k         1 2 3 4 5 6
            # i         1 3 5 7 9 11
            self.p[i]=self.c[k]
            k=k+1
            
        for i in range(2,len(self.c),2):
            # print(k,plaintext[k],i)
            # cipher[k] V A O D  A
            # k         7 8 9 10 11
            # i         2 4 6 8  10
            self.p[i]=self.c[k]
            k=k+1
        #nối chuỗi => ta đổi từ mảng ra chuỗi là được kết quả
        #[] cipher = i[1] + i[2] + .. + i[n]
        ketqua=''
        #duyệt từng ký tự trong mảng plaintext
        for i in self.p:
            ketqua=ketqua+i
        return ketqua

#==============================================
def run():
    p = input("vui lòng nhập chuỗi cần mã hóa: ")

    cCchuyenvimotdong=Cchuyenvimotdong(p,'')
    c = cCchuyenvimotdong.MaHoa()
    print("chuỗi sau khi mã hóa: ",c)

    s=cCchuyenvimotdong.GiaiMa()
    print("chuỗi sau khi giải mã: ",s)

#===============================================
if __name__=='__main__':
    run()
