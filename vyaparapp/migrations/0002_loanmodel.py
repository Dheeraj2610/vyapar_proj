# Generated by Django 4.2.5 on 2023-11-28 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vyaparapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=255)),
                ('account_num', models.PositiveBigIntegerField(null=True)),
                ('lender_bank', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True)),
                ('balance', models.BigIntegerField(null=True)),
                ('as_of_date', models.DateField(null=True)),
                ('loan_received', models.CharField(max_length=255, null=True)),
                ('intrest', models.BigIntegerField(null=True)),
                ('duration', models.IntegerField(null=True)),
                ('processing_fee', models.IntegerField(null=True)),
                ('processing_from', models.CharField(max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
