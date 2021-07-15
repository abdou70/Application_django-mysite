# Generated by Django 3.2.4 on 2021-07-14 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0002_alter_subject_staffs_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_naissance',
            field=models.DateField(default='2010-05-10'),
        ),
        migrations.AlterField(
            model_name='costumuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'Staffs'), (3, 'Student'), (4, 'Secretaire')], default=1, max_length=10),
        ),
        migrations.CreateModel(
            name='Secretaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=150)),
                ('adresse', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
