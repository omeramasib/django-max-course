# Generated by Django 4.1 on 2022-10-13 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0008_rename_address_addres'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Addres',
            new_name='Address',
        ),
    ]
