# Generated by Django 4.1.2 on 2022-10-14 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_devices_os_deviceinfo_browser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=300)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='device_type',
            field=models.SmallIntegerField(choices=[(1, 'موبایل'), (2, 'تبلت'), (3, 'کامپیوتر'), (4, 'لمسی'), (5, 'بات'), (6, 'نامشخص')], default=6),
        ),
    ]
