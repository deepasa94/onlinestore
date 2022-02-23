from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from owner.forms import BookForm,EmployeeForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from owner.models import Books,Employee
from django.utils.decorators import method_decorator
from customer.decorators import owner_permission_required
# Create your views here.
@method_decorator(owner_permission_required,name="dispatch")
class AddBookView(CreateView):
    model = Books
    form_class = BookForm
    template_name = "addbook.html"
    success_url =reverse_lazy("addbook")
    # def get(self,request,*args,**kwargs):
    #     form=BookForm()
    #     context={"form":form}
    #     return render(request,"addbook.html",context)
    # def post(self,request,*args,**kwargs):
    #     form=BookForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         print("saved")
    #         return render(request,"addbook.html")
    #     else:
    #         context={"form":form}
    #         return render(request,"addbook.html",context)
@method_decorator(owner_permission_required, name="dispatch")
class BookListView(ListView):
    model=Books
    context_object_name="books"
    template_name="booklist.html"
    # def get(self,request,*args,**kwargs):
    #     qs=Books.objects.all()
    #     context={"books":qs}
    #     return render(request,"booklist.html",context)
@method_decorator(owner_permission_required,name="dispatch")
class BookDetailView(DetailView):
    model=Books
    context_object_name ="book"
    template_name = "bookdetail.html"
    pk_url_kwarg='id'
    # def get(self,request,*args,**kwargs):
    #     print(kwargs)
    #     id=kwargs.get("id")
    #     qs=Books.objects.get(id=id)
    #     context={"book":qs}
    #     return render(request,"bookdetail.html",context)
@method_decorator(owner_permission_required,name="dispatch")
class BookChange(UpdateView):
    model=Books
    template_name = "bookedit.html"
    form_class = BookForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("booklist")



@method_decorator(owner_permission_required,name="dispatch")
class BookDeleteView(DeleteView):
    template_name = "bookdelete.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("booklist")
    model = Books
    context_object_name = "book"
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     qs=Books.objects.get(id=id)
    #     qs.delete()
    #     books=Books.objects.all()
    #     context={"book":qs,"books":books}
    #     return render(request,"booklist.html",context)
        # return redirect("booklist")

class AddEmployeeView(View):

    def get(self,request,*args,**kwargs):
        form=EmployeeForm()
        context={"form":form}
        return render(request,"addemployee.html",context)
    def post(self,request,*args,**kwargs):
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print("Saved")
            return render(request,"addemployee.html")
        else:
            context = {"form": form}
            return render(request, "addemployee.html", context)

class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        context={"emp":qs}
        return render(request,"employeelist.html",context)
class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        id=kwargs.get("id")
        qs=Employee.objects.get(id=id)
        context={"emp":qs}
        return render(request,"employeedetail.html",context)
class EmployeeEditView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        qs = Employee.objects.get(id=id)
        form=EmployeeForm(instance=qs)
        context={"form":form}
        return render(request,"employeeedit.html",context)
    def post(self,request,**kwargs):
        id=kwargs.get("id")
        qs = Employee.objects.get(id=id)
        form=EmployeeForm(request.POST,files=request.FILES,instance=qs)
        if form.is_valid():
            print("Inside save")
            form.save()
            return render(request,"mployeeedit.html.html")
        else:
            print("outside save")
            context={"form":form}
            return render(request,"employeeedit.html",context)
