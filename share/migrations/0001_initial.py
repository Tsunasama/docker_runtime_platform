# Generated by Django 2.1.2 on 2018-12-10 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='subscription',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_user', to='share.User'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='share.User'),
        ),
        migrations.AddField(
            model_name='container',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.Image'),
        ),
        migrations.AddField(
            model_name='container',
            name='port',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.Port'),
        ),
        migrations.AddField(
            model_name='container',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.User'),
        ),
    ]
