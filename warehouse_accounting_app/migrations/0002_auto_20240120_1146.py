# Generated by Django 3.2.23 on 2024-01-20 08:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_accounting_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Место хранения',
                'verbose_name_plural': 'Места хранения',
            },
        ),
        migrations.AlterModelOptions(
            name='cargo',
            options={'verbose_name': 'Груз', 'verbose_name_plural': 'Грузы'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-number'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='cargo',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cargoes', to='warehouse_accounting_app.order', verbose_name='Заказ'),
        ),
    ]
