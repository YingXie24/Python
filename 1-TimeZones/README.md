# Timezones.py

The problem domain for this project involves time zones, and in particular Coordinated Universal Time (UTC), which is the primary time standard by which the world regulates clocks and time.

There are 40 time zones in the world. One of them, UTC+00:00, is considered to be in the middle of the other time zones. For example, the Phillipines are in the time zone UTC+08:00 because clocks there are set 8 hours later than in time zone UTC+0:00.

In **TimeZones.py**, several functions were implemented:
* seconds_difference(time_1, time_2): returns how many seconds later the second time is than the first
*  hours_difference(time_1, time_2): returns how many *hours* later the second time is than the first
* to_float_hours(hours, minutes, seconds): returns the combined time in hours (float)
* get_hours, get_minutes and get_seconds(time): return the hours part, minutes part or seconds part of a time in seconds
* time_to_utc(utc_offset, time): returns time at UTC+0, where utc_offset is the number of hours away from UTC_0
* time_from_utc(utc_offset, time): returns UTC time in time zone utc_offset

A graphical user interface(GUI) is also provided in **TimeZones_gui.py**, that shows four clocks and allows the user to choose time zones to display. This python file is provided by the Coursera Learn to Program: the Fundamentals course.  

<img src="https://github.com/YingXie24/images/blob/master/Python-1-TimeZone/GUI.PNG" width=70% >
