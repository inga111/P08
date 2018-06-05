Python 2.7.6 (default, Nov 23 2017, 15:49:48) 
[GCC 4.8.4] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> g=9.81
>>> V0=20
>>> T=14
>>> t=14
>>> y=v*t-((g*(t**2))/2)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    y=v*t-((g*(t**2))/2)
NameError: name 'v' is not defined
>>> y=V0*t-((g*(t**t))/2)
>>> y
-2.147869532318115e+18
>>> 
