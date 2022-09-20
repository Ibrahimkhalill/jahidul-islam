# Generated by Django 4.1.1 on 2022-09-18 05:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesaage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.TextField()),
                ('subject', models.TextField()),
                ('text', models.TextField()),
                ('date_timefield', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]