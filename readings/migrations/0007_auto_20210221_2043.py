# Generated by Django 3.1.1 on 2021-02-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0006_auto_20201129_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]