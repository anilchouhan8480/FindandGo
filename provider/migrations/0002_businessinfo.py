# Generated by Django 2.1.7 on 2021-03-04 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FindandGo', '0001_initial'),
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('passwd', models.IntegerField()),
                ('street', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
                ('dated', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FindandGo.UserProfile')),
                ('biz_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.BusinessTypes')),
            ],
        ),
    ]