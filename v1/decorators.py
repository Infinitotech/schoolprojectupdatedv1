from django.shortcuts import redirect


def login_required(view_func):
    def wrapper(self,request):
        try:
            if request.session['user']['authenticate'] == True:
                return view_func(self,request)
            else:
                return redirect('/login')
        except Exception:
            return redirect('/login')
    return wrapper
