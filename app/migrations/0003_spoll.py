# Generated by Django 3.0.6 on 2020-06-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200615_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opt', models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3)),
            ],
        ),
    ]
