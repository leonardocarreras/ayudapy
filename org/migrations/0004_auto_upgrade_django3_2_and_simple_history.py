# Generated by Django 3.2.23 on 2023-11-29 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0003_historicalpool_pool'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaldonationcenter',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Centro de Donación', 'verbose_name_plural': 'historical Centros de Donación'},
        ),
        migrations.AlterModelOptions(
            name='historicalpool',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical pool', 'verbose_name_plural': 'historical pools'},
        ),
        migrations.AlterField(
            model_name='historicaldonationcenter',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalpool',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
