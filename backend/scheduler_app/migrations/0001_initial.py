# Generated by Django 4.1.4 on 2022-12-22 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.CharField(max_length=100)),
                ('away', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('game_date', models.DateField()),
                ('game_time', models.TimeField()),
                ('note', models.TextField()),
            ],
        ),
    ]