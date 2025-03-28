# Generated by Django 5.1.7 on 2025-03-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homeapp', '0009_delete_empdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=200)),
                ('working', models.BooleanField(default=True)),
                ('jdate', models.CharField(max_length=200)),
                ('ldate', models.CharField(max_length=200)),
                ('dept', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('add', models.CharField(max_length=1500)),
                ('state', models.CharField(max_length=200)),
                ('idproof', models.CharField(max_length=200)),
            ],
        ),
    ]
