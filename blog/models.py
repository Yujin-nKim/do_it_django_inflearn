from django.db import models

# Create your models here.

# models의 Model을 이용해 모델 생성(django가 제공하는 기능 사용)
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True) #새로만들어졌을때 현재 시간으로
    updated_at = models.DateTimeField(auto_now=True)
    # author: 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.title}'