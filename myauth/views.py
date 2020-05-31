from django.shortcuts import render
from django.http import HttpResponse
from myauth.forms import LoginForm

def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:
            return HttpResponse('잘못됨')
    else:
        form = LoginForm()
    return render(request, 'myauth/login.html', {'form': form})
            