# Generated by Django 5.1.1 on 2024-09-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(verbose_name='blog-content'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='blog-preview'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='blog-title'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='blog-views'),
        ),
    ]
