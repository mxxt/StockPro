# Generated by Django 2.2 on 2019-05-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockBasicTradeCal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.CharField(max_length=5)),
                ('cal_date', models.CharField(max_length=10)),
                ('is_open', models.CharField(max_length=2)),
                ('pretrade_date', models.CharField(max_length=10)),
            ],
        ),
    ]