# Khai báo và sử dụng ( thuộc tính )
class Nguoidung:
    member = 1
    def __init__(self, name, age, district):
        self.name = name
        self.age = age
        self.district = district

Nguoidung1 = Nguoidung("A", "20", "District1")
print(Nguoidung.member)
print(Nguoidung1.member)

# Cập nhật giá trị thuộc tính thông qua lớp
class Nguoidung:
    stt = 1;            # cần tạo ra cái này nhằm mục đích tạo ra cho từng thể hiện để lưu trữ giá trị đó mà không đụng vô thông qua class
    so_thu_tu = 1       # số thứ tự của class - khi thay đổi sẽ làm nó thay đổi tất cả các giá trị trong đó
    member = 1
    def __init__(self, name, age, district):
        self.name = name
        self.age = age
        self.district = district
        self.stt = Nguoidung.so_thu_tu
        Nguoidung.so_thu_tu += 1
Nguoidung1 = Nguoidung("A", "20", "District1")
print(Nguoidung.member)
print(Nguoidung1.member)

Nguoidung.member = 2
print(Nguoidung.member)
print(Nguoidung1.member)

Nguoidung2 = Nguoidung("B", "22", "Dictrict2")
print(Nguoidung1.stt)
print(Nguoidung2.stt)
print(Nguoidung.so_thu_tu)
'''
ta chỉ thay đổi lại giá trị thuộc tính của lớp, 
tuy nhiên lại làm ảnh hưởng tới giá trị của đối tượng mặc dù đối tượng này được tạo  ra từ lớp 
ta chỉ thay đổi lại giá trị thuộc tính của lớp, tuy nhiên lại làm ảnh hưởng tới giá trị của đối 
tượng mặc dù đối tượng này được tạo  ra từ lớp 
'''

# Cập nhật giá trị thuộc tính thông qua đối tượng
class Nguoidung:
    member = 1
    def __init__(self, name, age, district):
        self.name = name
        self.age = age
        self.district = district    
Nguoidung1 = Nguoidung("A", "20", "District1")
print(Nguoidung.member)
print(Nguoidung1.member)

Nguoidung1.member = 2
print(Nguoidung.member)
print(Nguoidung1.member)
'''
Đã có sự khác biệt. Khi bạn thay đổi giá trị thuộc tính của một đối tượng, thì chỉ có đối tượng đó bị thay đổi, 
còn cái “khuôn mẫu” của chúng ta vẫn như vậy. Và dĩ nhiên nếu như có nhiều đối tượng khác nó cũng vẫn sẽ không bị ảnh hưởng chung.
'''

# Sử dụng thuộc tính trong các phương thức
class Nguoidung:
    def __init__(self, name, age, district):
        self.name = name
        self.age = age
        self.district = district    
    def xinchao(self):
        print("Hello my name is", self.name)
        print("My age is", self.age)
        print("Live in", self.district)
Nguoidung1 = Nguoidung("A", "20", "District1")    
Nguoidung1.xinchao()