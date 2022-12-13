# Class method
'''
Nếu regular method có argument đầu tiên tự động đưa vào là đối tượng đó và được nhận bởi parameter self thì ở class method, 
argument đầu tiên tự động đưa vào chính lớp gọi phương thức đó hoặc là lớp của đối tượng gọi phương thức đó.
Theo quy ước thì parameter nhận argument này sẽ là cls.
'''
class Monhoc:
    slot = 30
    def __init__(self, ten, slot_so, giang_vien):
        self.ten = ten
        self.slot_so = slot_so
        self.giang_vien = giang_vien

CSI104 = Monhoc("CSI104", "Mot", "ABC")

Monhoc.slot = 40



# Dùng class method
class Monhoc:
    slot = 30
    def __init__(self, ten, slot_so, giang_vien):
        self.ten = ten
        self.slot_so = slot_so
        self.giang_vien = giang_vien
    @classmethod
    def capnhatslothoc(cls, soslot):
        cls.slot = soslot

CSI104 = Monhoc("CSI104", "Mot", "ABC")
print(Monhoc.slot)
print(CSI104.slot)

Monhoc.capnhatslothoc = 40

print(Monhoc.slot)
print(CSI104.slot)
# Tuy nhiên, đây không phải là ứng dụng chính của class method. Class method thường được dùng để tạo đối tượng.


#  có một chút kiến thức về XỬ LÝ CHUỖI. Đầu tiên ta cần tách bằng kí tự “-“, nghĩa ngay tới phương thức split của chuỗi
class Monhoc:
    slot = 30
    def __init__(self, paraten, paraslot_so, paragiang_vien):
        self.ten = paraten
        self.slot_so = paraslot_so
        self.giang_vien = paragiang_vien
    @classmethod
    def from_string(cls, s):
        lst = s.split('-')
        new_lst = [st.strip() for st in lst]
        ten, slot_so, giang_vien = new_lst
        return cls(ten, slot_so, giang_vien)

infor_str = "CSI104 - Slot1 - ABC"
CSI104 = Monhoc.from_string(infor_str)
print(CSI104.__dict__)



# Static method
'''
Regular method được ngầm gửi vào argument là chính đối tượng gọi phương thức và ta sử dụng parameter self để xử lí những vấn đề khác, 
class method được ngầm gửi vào argument là chính class gọi phương thức và ta sử dụng parameter cls để xử lí những vấn đề khác 
thì static method chẳng ngầm gửi cái gì vào cả, nó như một hàm bình thường.
'''
class Monhoc:
    slot = 30
    def __init__(self, paraten, paraslot_so, paragiang_vien):
        self.ten = paraten
        self.slot_so = paraslot_so
        self.giang_vien = paragiang_vien
    @staticmethod
    def hocvuive():
        print("Tôi rất vui khi học môn này")
CSI104 = Monhoc("CSI104", "Mot", "ABC")
CSI104.hocvuive()

#####################################
class Monhoc:
    slot = 30
    def __init__(self, paraten, paraslot_so, paragiang_vien):
        self.ten = paraten
        self.slot_so = paraslot_so
        self.giang_vien = paragiang_vien
    def hocvuive(self): # bỏ static method thì thêm self
        print("Tôi rất vui khi học môn này")
CSI104 = Monhoc("CSI104", "Mot", "ABC")
CSI104.hocvuive()

'''
khi nào dùng regular method, class method, static method thì bạn chỉ cần nhớ thế này:

Nếu bạn dựng một phương thức cần sử dụng đối tượng đó thì dùng regular method
Nếu bạn cần dùng class thì dùng class method
Trường hợp còn lại (tức là không dùng gì) thì dùng static method
luôn luôn dùng regular method cho lớp, lúc nào cũng có một parameter self cho dù trong phương thức đó chẳng bao giờ sử dụng tới. 
Điều này không sai, tuy nhiên khi đọc code sẽ thấy sự thiếu chuyên nghiệp.
'''