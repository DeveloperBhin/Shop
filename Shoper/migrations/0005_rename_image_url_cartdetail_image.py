# Generated by Django 5.1.1 on 2024-11-12 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shoper', '0004_rename_productdetail_cartdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdetail',
            old_name='image_url',
            new_name='Image',
        ),
    ]
