# Generated by Django 5.0.1 on 2024-01-30 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deepapp', '0003_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
