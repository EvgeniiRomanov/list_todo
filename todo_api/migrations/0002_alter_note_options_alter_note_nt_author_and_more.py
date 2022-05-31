# Generated by Django 4.0.4 on 2022-05-31 13:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['nt_endtime'], 'verbose_name': 'Заметка', 'verbose_name_plural': 'Заметки'},
        ),
        migrations.AlterField(
            model_name='note',
            name='nt_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='note',
            name='nt_endtime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 13, 45, 42, 974853), verbose_name='Выполнить к:'),
        ),
    ]