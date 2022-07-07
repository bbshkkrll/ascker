from django.db import models


class File(models.Model):
    original_size = models.CharField(max_length=24, verbose_name='Оригинальный размер')
    converted_size = models.CharField(max_length=24, verbose_name='Размер после конвертации', auto_created=True)
    original_img = models.FileField(upload_to='originals/%m/%d/', verbose_name='Original image')
    converted_img = models.FileField(upload_to='converted/%m/%d/', verbose_name='Converted image')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['original_size']

    def __str__(self):
        return f'File with size {self.original_size}'


class ConvertRequest(models.Model):
    username = models.EmailField()
    image = models.OneToOneField(File, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Запрос на конвертацию'
        verbose_name_plural = 'Запросы на конвертацию'
        ordering = ['created_at']

    def __str__(self):
        return f'Request from {self.username}'
