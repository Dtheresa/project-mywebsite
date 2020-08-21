from django.shortcuts import render
from django.utils import timezone
from .models import Book


def book_list(request):
    # # books = Book.objects.all()
    # comp_book = Book.objects.filter(end_date__lte=timezone.now()).order_by('end_date')
    # return render(request, 'books/book_list.html', {'comp_book': comp_book})

    # cr_book = Book.objects.filter(start_date__lte=timezone.now(), end_date=None)
    # return render(request, 'books/book_list.html', {'cr_book': cr_book})

    # tbr_book = Book.objects.filter(start_date=None, end_date=None)
    # return render(request, 'books/book_list.html', {'tbr_book': tbr_book})

    comp_book = Book.objects.filter(end_date__lte=timezone.now()).order_by('end_date')
    cr_book = Book.objects.filter(start_date__lte=timezone.now(), end_date=None)
    tbr_book = Book.objects.filter(start_date=None, end_date=None)
    return render(request, 'books/book_list.html', {'comp_book': comp_book, 'cr_book': cr_book, 'tbr_book': tbr_book})
