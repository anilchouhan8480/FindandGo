# Generated by Django 2.1.7 on 2021-03-09 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0004_businessinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessinfo',
            name='biz_type',
        ),
        migrations.RemoveField(
            model_name='businessinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='BusinessInfo',
        ),
        migrations.DeleteModel(
            name='BusinessTypes',
        ),
    ]
