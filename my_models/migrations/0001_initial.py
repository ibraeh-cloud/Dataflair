# Generated by Django 3.0.1 on 2020-05-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('shirt_size', models.CharField(choices=[('L', 'LARGE'), ('M', 'MEDIUM'), ('S', 'SMALL')], max_length=1)),
            ],
        ),
    ]
