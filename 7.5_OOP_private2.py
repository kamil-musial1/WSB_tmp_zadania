from oop7_4_OOP_private1 import User, Date

user1 = User('123@wp.pl', 12345)
print(user1.mail)
user1.wyswietl_id()

user1.mail = '123$yaghoo.com'
print(user1.mail)

user1.__id = 56778
user1.wyswietl_id()

user1.zmien_id(567788)
user1.wyswietl_id()


date1 = Date(11, 2, 2029)
print(date1)
date1.zmien_date(12, 666, 2029)
print(date1)

