# Generated by Django 2.1.3 on 2019-05-29 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personal_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244)),
                ('fathername', models.CharField(max_length=244)),
                ('address', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('ph', models.IntegerField()),
            ],
        ),
    ]