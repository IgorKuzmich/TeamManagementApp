# Generated by Django 2.2.6 on 2019-10-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamapp', '0002_emailurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailurl',
            name='id',
        ),
        migrations.AlterField(
            model_name='emailurl',
            name='URL',
            field=models.CharField(help_text='Enter school email url', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
