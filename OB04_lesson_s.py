# Пример без использования принципа единственной ответственности

"""class UserManager():
    def __init__(self,user):
        self.user = user
    def change_user_name(self, user_name):
        self.user = user_name
    def save_user(self):
        file = open("users.txt", "a")
        file.write(self.user)
        file.close()
это созданн класс, который работает с 
изменением имени и сохраняет данные пользователя"""
# Делаем это же с соблюдением принциав единственной ответственности.

class User():
    def __init__(self,user):
        self.user = user
class UserNameVhanger():
    def __init__(self,user):
        self.user = user
    def change_name(self,new_name):
        self.user = new_name
class SaveUser():
    def __init__(self,user):
        self.user = user
    def save(self):
        file = open("users.txt", "a")
        file.write(self.user)
        file.close()
        

                    
