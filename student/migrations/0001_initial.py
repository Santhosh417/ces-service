# Generated by Django 3.0.7 on 2021-03-15 01:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('professor', models.CharField(max_length=50)),
                ('program', models.CharField(max_length=50)),
                ('course_type', models.CharField(max_length=30)),
                ('credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('cell_phone', models.CharField(max_length=50)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('graduation_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_name', models.CharField(max_length=30)),
                ('start_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('end_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('status', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_course', to='student.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_student', to='student.Student')),
            ],
        ),
    ]
