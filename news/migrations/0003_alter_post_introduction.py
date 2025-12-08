from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_post_introduction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="introduction",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Introduction",
                help_text="Introduction",
            ),
        ),
    ]
