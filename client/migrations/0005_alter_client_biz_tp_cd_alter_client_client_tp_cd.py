# Generated by Django 4.0.1 on 2022-02-14 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_remove_codedt_code_id_codedt_code'),
        ('client', '0004_alter_client_biz_tp_cd_alter_client_client_tp_cd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='biz_tp_cd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='client_biz_tp_cd', to='common.codedt'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_tp_cd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='client_client_tp_cd', to='common.codedt'),
        ),
    ]
