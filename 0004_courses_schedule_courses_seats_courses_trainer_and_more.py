# Generated by Django 4.2.4 on 2023-08-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_homemotto_title_homemotto_titlee'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='schedule',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='courses',
            name='seats',
            field=models.IntegerField(blank=True, default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courses',
            name='trainer',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='courses',
            name='money',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='courses',
            name='personname',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]