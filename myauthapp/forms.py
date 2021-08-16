from django import forms
from .models import PredictIncome

class PredictCreateForm(forms.ModelForm):
  class Meta:
    model = PredictIncome
    fields = ("age", "work_class", "education", "marital_status", "occupation", "relationship", "race", "sex", "capital_gain", "capital_loss", "hours_per_week", "native_country")