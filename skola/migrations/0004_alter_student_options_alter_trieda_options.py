# Generated by Django 4.2.7 on 2023-12-15 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0003_trieda_alter_student_trieda_alter_ucitel_trieda'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Študent', 'verbose_name_plural': 'Študenti'},
        ),
        migrations.AlterModelOptions(
            name='trieda',
            options={'verbose_name': 'Trieda', 'verbose_name_plural': 'Triedy'},
        ),
    ]
