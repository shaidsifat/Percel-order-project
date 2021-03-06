# Generated by Django 3.2 on 2021-04-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_createorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='createcheckorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_divison', models.CharField(choices=[('1', 'dhaka divison'), ('2', 'outside dhaka vision'), ('3', 'outside dhaka')], max_length=300)),
                ('product_weight', models.CharField(choices=[('1', '500 t0 2kg'), ('2', '3 kg'), ('3', '4 kg'), ('4', '5 kg')], max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='createnewpercel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='createorder',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='createorder',
            name='product_type',
            field=models.CharField(choices=[('1', 'Fragile'), ('2', 'Liquid]')], max_length=300),
        ),
    ]
