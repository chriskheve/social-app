# Generated by Django 5.0.6 on 2024-08-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_comments_count_comment_post_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=255)),
                ('occurences', models.IntegerField()),
            ],
        ),
    ]
