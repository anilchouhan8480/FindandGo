# Generated by Django 2.1.7 on 2021-03-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0008_remove_businessinfo_passwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinfo',
            name='biz_img',
            field=models.ImageField(blank=True, upload_to='business_images'),
        ),
    ]