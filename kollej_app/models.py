from django.db import models
from django.core.exceptions import ValidationError
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
def validate_file_size(value):
    filesize = value.size

    if filesize > 1000 * 2024:
        raise ValidationError("The maximum file size that can be uploaded is 2mb")
    else:
        return value

class Leadership(models.Model):
    full_name = models.CharField(max_length=56, verbose_name="To'liq isim")
    acceptions = models.CharField(max_length=56, verbose_name='Qabul kunlari')
    position = models.CharField(max_length=26, verbose_name='lavozim')
    phone_number = models.CharField(max_length=26, verbose_name='Telfon raqam')
    email = models.CharField(max_length=56)
    image = models.ImageField(upload_to='img/', validators=[validate_file_size])

    date_created = models.DateField(auto_now_add=True)
    date_update   = models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name


class News(models.Model):
    NEW_METHODS = [
        ("1", 'news'),
        ('2', 'events')
    ]

    new_type = models.CharField(
        max_length=20, default='1', choices=NEW_METHODS
    )
    image = models.ImageField(upload_to='img/', validators=[validate_file_size])
    body          = RichTextUploadingField(verbose_name='Yangilik matni')
    views         = models.IntegerField(default=0, verbose_name="ko'rishlar soni")
    title         = models.CharField(max_length=255, verbose_name="Sarlavha")


    date_created = models.DateField(auto_now_add=True)
    date_update   = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class Requisites(models.Model):
    college_name = models.CharField(max_length=100, verbose_name="kollej nomi")
    address       = models.CharField(max_length=100, verbose_name="manzil")
    phone         = models.CharField(max_length=100, verbose_name="tellfon raqam")
    email         = models.CharField(max_length=100, verbose_name="poschta manzil")
    bank_account  = models.CharField(max_length=100, verbose_name="bank hisob raqam")
    fax           = models.CharField(max_length=100)
    bank          = models.CharField(max_length=100)
    mfo           = models.CharField(max_length=100)
    INN           = models.CharField(max_length=100)
    OKONX         = models.CharField(max_length=100)
    date_created  = models.DateTimeField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.college_name

class OpenData(models.Model):

    OPEN_METHOD = [
        ("1", "ochiq ma'lumotlar"),
        ("2", "nizom")
    ]

    name       = models.CharField(max_length=255, verbose_name='hujat nomi')
    pdf_file   = models.FileField()
    open_method = models.CharField(max_length=20, choices=OPEN_METHOD)

    date_created  = models.DateTimeField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Directions(models.Model):
    name = models.CharField(max_length=120, verbose_name="Yo'nalish nomi")
    body = RichTextUploadingField(verbose_name="Yo'nalish matni")
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    