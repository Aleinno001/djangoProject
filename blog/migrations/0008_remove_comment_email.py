# Generated by Django 4.2.1 on 2023-05-25 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
