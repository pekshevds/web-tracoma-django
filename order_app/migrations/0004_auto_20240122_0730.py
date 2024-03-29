# Generated by Django 3.2.23 on 2024-01-22 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0003_auto_20240122_0721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contractor',
            options={'ordering': ['name'], 'verbose_name': 'Контрагент', 'verbose_name_plural': 'Контрагенты'},
        ),
        migrations.AlterField(
            model_name='order',
            name='recipient_name',
            field=models.CharField(default='', max_length=150, verbose_name='Наименование получателя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sender_name',
            field=models.CharField(default='', max_length=150, verbose_name='Наименование отправителя'),
        ),
    ]
