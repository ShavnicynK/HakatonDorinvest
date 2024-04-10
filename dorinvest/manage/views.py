from django.shortcuts import render


def manage_page(request):

    return render(request, "manage/manage_page.html", {})