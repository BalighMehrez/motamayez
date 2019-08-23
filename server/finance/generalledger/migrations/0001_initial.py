# Generated by Django 2.1.4 on 2018-12-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostCenters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=30)),
                ('Eng_Name', models.CharField(max_length=30)),
                ('Arb_Name', models.CharField(max_length=30)),
                ('Remarks', models.CharField(max_length=50)),
                ('Reg_Date', models.DateTimeField(auto_now_add=True)),
                ('Update_Date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CostCentersGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=30)),
                ('Eng_Name', models.CharField(max_length=30)),
                ('Arb_Name', models.CharField(max_length=30)),
                ('Remarks', models.CharField(max_length=50)),
                ('Reg_Date', models.DateTimeField(auto_now_add=True)),
                ('Update_Date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]