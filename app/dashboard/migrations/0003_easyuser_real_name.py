# Generated by Django 4.2.10 on 2024-03-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_easyuser_goal_score_easyuser_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='easyuser',
            name='real_name',
            field=models.CharField(default='default name', max_length=255),
            preserve_default=False,
        ),
    ]
