# Generated by Django 2.0 on 2018-01-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.IntegerField()),
                ('sentiment', models.CharField(max_length=140)),
            ],
        ),
    ]
