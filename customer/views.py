from django.shortcuts import render,redirect
from django.http import HttpResponse
from owner.models import Books
from django.views.generic import View,ListView
from customer.forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from customer.decorators import sign_in_required
from django.utils.decorators import method_decorator
from customer.models import Carts
from django.db.models import Sum
# Create your views here.
@method_decorator(sign_in_required,name="dispatch")
class ListAllView(View):
    def get(self,request,*args,**kwargs):
            qs=Books.objects.all()
            context={"books":qs}
            return render(request,"customerhome.html",context)

class SignUpView(View):
    def get(self,request):
        form=UserRegistrationForm()
        context={"form":form}
        return render(request,"signup.html",context)
    def post(self,request):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"signup.html")
        else:
            context={"form":form}
            return render(request,"signup.html",context)
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        context={"form":form}
        return render(request,"signin.html",context)
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if request.user.is_superuser:
                    return redirect("booklist")
                else:
                    return redirect("allbooks")
            else:
                context={"form":form}
                return render(request,"signup.html",context)
def signout(request):
    logout(request)
    return redirect("signin")

class AddtoCartView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        book=Books.objects.get(id=id)
        user=request.user
        cart=Carts(user=user,item=book)
        cart.save()
        print("Item has been Added")
        return redirect("allbooks")
class CartItems(ListView):
    model = Carts
    template_name = "cartitems.html"
    context_object_name = 'items'
    def get(self,request,*args,**kwargs):
        qs= self.model.objects.filter(user=self.request.user).exclude(status="cancelled")
        total=qs.aggregate(Sum("item__price"))

        print(total)
        sum=total["item__price__sum"]
        context = {"items": qs,"sum":sum}
        return render(request,self.template_name,context)

class RemoveCartItem(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        cart=Carts.objects.get(id=id)
        cart.status="cancelled"
        cart.save()
        return redirect("allbooks")
