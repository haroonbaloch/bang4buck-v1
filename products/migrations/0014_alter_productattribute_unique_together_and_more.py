# Generated by Django 4.1.7 on 2023-04-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_subattribute_value_productattributevalue'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productattribute',
            unique_together={('product', 'attribute', 'subattribute')},
        ),
        migrations.AddField(
            model_name='productattribute',
            name='value',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductAttributeValue',
        ),
    ]
