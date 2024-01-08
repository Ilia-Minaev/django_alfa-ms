# Generated by Django 5.0 on 2024-01-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_alter_order_city_alter_order_email_alter_order_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-id',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AddField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('1', 'Заказ из корзины'), ('2', 'Купить в 1 клик'), ('3', 'Обратный звонок'), ('4', 'Консультация')], default='1', max_length=127, verbose_name='Тип заказа'),
        ),
    ]
