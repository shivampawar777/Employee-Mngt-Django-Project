# Generated by Django 5.1.7 on 2025-03-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdata',
            name='contact',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='empdata',
            name='dept',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='empdata',
            name='emp_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='empdata',
            name='idproof',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='empdata',
            name='jdate',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='empdata',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='empdata',
            name='state',
            field=models.CharField(max_length=200),
        ),
    ]
