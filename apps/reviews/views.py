from django.shortcuts import render
from rest_framework import generics

# local
from .serializers import ReviewSerializer
from .permissions import IsCustomer, IsStaves
from .models import Review

class CommentList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsStaves]

class AdminRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsStaves]


class CommentCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsCustomer]

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)