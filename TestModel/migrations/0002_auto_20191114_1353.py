# Generated by Django 2.2.7 on 2019-11-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('session_id', models.CharField(max_length=16)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
