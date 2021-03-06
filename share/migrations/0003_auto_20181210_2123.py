# Generated by Django 2.1.2 on 2018-12-10 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_auto_20181210_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='serial_number',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='port',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='port',
            name='port_number',
            field=models.IntegerField(),
        ),
    ]
