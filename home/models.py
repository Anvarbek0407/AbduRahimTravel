from django.db import models

# Create your models here.
class Contient(models.Model):
    image = models.ImageField(upload_to='contient/',verbose_name="Rasmi")
    name = models.CharField(max_length=250,verbose_name="Ismi")
    def __str__(self):
        return(self.name)



class DealInclude(models.Model):
    icon = models.CharField(max_length=250,verbose_name="ikon")
    name = models.CharField(max_length=250,verbose_name="ismi")
    def __str__(self):
        return(self.name)


class CityTown(models.Model):
    image = models.ImageField(upload_to='citytown/',verbose_name="Rasmi")
    name = models.CharField(max_length=250,verbose_name="ismi")
    prince = models.PositiveSmallIntegerField(verbose_name="narxi")
    people = models.PositiveSmallIntegerField(verbose_name="odamlar")
    deal_includes = models.ManyToManyField(DealInclude,verbose_name="kelishuvlar")
    phone = models.CharField(max_length=250,verbose_name="telefon")
    email = models.EmailField(verbose_name="email")
    address = models.CharField(max_length=250,verbose_name="adres")
    lotation =  models.TextField(verbose_name="lotatsiya")
    days =  models.PositiveSmallIntegerField(verbose_name="kunlar")
    address_iframe = models.TextField(null=True,verbose_name="adres iframe")
    def __str__(self):
        return(self.name)


class Country(models.Model):
    image = models.ImageField(upload_to='country/',verbose_name="Rasmi")
    name = models.CharField(max_length=250,verbose_name="ismi")
    populations = models.PositiveSmallIntegerField(verbose_name="populyatsiyalar")
    terytory = models.PositiveSmallIntegerField(verbose_name="hudud")
    avg_price = models.PositiveSmallIntegerField(verbose_name="avg narxi")
    title = models.CharField(max_length=250,verbose_name="yozuv")
    continent = models.ForeignKey(Contient, on_delete=models.CASCADE,verbose_name="qit'a")
    cities_towns = models.ManyToManyField(CityTown,verbose_name="mashhur joylari")
    map_image = models.ImageField(upload_to='map_image/',verbose_name="xarita rasmi")
    total_guest_yearly = models.PositiveSmallIntegerField(verbose_name="yillik mehmonlar")
    amazing_places = models.PositiveSmallIntegerField(verbose_name="ajoyib joylar")
    amazing_acc = models.PositiveSmallIntegerField(verbose_name="ajoyib ass")
    in_yearly = models.PositiveSmallIntegerField(verbose_name="yil ichida")
    content = models.CharField(max_length=250,verbose_name="content")
    def __str__(self):
        return(self.name)

class NumberofGuest(models.Model):
    name = models.CharField(max_length=250,verbose_name="ismi")
    def __str__(self):
        return (self.name)



class Reservation(models.Model):
    name = models.CharField(max_length=250,verbose_name="ismi")
    phone = models.PositiveSmallIntegerField(verbose_name="telefon")
    data = models.DateField(verbose_name="sana")
    numberofguest = models.ForeignKey(NumberofGuest, on_delete=models.CASCADE,verbose_name="mehmon soni")
    direction = models.ForeignKey(CityTown, on_delete=models.CASCADE,verbose_name="yo'nalish")
    def __str__(self):
        return(self.name)

class Price_Range(models.Model):
    startprice = models.PositiveSmallIntegerField(verbose_name="boshlang'ich narxi")
    endprice  = models.PositiveSmallIntegerField(verbose_name=" max narxi")



