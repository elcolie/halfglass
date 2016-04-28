from django import forms

from .models import Planner


class PlannerModelForm(forms.ModelForm):
    class Meta:
        model = Planner
        exclude = ()

class PlannerForm(forms.Form):
    BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
    FAVORITE_COLORS_CHOICES = (
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    )
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(required=False,
                                                widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    """http://stackoverflow.com/questions/1057252/how-do-i-access-the-request-object-or-any-other-variable-in-a-forms-clean-met/6062628#6062628"""
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PlannerForm, self).__init__(*args, **kwargs)

    def clean(self):
        return self.request