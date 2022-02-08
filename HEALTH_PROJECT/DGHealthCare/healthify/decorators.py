from django.shortcuts import redirect

def custom_login_required(func):
    def wrapper(*args,**kwargs):
        #print(dir(args[0].user))
        if args[0].user.is_authenticated:
            return func(*args,**kwargs)
        return redirect('login')
    return wrapper
