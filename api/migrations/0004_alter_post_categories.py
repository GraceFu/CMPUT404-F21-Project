# Generated by Django 3.2.7 on 2021-12-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_inbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
