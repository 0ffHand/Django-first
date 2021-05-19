from django.shortcuts import render
from sales_manager.models import Book


def main_page(request):
    query_set = Book.objects.all()
    context = {"query_set": query_set}
    return render(request, "sales_manager/index.html", context=context)


