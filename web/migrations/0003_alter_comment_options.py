# Generated by Django 4.0.5 on 2022-06-16 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
    ]
