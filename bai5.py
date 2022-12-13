# Giới thiệu chung về phương thức đặc biệt
'''
Special method, đôi lúc người ta còn gọi là Magic method hoặc Dunder method. 
Những phương thức này đã được quy ước sẵn tên. Định dạng chung của các phức thức này là __tên phương thức __. 
Và chúng ta đã tìm hiểu một special method rồi đấy. Nếu bạn đọc chưa nhớ ra thì đó chính là hàm constructor của chúng ta. 
Nó cũng là một special method.
'''

# Giới thiệu một số phương thức đặc biệt
class Nguoidung:
    def __init__(self, name, age, district):
        self.name = name
        self.age = age
        self.district = district
Nguoidung1 = Nguoidung("A", "20", "District1")
print(Nguoidung1)
'''  Nếu bạn muốn khi in ra mà ta có một miêu tả rõ ràng về thứ này là gì, thì ta sẽ nên sử dụng hàm __str__ 
     Thì khi in ra, hàm __str__ này được gọi đến và trả về kết quả như bạn muốn 
     Phương thức __str__ này còn có một anh em họ nữa là phương thức __repr__                              '''

'''
 khi dùng hàm print. Nếu như lớp của bạn cùng có cả 2 phương thức __str__ và __repr__ thì hàm print ưu tiên dùng __str__ hơn. 
 Còn trên interactive prompt khi không dùng hàm print thì sẽ ưu tiên __repr__ hơn. 
 Tuy nhiên ta vẫn có cách để gọi __repr__ nếu cần (ngoài cách gọi trực tiếp đối tượng.__repr__()). 
 Vì mục đích của __repr__ cho thông tin chi tiết cụ thể về đối tượng, còn __str__ chỉ đơn giản là giá trị. 
 Ta nghĩ đơn giản như ta là một đối tượng, mỗi khi ta gọi hàm __str__ thì nó sẽ trả về hình ảnh bề da thịt của cơ thể chúng ta, 
 còn nếu gọi __repr__ thì trả về hình ảnh xương cốt, gân, cơ bắp của cơ thể chúng ta.
'''
class Nguoidung:                                # sử dụng str
    def __init__(self, name, age, district):
        self.name = name
        self.age = age
        self.district = district
    def __str__(self):
        return 'Day la {}, tuoi la {}, o quan {}'.format(self.name, self.age, self.district)
Nguoidung1 = Nguoidung("A", "20", "District1")
print(Nguoidung1)

class Nguoidung:                                # sử dụng repr
    def __init__(self, name, age, district):
        self.name = name
        self.age = age
        self.district = district
    def __repr__(self):
        return 'Day la: {} \ntuoi la: {} \no quan: {}'.format(self.name, self.age, self.district)
Nguoidung1 = Nguoidung("A", "20", "District1")
print(Nguoidung1)

# Bản chất hàm len cũng là một special method.
s = 'Zaonek'
print(len(s))
print(s.__len__())
'''
 bạn hoàn toàn có thể tự tạo riêng cho lớp của mình một special method để có thể sử dụng được hàm len (mặc định thì chưa được)
'''
def __len__(self):
    return len(self.ten)


# toán tử + của kiểu dữ liệu số hoặc chuỗi, list - Bản chất các toán tử cũng là những special method
print(2 + 3)
print(int.__add__(2, 3))
print('Bé ' + 'Zào')
print(str.__add__('Zào' , 'Đây'))
print([1, 2] + [3, 4])
print(list.__add__([1, 2], [3, 4]))

'''
 bạn cũng hoàn toàn có thể tạo riêng cho mình một toán tử
'''
def __add__(self, Nguoidungkhac):
    return self.sott + Nguoidungkhac.sott
