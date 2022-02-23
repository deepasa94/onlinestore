from django.shortcuts import redirect

def sign_in_required(fun):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            # fun(request,*args,**kwargs)
            return redirect("signin")
        else:
            return fun(request,*args,**kwargs)
    return wrapper
def owner_permission_required(fun):
    def wrapper(request,*args,**kwargs):
        if request.user.is_superuser:
            return fun(request,*args,**kwargs)
        else:
            return redirect("signin")
    return wrapper