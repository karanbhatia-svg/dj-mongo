# Generated by Django 4.1.9 on 2023-05-18 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('date_of_joining', models.DateField()),
            ],
        ),
    ]
