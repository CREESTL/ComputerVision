**Summary**

In this repository I have all of my files from the beginning of studying computer vision. Most of these files are super small.
For example _"just_camera.py"__ gets video from your web-cam and shows it on the screen. If you press "q" is stops working
__"QR_from_camera"__ also gets the video from your web-cam but if you show some QR-code to the camera it will open the link which
is stored on this code. I find it pretty useful
__"QR_generator"__ does this:
  1) In the Excel table there are name, second name and age of some people.
  2) For each person program generates individual QR-code and places it in specific folder (you can put a path to it on the 27 line)
__"Face_detection"__ finds a human face on the video and returns the frame where this face was found

The most complecated program is __"Face_and_QR_to_Excel"__ and that`s what it does:
  1) A user hold a phone or a paper with QR-code on it
  2) User`s face is detected
  3) QR-code is detected
  4) User`s face photo is placed in a separate folder (line 100)
  5) QR-code must contain some text. If this text has already been detected some time ago and it`s in computer`s memory - it will be ignored,
  but if it`s a new text, then it will be saved to the Excel table.
  
  The idea was that thiss program can be used on some factory for example. So the worker in the beginning of the day comes to the special room
  with the camera in it, shows his individual QR-code, his face is beeing saved to the first folder, and his personal data - to the other folder.
  This way it would be easier to control all working hours, number of people working etc.
