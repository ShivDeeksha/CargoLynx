# Generated by Django 5.0.4 on 2024-04-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customclearanceagent',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='user',
        ),
        migrations.RemoveField(
            model_name='transporter',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='license_image',
            field=models.FileField(blank=True, null=True, upload_to='documents/liscence'),
        ),
        migrations.DeleteModel(
            name='Carrier',
        ),
        migrations.DeleteModel(
            name='CustomClearanceAgent',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.DeleteModel(
            name='Transporter',
        ),
    ]