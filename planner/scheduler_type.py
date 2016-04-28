from django.utils.translation import ugettext as _

# http://stackoverflow.com/questions/24403075/django-choicefield
SCHEDULER_TYPE = (
    (0, _("One-Time Date/Time")),
    (1, _("Recurrence Date/Time")),
    (2, _("Specific Date/Time"))
)
START_TYPE = (
    (0, _("Certain Start/Stop Time")),
    (1, _("Period Lifetime"))
)
