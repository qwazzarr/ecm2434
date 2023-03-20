# Generated by Django 4.1.7 on 2023-03-20 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_pendingfriendinvite'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='profile_pic', to='database.shopitem'),
        ),
        migrations.AlterField(
            model_name='shopitem',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]