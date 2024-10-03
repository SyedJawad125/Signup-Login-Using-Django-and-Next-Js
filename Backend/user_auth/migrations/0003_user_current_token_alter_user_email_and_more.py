# Generated by Django 5.0.3 on 2024-10-03 12:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='current_token',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid_input', message='This field accepts only alphabetic characters.', regex='^[a-zA-Z]+$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid_input', message='This field accepts only alphabetic characters.', regex='^[a-zA-Z]+$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be between 9 to 15 digits.', regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
