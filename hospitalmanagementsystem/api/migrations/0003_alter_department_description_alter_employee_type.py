# Generated by Django 4.1.3 on 2022-11-06 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_client_email_remove_client_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='type',
            field=models.CharField(choices=[('D', 'Doctor')], max_length=1),
        ),
    ]
