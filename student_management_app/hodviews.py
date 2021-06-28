from django.shortcuts import render


def showpage(request):
    return render(request,'hod_template/home_content.html')