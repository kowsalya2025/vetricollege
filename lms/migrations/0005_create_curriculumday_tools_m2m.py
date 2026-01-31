from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_create_tool'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurriculumDay_tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculumday', models.ForeignKey(on_delete=models.CASCADE, to='lms.curriculumday')),
                ('tool', models.ForeignKey(on_delete=models.CASCADE, to='lms.tool')),
            ],
            options={
                'db_table': 'lms_curriculumday_tools',
                'managed': True,
            },
        ),
    ]

