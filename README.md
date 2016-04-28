# halfglass
Prototype of scheduler

Has 2 urls
1. url /planner/cdt     (Certain data-time)
2. url /planner/period
========================================================
1. Certain Date-time : Create page.
* predefined 2 parameters.
* scheduler_type : Recurrence
* start_type : Certain Start/Stop Time
Comment : TextInput
Month
    [ ] Jan [ ] May
    [ ] Feb [ ] June
    [ ] Mar
    [ ] Apr   ... [ ] Dec
Radio buttons() and Multiple Check Boxes[]
( ) week day
    [ ] Sun [ ] Mon [ ] Tue [ ] Wed [ ] Thu [ ] Fri [ ] Sat
( ) date
    [ ] 1 [ ] ...
    [ ] 11 ...
    [ ] 30 [ ] 31
start time : HH:MM  //With 24hr in place-holder

stop time :
( ) time
    HH:MM   //With 24hr in place-holder
( ) period
    + PositiveSmallIntegerField()
    + Drop Down List (Min, Hour, Day)
[submit btn]


