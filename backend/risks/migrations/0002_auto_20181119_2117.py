# Generated by Django 2.1.2 on 2018-11-19 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='description',
            field=models.CharField(max_length=260, null=True),
        ),
    ]
