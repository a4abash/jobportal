# Generated by Django 2.2.4 on 2019-09-23 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0004_jobseeker_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='full_name',
            field=models.CharField(default='Ram', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cv/'),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
