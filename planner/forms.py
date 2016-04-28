from django import forms

from .models import Planner
from planner.scheduler_type import *


class PlannerModelForm(forms.ModelForm):
    class Meta:
        model = Planner
        exclude = ()


class PlannerForm(forms.Form):
    # BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
    # FAVORITE_COLORS_CHOICES = (
    #     ('blue', 'Blue'),
    #     ('green', 'Green'),
    #     ('black', 'Black'),
    # )
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    # favorite_colors = forms.MultipleChoiceField(required=False,
    #                                             widget=forms.CheckboxSelectMultiple,
    #                                             choices=FAVORITE_COLORS_CHOICES)
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

    """http://stackoverflow.com/questions/1057252/how-do-i-access-the-request-object-or-any-other-variable-in-a-forms-clean-met/6062628#6062628"""
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PlannerForm, self).__init__(*args, **kwargs)

    def clean(self):
        return self.request

    class Meta:
        model = Planner
