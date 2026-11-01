from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from models import Question
from .api.serializers import QuestionSerializer
from django.contrib.auth.models import User


class LiketTests(APITestCase):

    # def test_get_like(self):
    #     url = reverse("like-list")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_likes(self):
            url = reverse("like-list")
            # url = "http://127.0.0.1:8000/api/forum/likes/"
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

class QuestionTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.question = Question.objects.create(title="Test Question", content="Test content", author=self.user, category="frontend")

    def test_detail_question(self):
        url = reverse("question-detail", kwargs={"pk" : self.question.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
       