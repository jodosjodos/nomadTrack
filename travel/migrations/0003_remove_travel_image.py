# Generated by Django 4.0.5 on 2024-10-24 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travel',
            name='image',
        ),
    ]
