# Generated by Django 5.0.1 on 2024-02-03 10:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Expense",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField(verbose_name="開始日")),
                ("end_date", models.DateField(verbose_name="終了日")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("学費", "学費"),
                            ("修学費", "修学費"),
                            ("家賃", "家賃"),
                            ("食費", "食費"),
                            ("光熱水料通信費", "光熱水料通信費"),
                            ("その他", "その他"),
                        ],
                        max_length=30,
                        verbose_name="カテゴリー",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=0,
                        help_text="1万円未満は切り捨てて入力してください。",
                        max_digits=2,
                        verbose_name="金額（単位：万円）",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
