from django import forms
from .models import Reports, Trails

# Groomer form
class ReportForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ['trail', 'report']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trail'].queryset = self.fields['trail'].queryset.order_by('trailName')

# Trail admin form
class TrailForm(forms.ModelForm):
    class Meta:
        model = Trails
        fields = ['trailName', 'location', 'rating']  

# Admin admin form for approvals
class ReportApprovalForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ['approvalStatus']  
