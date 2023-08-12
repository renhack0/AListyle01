from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib import messages


class ShoppingcardView(View):
    def get(self, content, son):
        savati = Savat.objects.filter(account__user=request.user)
        itemlar = SavatItem.objects.get(id=son)
        narx_sum = itemlar.aggregate(n=Sum('mahsulot__narx')).get('n')
        ch = 0
        for item in itemlar:
            ch += ((item.mahsulot.narx/100)*item.mahsulot.chegirma)*item.miqdor
            narx_sum += item.mahsulot.narx*item.miqdor
        savati.umumiy_summa = narx_sum - ch
        savati.save()
        content = {
            'savat': savati,
            'savatitem': itemlar,
            'total': narx_sum,
            'discount': ch,
            'price': narx_sum-ch
        }
        return render(request, 'page-shopping-cart.html', content)


class MiqdorKamaytir(View):
    def get(self, request, pk):
        item = SavatItem.objects.get(id=pk)
        item.miqdor -= 1
        item.summa -= item.mahsulot.narx
        item.save()
        return redirect('/buyurma/savat')


class MiqdorQosh(View):
    def get(self, request, pk):
        item = SavatItem.objects.get(id=pk)
        item.miqdor += 1
        item.summa += item.mahsulot.narx
        item.save()
        return redirect('/buyurma/savat/')


class SavatItemQosh(View):
    def get(self, reuqest, pk):
        savati = Savat.objects.get(account__user=reuqest.user)
        m = Mahsulot.objects.get(id=pk)
        savat_item = SavatItem.objects.filter(mahsulot=m, savat=savati)
        if len(savat_item) > 1:
            return redirect(f'/savat/mahsulot/{pk}/')
        SavatItem.objects.create(
            miqdor=1,
            mahsulot=m,
            savat=savati,
            summa=m.narx
        )
        return redirect(f'/asosiy/mahsulot/{pk}/')


class SavatItemOchir(View):
    def get(self, request, son):
        SavatItem.objects.get(id=son, savat__account__user=request.user).delete()
        return redirect("/buyurtma/savat/")


class BuyurmaQosh(View):
    def get(self, request, pk):
        Buyurtma.objects.create(
            savat=Savat.objects.get(id=pk),
            account=Account.objects.get(user=request.user),
            holat="Jarayonda",
            manzil=Manzil.objects.get(account__user=request.user, asosiy=True)
        )
        return redirect("/buyurtma/")


class ProfilOrders(View):
    def get(self, request):
        return render(request, 'page-profile-orders.html')


class ProfilTanlangan(View):
    def get(self, request):
        content = {
            "tanlanganlar": Tanlanganlar.objects.filter(account__user=request.user)
        }
        return render(request, 'page-profile-wishlist.html', content)


class TanlanganQosh(View):
    def get(self, request, son):
        Tanlanganlar.objects.create(
            mahsulot=Mahsulot.objects.get(id=son),
            account=Account.objects.get(user=request.user)
        )
        return redirect("/buyurtma/wishlist/")


class WishOchir(View):
    def get(self, request, son):
        Tanlanganlar.objects.get(id=son, account__user=request.user).delete()
        return redirect("/buyurtma/wishlist/")
