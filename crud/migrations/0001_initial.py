# Generated by Django 3.2.9 on 2022-03-21 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('emailid', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetail',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='crud.employee')),
                ('education', models.CharField(choices=[('a', 'BTech'), ('b', 'Mtech'), ('c', 'BCA'), ('d', 'MCA')], max_length=1)),
                ('department', models.CharField(max_length=15)),
                ('salary', models.CharField(max_length=30)),
                ('manager', models.CharField(max_length=30)),
            ],
        ),
    ]