from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    '''Данные о записи (посте)'''
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст записи')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    data = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y', blank=True, null=True)

    def str(self):
        return f'{self.title}, {self.author.username}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Comments(models.Model):
    '''Комментарий'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    def str(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'