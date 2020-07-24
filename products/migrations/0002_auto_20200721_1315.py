# Generated by Django 2.2.14 on 2020-07-21 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryfilter',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Category'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='cat_filter',
        ),
        migrations.AddField(
            model_name='product',
            name='cat_filter',
            field=models.ManyToManyField(to='products.CategoryFilter'),
        ),
    ]