# Generated by Django 4.1.7 on 2023-02-25 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_stockmanagement_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmanagement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
