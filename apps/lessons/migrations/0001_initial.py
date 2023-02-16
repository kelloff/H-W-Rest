# Generated by Django 4.1.6 on 2023-02-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='comics')),
                ('image', models.ImageField(upload_to='images/', verbose_name='image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
            ],
            options={
                'verbose_name': 'comics',
                'verbose_name_plural': 'comicses',
                'ordering': ('-id',),
            },
        ),
    ]