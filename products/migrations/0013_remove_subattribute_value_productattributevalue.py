# Generated by Django 4.1.7 on 2023-04-19 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_productattribute_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subattribute',
            name='value',
        ),
        migrations.CreateModel(
            name='ProductAttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.attribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('subattribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.subattribute')),
            ],
            options={
                'unique_together': {('product', 'attribute', 'subattribute')},
            },
        ),
    ]
