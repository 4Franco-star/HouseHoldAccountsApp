from django.db import models
from accounts.models import CustomUser

class Income(models.Model):
    CATEGORY = (
        ('家庭からの給付', '家庭からの給付'),
        ('日本学生支援機構の奨学金', '日本学生支援機構の奨学金'),
        ('日本学生支援機構以外の奨学金', '日本学生支援機構以外の奨学金'),
        ('アルバイト等収入', 'アルバイト等収入'),
        ('その他', 'その他'),
    )

    start_date = models.DateField(verbose_name="開始日")
    end_date = models.DateField(verbose_name="終了日")
    category = models.CharField(max_length=30, choices=CATEGORY, verbose_name="カテゴリー")
    amount = models.DecimalField(max_digits=2, decimal_places=0, verbose_name="金額（単位：万円）",
                                 help_text="1万円未満は切り捨てて入力してください。")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Expense(models.Model):
    CATEGORY = (
        ('学費', '学費'),
        ('修学費', '修学費'),
        ('家賃', '家賃'),
        ('食費', '食費'),
        ('光熱水料通信費', '光熱水料通信費'),
        ('その他', 'その他'),
    )

    start_date = models.DateField(verbose_name="開始日")
    end_date = models.DateField(verbose_name="終了日")
    category = models.CharField(max_length=30, choices=CATEGORY, verbose_name="カテゴリー")
    amount = models.DecimalField(max_digits=2, decimal_places=0, verbose_name="金額（単位：万円）",
                                 help_text="1万円未満は切り捨てて入力してください。")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)