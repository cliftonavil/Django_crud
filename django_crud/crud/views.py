from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from crud.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'pages', 'price', 'publish_year', 'status']


def book_list(request):
    book = Book.objects.all()
    data = {}
    data['object_list'] = book
    return render(request, 'books/book_list.html', data)


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('crud:book_list')
    return render(request, 'books/book_form.html', {'form':form})


def book_update(request, pk):
    book= get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('crud:book_list')
    return render(request, 'books/book_form.html', {'form':form})

def book_delete(request, pk):
    book= get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('crud:book_list')

