# Generated by Django 4.0.1 on 2022-02-14 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0002_user_account_user_address_user_address2_user_bank_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='corp_no',
            new_name='corp',
        ),
    ]