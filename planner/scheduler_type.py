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
MONTH_LIST = (
    (1, _("Jan")),
    (2, _("Feb")),
    (3, _("Mar")),
    (4, _("Apr")),
    (5, _("May")),
    (6, _("Jun")),
    (7, _("Jul")),
    (8, _("Aug")),
    (9, _("Sep")),
    (10, _("Oct")),
    (11, _("Nov")),
    (12, _("Dec"))
)
WEEK_DAY = (
    (0, _("Sun")),
    (1, _("Mon")),
    (2, _("Tue")),
    (3, _("Wed")),
    (4, _("Thu")),
    (5, _("Fri")),
    (6, _("Sat")),
)
DATA_DAY = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
    (12, 12),
    (13, 13),
    (14, 14),
    (15, 15),
    (16, 16),
    (17, 17),
    (18, 18),
    (19, 19),
    (20, 20),
    (21, 21),
    (22, 22),
    (23, 23),
    (24, 24),
    (25, 25),
    (26, 26),
    (27, 27),
    (28, 28),
    (29, 29),
    (30, 30),
    (31, 31),
)
STOP_TYPE = (
    (0, _("date/time")),
    (1, _("period"))
)
