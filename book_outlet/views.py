from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg


# Create your views here.


def index(request):
    books = Book.objects.all().order_by('-rating')
    books_num = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'books_num': books_num,
        'avg_rating': avg_rating
    })


def book_details(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_details.html', vars(book))
