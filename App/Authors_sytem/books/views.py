from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BookCredential
from django.urls import reverse_lazy

class BookListView(ListView):
    model = BookCredential
    template_name = "books/book_list.html"  # match template path  
    context_object_name = "books"

class BookDetailView(DetailView):
    model = BookCredential
    template_name = "books/book_detail.html"
    context_object_name = "book"

class BookCreateView(CreateView):
    model = BookCredential
    template_name = "books/book_form.html"
    fields = ["b_name", "chapter", "summary", "ch_content", "author", "status"]
    success_url = reverse_lazy("book_list")
    
class BookUpdateView(UpdateView):
    model = BookCredential
    fields = ["b_name", "chapter", "summary", "ch_content", "author", "status"]
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book_list")

class BookDeleteView(DeleteView):
    model = BookCredential
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy("book_list")