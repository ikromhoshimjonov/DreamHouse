from django.db.models import Model, TextField, CharField, EmailField, ImageField, ForeignKey, CASCADE

class News(Model):
    description = TextField()
    sales_department = CharField(max_length=255)
    phone = CharField(max_length=255)
    email = EmailField()

class NewsImage(Model):
    image = ImageField(upload_to="new/image/")
    news = ForeignKey("new.News",on_delete=CASCADE,related_name="image")

class Advertising(Model):
    icon = ImageField(upload_to='advertising')

class SiteSettings(Model):
    email = EmailField()
    phone_number = CharField(max_length=255)
    address = CharField(max_length=255)




