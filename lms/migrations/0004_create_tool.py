from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_alter_video_duration_alter_video_thumbnail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('icon_class', models.CharField(blank=True, max_length=100)),
                ('icon_image', models.ImageField(blank=True, null=True, upload_to='tool_icons/')),
                ('download_url', models.URLField(blank=True)),
                ('is_required', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[
                    ('design', 'Design Tools'),
                    ('development', 'Development Tools'),
                    ('video', 'Video Editing'),
                    ('data', 'Data Science'),
                    ('other', 'Other'),
                ], default='other', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['order', 'name'],
                'verbose_name': 'Tool',
                'verbose_name_plural': 'Tools',
            },
        ),
    ]

