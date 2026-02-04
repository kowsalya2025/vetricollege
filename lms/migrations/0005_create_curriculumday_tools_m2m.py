from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('lms', '0004_create_tool'),
    ]
    
    operations = [
        migrations.RunSQL(
            sql="""
                CREATE TABLE IF NOT EXISTS "lms_curriculumday_tools" (
                    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                    "curriculumday_id" bigint NOT NULL REFERENCES "lms_curriculumday" ("id") DEFERRABLE INITIALLY DEFERRED,
                    "tool_id" bigint NOT NULL REFERENCES "lms_tool" ("id") DEFERRABLE INITIALLY DEFERRED
                )
            """,
            reverse_sql="DROP TABLE IF EXISTS lms_curriculumday_tools",
            state_operations=[
                migrations.AddField(
                    model_name='curriculumday',
                    name='tools',
                    field=models.ManyToManyField(blank=True, related_name='curriculum_days', to='lms.tool'),
                ),
            ],
        ),
        # Create indexes for the many-to-many table
        migrations.RunSQL(
            sql="""
                CREATE INDEX IF NOT EXISTS "lms_curriculumday_tools_curriculumday_id" 
                ON "lms_curriculumday_tools" ("curriculumday_id")
            """,
            reverse_sql="DROP INDEX IF EXISTS lms_curriculumday_tools_curriculumday_id",
        ),
        migrations.RunSQL(
            sql="""
                CREATE INDEX IF NOT EXISTS "lms_curriculumday_tools_tool_id" 
                ON "lms_curriculumday_tools" ("tool_id")
            """,
            reverse_sql="DROP INDEX IF EXISTS lms_curriculumday_tools_tool_id",
        ),
        migrations.RunSQL(
            sql="""
                CREATE UNIQUE INDEX IF NOT EXISTS "lms_curriculumday_tools_curriculumday_id_tool_id" 
                ON "lms_curriculumday_tools" ("curriculumday_id", "tool_id")
            """,
            reverse_sql="DROP INDEX IF EXISTS lms_curriculumday_tools_curriculumday_id_tool_id",
        ),
    ]
