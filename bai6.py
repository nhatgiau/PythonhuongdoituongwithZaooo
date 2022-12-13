# Getter
class Meowbeu:
    def __init__(self, ho, ten):
        self.ho = ho
        self.ten = ten
        self.email = ho + '-' + ten + '@meowmeow.com'
    def ho_va_ten(self):
        return '{} {}'.format(self.ho, self.ten)

Meowbeu1 = Meowbeu("Nhật","Giàu")

Meowbeu1.ho = "Nguyen"
Meowbeu1.ten = "Giau"


print(Meowbeu1.ho)
print(Meowbeu1.ten)
print(Meowbeu1.email)
print(Meowbeu1.ho_va_ten())

'''
một điều là, bản chất nhìn vào nó là một phương thức, thật không đúng với cái ban  đầu ta muốn rằng nó là một thuộc tính. 
Để nó trở thành một thuộc tính, thì ta làm một thao tác như tạo classmethod. 
'''
class Meowbeu:
    def __init__(self, ho, ten):
        self.ho = ho
        self.ten = ten
        self.email = ho + '-' + ten + '@meowmeow.com'
@property
def email(self):
    return self.ho + '-' + self.ten + '@meowmeow.com'
@property
def ho_va_ten(self):
    return '{} {}'.format(self.ho, self.ten)
Meowbeu1 = Meowbeu("Nhật","Giàu")

Meowbeu1.ho = "Nguyen"
Meowbeu1.ten = "Giau"
print(Meowbeu1.ho)
print(Meowbeu1.ten)
print(Meowbeu1.email)
print(Meowbeu1.ho_va_ten())

# Setter
'''
Bản chất ho_va_ten là một phương thức, không thể gán cho một giá trị ngang như vậy được. Vì lí do đó, setter đã được sinh ra
'''
class Meowbeu:
    def __init__(self, ho, ten):
        self.ho = ho
        self.ten = ten
        self.email = ho + '-' + ten + '@meowmeow.com'
    @property
    def email(self):
        return self.ho + '-' + self.ten + '@meowmeow.com'
    @property
    def ho_va_ten(self):
        return '{} {}'.format(self.ho, self.ten)
    @ho_va_ten.setter
    def ho_va_ten(self, ten_moi):
        ho_moi, ten_moi = ten_moi.split(' ')
        self.ho = ho_moi
        self.ten = ten_moi

Meowbeu1 = Meowbeu("Nhật","Giàu")

Meowbeu1.ho_va_ten = "Nguyen Giau" # day la argument cho parameter ten_moi

print(Meowbeu1.ho_va_ten)

# Deleter
'''
Bạn muốn dùng xong xóa, thì deleter là công cụ giúp bạn xóa những thuộc tính bạn vừa gán. 
Xóa ở đây là việc gán một giá trị rác (giá trị không có ý nghĩa) cho cái chúng ta muốn xóa. 
Và thường trong Python giá trị đó được sử dụng là None (đôi lúc là 0, hoặc là một list rỗng, tùy từng thuộc tính mà ta muốn xóa)
Cú pháp gần như tương tự với setter (deleter không sử dụng parameter nào khác ngoài parameter self)
'''
class Meowbeu:
    def __init__(self, ho, ten):
        self.ho = ho
        self.ten = ten
        self.email = ho + '-' + ten + '@meowmeow.com'
    @property
    def email(self):
        return self.ho + '-' + self.ten + '@meowmeow.com'
    @property
    def ho_va_ten(self):
        return '{} {}'.format(self.ho, self.ten)
    @ho_va_ten.setter
    def ho_va_ten(self, ten_moi):
        ho_moi, ten_moi = ten_moi.split(' ')
        self.ho = ho_moi
        self.ten = ten_moi
    @ho_va_ten.deleter
    def ho_va_ten(self):
        self.ho = None
        self.ten = None
        print('Da xoa')
Meowbeu1 = Meowbeu("Nhật","Giàu")

Meowbeu1.ho_va_ten = "Nguyen Giau" # day la argument cho parameter ten_moi

print(Meowbeu1.ho_va_ten)
del Meowbeu1.ho_va_ten