# Generated by Django 2.2.5 on 2019-12-05 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechatAPP', '0004_auto_20191203_2033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activitymessage',
            options={'ordering': ['-createTime']},
        ),
        migrations.RenameField(
            model_name='groupmember',
            old_name='userID',
            new_name='openID',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='hasNewMessage',
        ),
        migrations.AddField(
            model_name='takepartin',
            name='hasNewMessage',
            field=models.CharField(default='0', max_length=5),
        ),
    ]
