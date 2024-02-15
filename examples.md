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
This is the internal address to connect to the sensor unit. Please do not change this otherwise the compute unit will not be able to connect to the sensor unit

PERSISTENT: YES

### detector-threshold
Each object detected from the object detector network has a confidence value attached to it. The detector threshold sets the value for how high this confidence value has to be to be accepted as a detection event. By lowering the value it raises the posibility to get false positives in. While setting the value to high might lead to missing certain objects completely

PERSISTENT: YES

### sensor-vertical-flip
Should the incoming image stream from the sensor unit be vertically flipped or not. This can be the case if you hang the sensor unit upside-down because it is a more confinent arrangment space in the situation. Only under these cirumcstances you should change this value. Otherwise the detector performance will greatly suffer in if the objects in the image stream do not have the correct expected orientation.

PERSISTENT: YES

### filter-nonmov
When assembling a data sequence often it can happen that certain false detection persist over the whole sequence. These false detections often tend to be a certain object or constellation in the image that mostly remains static or just has some small jittery movement. An easy way to get rid of these falls negative in the sequence is to basically filter all objects that show no or very little movement. The filter-nonmov parameters switches this sequence filte roption on or off

PERSISTENT: NO

### filter-longvisible
Similar to the previous option it might be that although the false negative object is mostly stationary other objects you are interested in are mostly too but occational they do move. This gives an additional option to filter mostly static objects but not by their movement but how long they seem to persist in the sensor area.

PERSISTENT: NO

### mergeIoU-threshold
It can happen that during the recording of a sequence and its assembly an object temporarly disappears or gets occluded by another object in the scene, if that occlusion is long enough that the object in interest has moved or the length of occlusion is very long that these events are then registered as the occurance of two different objects. In a subsequent processing step it is determined if some of these individual occurence events can be merged to a single occurence. For this merging process a [IoU metric](https://viso.ai/computer-vision/intersection-over-union-iou/) is used to tell the system how close have the objects visibile be in these events before they are considered to be merged into a single occurence event  

PERSISTENT: NO

### feature-mincorrelation
For each object detected a feature vector is generated which acts like a kind of "finger print". This parameter determine what is the minimum correlation value (0.0 meaning not correlated at all while 1.0 extremely correlated) of the "finger print" between two objects to be seen as the same object

PERSISTENT: NO

### feature-mergecorrelation
Similar to the mergeIoU threshold the feature-mergecorrelation parameter sets the threshold on how high the "finger prints" correlation of the object in two different occruence events has to be before they are considered to be merged when the IoU metric is low but above the threshold value

PERSISTENT: NO

### feature-mergecorrelation2
The feature-mergecorelation2 is like the feature-mergecorrelation but is another threshold that can either be lower or higher than the previous one but gets used when the IoU metric of the the objects in the two different occurence events is high

PERSISTENT: NO

### minimum-continous-frames-before-nerge

PERSISTENT: NO

### minimum-continous-frames-after-nerge

PERSISTENT: NO

### filter-nonmove-threshold

PERSISTENT: NO

### filter-maxseconds

PERSISTENT: NO
