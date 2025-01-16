# Generated by Django 5.1.5 on 2025-01-15 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_category_options_blogs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'verbose_name_plural': 'blogs'},
        ),
        migrations.RenameField(
            model_name='blogs',
            old_name='is_feacherd',
            new_name='is_featured',
        ),
        migrations.AlterField(
            model_name='blogs',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=100),
        ),
    ]
