# Overview of Python example codes
We provide some small python examples in the example sub directory of this repository that demonstrate how you can use the data service RestAPI that is installed on the on-premise compute unit that comes with the drinnenbox. To run these scripts you'll need:
* Python 3.3 or above
* [Python Imaging Library (Pillow)](https://pypi.org/project/pillow/)

Of course these API calls should be easily to port into any other programming language. Alternative under Unix you can use curl or on any Operating System even directly your webbrowser

## helloblindsensor.py
This first example script should get you easily started on how to use the data service API. This example demonstrates how to connect to the data service API and get the current system status (temperatures and if the system is up and running) and current version nummbers of the installed software components on the compute unit.

## getcurrentview.py
This script gets the current view of the sensor unit. This means the current detected object at the time when sending the request since there is a bit of a delay between sending request, receiving request and sending the information all depending back (all depending also on the responsiveness of the betwork) it might of course not exctly reflect the situation right at the moment when you receive the answer back. But it gives you a good indication if the object detection is actually detecting anything at the moment. Additionally this script has the option to get a snapshot and render the position of the detected objects into that snapshot. This is then saved as
```
image.jpg
```
at the location where the getucrrentview.py script is located
In case you get the JSON data back along side a warning message that there is a significant time drift and the data might be old try this call again. If this problem persists than there is likely an issue with the detection program. First check if it is running you can do this with the helloblindsensor.py script or via the web browser. If yes then it might be hanging so try the restartdetection.py script next. If not then simply wait for another 5 seonds and try again. If that still persists power-cycle the compute unit

## getsequencedata.py
This scripts demonstrates how to get sequence data of a certain length in seconds from the dataservice API. The information is returned as one long JSON string. This script includes a sceleton structure to decode that JSON string for each individual object

## restartdetection.py
This scripts demonstrates how to restart the detection service and check again if it is running

## getsetsettings.py
Since the compute unit has a number of system settings that both control the detection part of the compute unit as also the assembly of the sequence data it is possible to change these settings from their default setting. The getsetsettings python script shows how this can be done.
In a first calls it asks the system for all the current parameters and their current value which are returned combined in a single JSON structure.
In a second part it changes the value for detector-threshold to a new value and sends the JSON back to the dataservice API. And in a final step it gets the current parameters and their values back so one can see if the threshold paramter has actually been changed. It is worth knowing that some of the paramter changes will stay persistent so that means after a restart or reboot of the compute unit it will use the changed paramter. Other parameters however will not and every restart will change them back to their initial factory value. Bellow is the list of parameters, a short description of what they actually control and if it stays persistent or not.

### sensor-addres

PERSISTENT:

### detector-threshold

PERSISTENT:

### sensor-vertical-flip

PERSISTENT:

### filter-nonmov

PERSISTENT:

### filter-longvisible

PERSISTENT:

### mergeIoU-threshold

PERSISTENT:

### feature-mincorrelation

PERSISTENT:

### feature-mergecorrelation

PERSISTENT:

### feature-mergecorrelation2

PERSISTENT:

### minimum-continous-frames-before-nerge

PERSISTENT:

### minimum-continous-frames-after-nerge

PERSISTENT:

### filter-nonmove-threshold

PERSISTENT:

### filter-maxseconds

PERSISTENT:
