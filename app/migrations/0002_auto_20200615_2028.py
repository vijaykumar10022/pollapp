# Generated by Django 3.0.6 on 2020-06-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='No',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='yes',
        ),
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.CharField(max_length=100, null=True),
        ),
    ]