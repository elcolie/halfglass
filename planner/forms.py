from django import forms

from .models import Planner
from planner.scheduler_type import *


class PlannerModelForm(forms.ModelForm):
    class Meta:
        model = Planner
        exclude = ()


class PlannerForm(forms.Form):
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Note here'}))

    scheduler_type = forms.ChoiceField(required=False, help_text="This field is required", choices=SCHEDULER_TYPE)
    start_type = forms.ChoiceField(required=False, help_text="This field is required", choices=START_TYPE)

    start_time = forms.TimeField(required=False, widget=forms.TimeInput(format='%H:%M',
                                                                        attrs={'placeholder': "HH:MM in 24hr unit"}))
    stop_time = forms.TimeField(required=False, widget=forms.TimeInput(format='%H:%M',
                                                                       attrs={'placeholder': "HH:MM in 24hr unit"}))
    month_list = forms.MultipleChoiceField(required=False,
                                           widget=forms.CheckboxSelectMultiple,
                                           choices=MONTH_LIST)
    week_day = forms.MultipleChoiceField(required=False,
                                         widget=forms.CheckboxSelectMultiple,
                                         choices=WEEK_DAY)
    date_day = forms.MultipleChoiceField(required=False,
                                        widget=forms.CheckboxSelectMultiple,
                                        choices=DATA_DAY)
    stop_type = forms.ChoiceField(required=False, choices=STOP_TYPE)

    lifetime_quantity = forms.IntegerField(required=False, max_value=32767, min_value=0)
    lifetime_unit = forms.ChoiceField(required=False, choices=LIFETIME_UNIT)

    class Meta:
        model = Planner
