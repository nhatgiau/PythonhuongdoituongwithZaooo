# Tạo lớp kế thừa
class Game:
    pass

class GameLMHT(Game):
    pass

game_lmht = GameLMHT()
print(game_lmht)
'''
Lớp này có đặc điểm là một lớp nâng cấp của lớp trên
Có nghĩa là nó có nhiều thứ mà lớp trên chưa có.
'''

# Kế thừa thuộc tính
class Game:
    gamenap = 100
    pass

class GameLMHT(Game):
    pass

game_lmht = GameLMHT()
print(game_lmht.gamenap)
'''
Kế thừa từ lớp trên, lớp trên có gì lớp dưới có đó
'''
'''
Giả sử như bạn không muốn thừa hưởng giá trị từ lớp ta kế thừa thì phải làm sao
----> Viết lại
'''
class Game:
    gamenap = 100
    pass

class GameLMHT(Game):
    gamenap = 500
    pass
    
game_lmht = GameLMHT()
print(game_lmht.gamenap)



# Kế thừa hàm constructor
class Game:
    gamenap = 100
    def __init__(self,rank,banbe,giochoi):
        self.Rank = rank
        self.Banbe = banbe
        self.Giochoi = giochoi

class GameLMHT(Game):
    gamenap = 500
    pass
    
game_lmht = GameLMHT("Đồng","56","100")
print(game_lmht.__dict__)
print(game_lmht.gamenap)
'''
Cha có constructor nên con có constructor
Nếu muốn thêm constructor riêng cho con thì thêm vào con ( ghi lại hết của cha và thêm constructor cần)
Hoặc ngắn gọn bằng cách dùng super
'''
class Game:
    gamenap = 100
    def __init__(self,rank,banbe,giochoi):
        self.Rank = rank
        self.Banbe = banbe
        self.Giochoi = giochoi

class GameLMHT(Game):
    gamenap = 500
    def __init__(self,rank,banbe,giochoi,thidau):
    super().__init__(rank,banbe,giochoi)
    self.Thidau = thidau
    
game_lmht = GameLMHT("Đồng","56","100")
print(game_lmht.__dict__)
print(game_lmht.gamenap)


# Kế thừa phương thức
'''
Hoàn toàn tương tự như kế thừa thuộc tính. Nếu lớp trước có những phương thức gì, bạn được kế thừa toàn bộ. 
Nếu bạn muốn thêm thì viết thêm ở lớp kế thừa. Còn nếu muốn chỉnh sửa, thì ta viết lại phương thức đó
'''