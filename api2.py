from mongoengine import *
connect(host='mongodb+srv://admin:jackhammer@cluster0.q0a3b.mongodb.net/ZanebotDB?retryWrites=true&w=majority', port=27017)

class Users(Document):
    name = StringField(required=True)
    age = IntField(required=True)

Tim = Users(
    name = 'Tim',
    age = 60
)
Tim.save()
print(Tim.name)
print(Tim.age)
print(Users.objects.first()["age"])