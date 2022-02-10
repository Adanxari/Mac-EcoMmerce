# Generated by Django 4.0.1 on 2022-02-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=1000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
