from django.db.models import Model, CharField, TextField, TextChoices, ForeignKey, SET_NULL, DecimalField, IntegerField, \
    FileField, DateField, ImageField, CASCADE, BooleanField, EmailField


class Home(Model):
    class StatusType(TextChoices):
        RENT = "rent" , "Rent"
        SALE = "sale" , "Sale"

    class StatusProperty(TextChoices):
        BOYS =   "boys"   , "Boys"
        GIRLS =  "girls"  , "Girls"
        FAMILY = "family" , "Family"

    class StatusHome(TextChoices):
        OFFICE = "office",  "Office"
        VILLA =  "villa" ,  "Villa"
        SHOP  =  "shop"  ,  "Shop"


    name = CharField(max_length=255)
    description = TextField()
    property_code = CharField(max_length=255)
    price = DecimalField(max_digits=15,decimal_places=2)
    beds = IntegerField()
    baths = IntegerField()
    volume = CharField(max_length=255)
    build = CharField(max_length=255)
    garage = IntegerField()
    country = CharField(max_length=255)
    state = CharField(max_length=255)
    area = CharField(max_length=255)
    documents = FileField(upload_to='documents/')
    latitude = DecimalField(max_digits=9,decimal_places=6)
    longitude = DecimalField(max_digits=9,decimal_places=6)
    date = DateField(auto_now=True)
    status = CharField(max_length=255,choices=StatusType)
    property = CharField(max_length=255,choices=StatusProperty)
    status_home = CharField(max_length=255,choices=StatusHome)
    sale = BooleanField(default=True)


    city = ForeignKey("home.City", on_delete=SET_NULL, null=True, blank=True, related_name="home")
    contact = ForeignKey("home.Contact",on_delete=CASCADE)

class City(Model):
    name = CharField(max_length=255)
    image = ImageField(upload_to="image/")

    def __str__(self):
        return self.name

class HomeImage(Model):
    image = ImageField(upload_to="home/")
    home = ForeignKey("home.Home",on_delete=CASCADE,related_name="image")

class Amenities(Model):
    name = CharField(max_length=255)

class AmenitiesHome(Model):
    amenities = ForeignKey("home.Amenities", on_delete=CASCADE,related_name="amenities")
    home = ForeignKey("home.Home", on_delete=CASCADE,related_name="amenities_home")

class Contact(Model):
    name = CharField(max_length=255)
    email = EmailField()
    phone = CharField(max_length=30)
    avatar = CharField(max_length=255)

    def __str__(self):
        return self.name
