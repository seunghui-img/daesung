# Generated by Django 4.0.1 on 2022-02-14 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corp', '0001_initial'),
        ('acc', '0005_alter_user_corp_remove_user_staff_tp_cd_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='staff_tp_cd',
        ),
        migrations.AlterField(
            model_name='user',
            name='corp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_corp', to='corp.corp'),
        ),
    ]
