from django.db import models
from asosiy.models import Mahsulot
from userapp.models import Account


class Tanlangan(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Savat(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    umumiy_summa = models.PositiveSmallIntegerField()
    sana = models.DateField()
    atatus = models.CharField(max_length=30)

    # def save(self, *args, **kwargs):
    #     svat_items = SavatItem.objects.filter(savat__id=self.id)
    #     summa = 0
    #     for item in svat_items:
    #         ch = (item.mahsulot.narx/100)*item.mahsulot.chegirma
    #         narxi = item.mahsulot.narx - int(ch)
    #         narxi= narxi*item.miqdor
    #         summa += narxi
    #     self.umumiy_summa = summa
    #     super(Savat, self).save(*args, **kwargs)


class SavatItem(models.Model):
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE, related_name='itemlari')
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField()
    summa = models.PositiveSmallIntegerField()

    # def save(self, *args, **kwargs):
    #     ch = (self.mahsulot.narx / 100) * self.mahsulot.chegirma
    #     narxi = self.mahsulot.narx - int(ch)
    #     self.summa = narxi*self.miqdor
    #     savat = Savat.objects.get(id=self.savat.id)
    #     savat.save()
    #     super(SavatItem, self).save(*args, **kwargs)


class Manzil(models.Model):
    davlat = models.CharField(max_length=50)
    shahar = models.CharField(max_length=50)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    manzil = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    asosiy = models.BooleanField(default=True)


class Buyurtma(models.Model):
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    holat = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
