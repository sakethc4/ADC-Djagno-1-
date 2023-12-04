from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AppDevClubReviewsView(APIView):
        reviews = [
            'app dev is great',
            'you should join',
            'hello world',
            'intro to django'
        ]
        return Response({'reviews': reviews})

    def get(self, request):
        return Response({'reviews': self.reviews})

    def post(self, request):
        new_review = request.data.get('review', None)
        if new_review is not None: 
            self.reviews.append(new_review)
        


