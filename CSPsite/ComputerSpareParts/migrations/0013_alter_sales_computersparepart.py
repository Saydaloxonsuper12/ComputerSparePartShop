# Generated by Django 4.1 on 2022-09-18 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ComputerSpareParts', '0012_sales_computersparepart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='computersparepart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComputerSpareParts.computersparepart'),
        ),
    ]