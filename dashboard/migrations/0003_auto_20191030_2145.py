# Generated by Django 2.2.4 on 2019-10-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20191030_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='program_language',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='编程语言'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill_explain',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='技能说明'),
        ),
    ]
