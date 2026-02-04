from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('lms', '0003_alter_video_duration_alter_video_thumbnail_and_more'),
    ]
    
    operations = [
        migrations.RunSQL(
            sql="""
                CREATE TABLE IF NOT EXISTS "lms_tool" (
                    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                    "name" varchar(100) NOT NULL,
                    "description" text NOT NULL,
                    "icon_class" varchar(100) NOT NULL,
                    "icon_image" varchar(100) NULL,
                    "download_url" varchar(200) NOT NULL,
                    "is_required" bool NOT NULL,
                    "order" integer NOT NULL,
                    "category" varchar(20) NOT NULL,
                    "created_at" datetime NOT NULL,
                    "updated_at" datetime NOT NULL
                )
            """,
            reverse_sql="DROP TABLE IF EXISTS lms_tool",
            state_operations=[
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
            ],
        ),
    ]

