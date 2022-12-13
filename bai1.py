# Lớp là gì?
'''
Nói đơn giản nó giống như là một bản mẫu, một khuôn mẫu. 
Ở đó ta khai báo các thuộc tính (attribute) và phương thức (method) nhằm miêu tả để từ đó ta tạo ra được những object (đối tượng)
đôi khi object người ta cũng có thể ghi là instance, tuy nó không sát nghĩa cho lắm
'''
'''
Cú pháp để tạo một lớp
class <tên_lớp>:

    # code
'''
class zaonek:
    pass

Zao = zaonek()
print(Zao)
'''
__main__.zaonek nghĩa là đây là đối tượng thuộc lớp zaonek ở hàm main (có nghĩa là ở file ta đang chạy thực thi) 
kèm theo cái nơi cư trú của nó – thứ mà ta không cần bận tâm lắm lúc này.
'''

# Thuộc tính là gì?
'''
Khi khai báo thuộc tính cho một đối tượng, bạn phải nghĩa ra những thuộc tính để mà giúp ta có thể phân biệt nó với những đối tượng 
khác cùng lớp, ví dụ như giữa 2 thằng con trai đừng lấy giới tính ra để phân biệt mà nên dùng hơn là sử dụng tên.
Lưu ý là thuộc tính nào có mới lấy ra được , chứ cái class của chúng ta không tự động sinh ra thuộc tính đâu

'''

class zaonek:
    pass

Zaocute = zaonek()

Zaocute.name = " Giau "
Zaocute.age = " 20 "
Zaocute.pet = " cat "

print(" My name is ", Zaocute.name)
print(" YOB is ", Zaocute.age)
print(" My pet is ", Zaocute.pet)


# Hàm constructor (initialize method)
'''
Ví dụ ta cần khai báo khoảng 1000 người. Giả sử một người có 5 thuộc tính như trên vị chi ta sẽ mất 5000 dòng khai báo. 
Tuy là bạn vẫn có thể khai báo chỉ bằng 1000 dòng bằng cách khai báo one-liner của Python tuy nhiên đôi lúc những thuộc tính của 
đối tượng không dễ dàng để khai báo một cách đơn giản như vậy.
Ta cần phải cần một cái khuôn mẫu mà chỉ cần đưa các giá trị thuộc tính vào còn việc gán giá trị thì để cho khuôn mẫu làm. 
Dĩ nhiên khuôn mẫu có thể, nếu ta xây dựng cho nó một hàm constructor.

Lưu ý: 2 dấu gạch “_” bắt đầu và kết thúc
'''

class Nguoidung:
    def __init__(self):
        pass
# def __init__(self):  hàm được đặt dưới dạng constructor - Trong Python, một số hàm trong lớp sẽ được tự động gọi khi ta 
#                      khai báo một đối tượng và constructor là một trong số những hàm đó
# Từ khóa self hay cụ thể ở đây là parameter self là một quy ước 
# (lưu ý là hoàn toàn sẽ không bị bắt lỗi cú pháp nếu dùng từ khóa khác), bạn có thể dùng một từ khóa khác
#  Ý nghĩa của self là chính đối tượng đó.
'''
từ khóa self sẽ nhận giá trị chính là đối tượng đã  gọi hàm đó
Hàm __init__ có đối tượng nào gọi đâu? Đương nhiên là không cần gọi, nó đã được tự động gọi khi bạn khởi tạo đối tượng rồi
Ví dụ khi dùng class Nguoidung khởi tạo Nguoidung1 thì mặc định bạn đã kêu Nguoidung1 gọi hàm __init__
Và self được gán là đối tượng Nguoidung1 với 1 số thuộc tính như "A", "20", "District1" được truyền vào theo thứ tự
'''

'''
nhớ rằng mỗi khi có một đối tượng nào đó gọi một hàm thì luôn luôn tối thiểu sẽ có một argument được gửi vào hàm đó chính là 
chính đối tượng đó, nếu hàm đó không có parameter nhận thì sẽ sinh lỗi, còn nếu dư argument 
(vì ta không lường trước được có một argument là chính đối tượng được ngầm gửi vào) thì vẫn sẽ có lỗi tràn argument. 
Còn nếu mà gửi vào vẫn không có lỗi thì…Bug này nặng khó fix đây.
'''
class Nguoidung:
    def __init__(self, name, age, district):
        self.name = name
        self.age = age
        self.district = district

Nguoidung1 = Nguoidung("A", "20", "District1")

print("My name is", Nguoidung1.name)
print("My age is", Nguoidung1.age)
print("Live in", Nguoidung1.district)


# Phương thức là gì?

class Nguoidung:
    def __init__(self, name, age, district):
        self.name = name
        self.age = age
        self.district = district
    def chaodon(self):
        return " Chào đón tuổi" + self.age
Nguoidung1 = Nguoidung("A", "20", "District1")

print("My name is", Nguoidung1.name)
print("My age is", Nguoidung1.age)
print("Live in", Nguoidung1.district)
print(Nguoidung1.chaodon())                 # vì nó là hàm nên nhớ là hãy thêm () để gọi hàm
print(Nguoidung.chaodon(Nguoidung1))        # một cách gọi khác nhưng rất không phổ biến
