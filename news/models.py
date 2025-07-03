from django.db import models
from django.urls import reverse

# Create your models here.

class novost(models.Model):
    title = models.CharField('Название', max_length=75, default = 'Новый пост')
    intro = models.CharField('Анонс', max_length=250, default = 'Текст анонса')
    text = models.TextField('Пост')
    date = models.DateField('Дата публикации поста')
    image = models.ImageField(upload_to='main/img/post_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
