# Generated by Django 4.0.1 on 2022-02-18 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0007_user_staff_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]