# Generated by Django 4.2.4 on 2023-08-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_app', '0004_remove_carouselitem_button1_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('vacancy_count', models.IntegerField()),
            ],
        ),
    ]
