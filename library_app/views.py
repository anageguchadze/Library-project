from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.
class AuthorViewSet(viewsets. ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets. ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer