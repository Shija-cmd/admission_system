from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.ensemble import RandomForestClassifier
import joblib
# Register models here
# Drop down menu for the concept note of applicants
RE = (
    (1, 'Has concept note'),
    (0, 'Has no concept note'),
)
class Data(models.Model):
    NAME = models.CharField(max_length=100, null=True, unique = True)
    UGPA = models.FloatField(validators = [MaxValueValidator(5),MinValueValidator(0)], null=True)
    RCN = models.PositiveIntegerField(choices=RE, null=True)
    TOEFL = models.FloatField(validators = [MaxValueValidator(120),MinValueValidator(0)],null=True)
    LOR = models.FloatField(validators = [MaxValueValidator(5),MinValueValidator(0)],null=True)
    SOP = models.FloatField(validators = [MaxValueValidator(5),MinValueValidator(0)],null=True)
    HIGH_SCHOOL_POINTS = models.FloatField(validators = [MaxValueValidator(21),MinValueValidator(7)],null=True)
    STATUS = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    # Excution of the machine learning save model
    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/masters_intern.joblib')
        self.STATUS = ml_model.predict([[self.UGPA, self.RCN, self.TOEFL, self.LOR, self.SOP, self.HIGH_SCHOOL_POINTS]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.NAME

