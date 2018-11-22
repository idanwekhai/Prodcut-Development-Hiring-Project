# Generated by Django 2.1.2 on 2018-11-21 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('field_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=260, null=True)),
                ('required', models.NullBooleanField()),
                ('field_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='field_types.FieldType')),
            ],
        ),
    ]
