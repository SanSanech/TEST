class User:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
        
    def add_to_txt(self):
        with open("data.txt", "w") as file:
            file.write(self.name)
    
    
user_1 = User("Alex", "awdqw@yandex.ru")

user_1.add_to_txt()

print("dwqdq")