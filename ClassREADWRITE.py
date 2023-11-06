class READWRITE:
    def __init__(self,path,name,content):
        self.lines=[] # khai báo list chứa các dòng
        self.path=path
        self.name=name
        self.content=content

    # hàm đọc file
    def DocFile(self):
        f = open(self.path, encoding="utf8")
        for line in f:
            print(line) #in ra xem thử có đọc dc kh
            self.lines.append(line)
        return self.lines

#############################
    def GhiFile(self):
        #count=1 #count này xử lý bên biến truyền vào luôn cho dễ
        # nghĩa là name sẽ có dạng name1 name2 name3 nó xử lý trước r truyền vào
        # mình chỉ gán vào tên thôi
        f=open('3T'+self.name+'.txt','w',encoding="utf8")
        # thuộc tính w là Tạo một file mới để ghi, nếu file đã tồn tại thì sẽ bị ghi mới
        # count=count+1
        #f.writelines(self.lines) #MÌNH K GHI NỘI DUNG VỪA ĐỌC, MÀ MÌNH SẼ GHI NỘI DUNG ĐƯỢC TRUYỀN VÀO
        f.writelines(self.content)
        # làm sao để đặt biến ++ cho đúng, mỗi lần gọi ghi file là nó tăng
    
#=========================

def run():

    cREADWRITE=READWRITE('text.txt','vignere')
    
    cREADWRITE.DocFile()
    cREADWRITE.GhiFile()
#========================
if __name__=='__main__':
    run()

