# Generated by Django 3.1.7 on 2021-04-02 04:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0010_businessinfo_mobile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainsite', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('message', models.TextField(max_length=800)),
                ('biz_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.businessinfo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
