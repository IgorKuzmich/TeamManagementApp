# Generated by Django 2.2.6 on 2019-11-07 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teamapp', '0012_auto_20191107_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_leader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teamapp.Student'),
            preserve_default=False,
        ),
    ]