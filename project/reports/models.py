from django.db import models
from django.utils import timezone

class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('donation', 'Donation'),
        ('expense', 'Expense'),
        ('inventory', 'Inventory'),
    ]

    report_type = models.CharField(
        max_length=20,
        choices=REPORT_TYPE_CHOICES,
        default='donation',
    )
    generated_at = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='reports/')  # To store the generated report files

    def __str__(self):
        return f"{self.get_report_type_display()} Report - {self.generated_at.strftime('%Y-%m-%d %H:%M:%S')}"
