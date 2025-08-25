from django.urls import path
from .views import BookListView
from . import views

# urlpatterns = [
#     path("", views.BookListView.as_view(), name="book_list"),
#     path("new/", views.BookCreateView.as_view(), name="book_create"),
#     path("<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
# ]

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("new/", views.BookCreateView.as_view(), name="book_create"),
    path("<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("<int:pk>/edit/", views.BookUpdateView.as_view(), name="book_update"),
    path("<int:pk>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
]
