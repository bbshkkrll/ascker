from django.db import models


class File(models.Model):
    original_size = models.CharField('Original size', max_length=24)
    converted_size = models.CharField('Converted size', max_length=24)
    original_img = models.FileField('Original size', upload_to='originals/%m/%d/')
    converted_img = models.FileField('Converted size', upload_to='converted/%m/%d/')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class ConvertRequest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.OneToOneField(File)

    class Meta:
        verbose_name = 'Convert request'
        verbose_name_plural = 'Convert requests'
