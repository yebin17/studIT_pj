# Generated by Django 2.2.7 on 2019-11-23 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20191123_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_user', models.TextField(max_length=20)),
                ('comment_thumbnail_url', models.TextField(max_length=300)),
                ('comment_textfield', models.TextField()),
                ('blog', models.ForeignKey(null=True, on_delete=True, to='blogapp.Blog')),
            ],
        ),
    ]