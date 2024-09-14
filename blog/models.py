from django.db import models

NULLABLE = {'null': True,
            'blank': True}

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='blog-title')
    content = models.TextField(verbose_name='blog-content')
    preview = models.ImageField(upload_to='posts/', verbose_name='blog-preview', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0, verbose_name='blog-views')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        permissions = [
            ('can_edit_title', 'Can edit blog title'),
            ('can_edit_content', 'Can edit blog content'),
        ]
