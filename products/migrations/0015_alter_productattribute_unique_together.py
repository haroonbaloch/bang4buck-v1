# Generated by Django 4.1.7 on 2023-04-22 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_productattribute_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productattribute',
            unique_together=set(),
        ),
    ]
