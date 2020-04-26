# ComputerVision

### Summary
In this repository I have all of my files from the beginning of studying computer vision. Most of these files are super small.
For example:
- 'just_camera.py` gets video from your web-cam and shows it on the screen. If you press `q` is stops working
- `QR_from_camera` also gets the video from your web-cam but if you show some QR-code to the camera it will open the link which
is stored on this code. I find it pretty useful
- `QR_generator`does this:
    - In the Excel table there are name, second name and age of some people.
    - For each person program generates individual QR-code and places it in specific folder (you can put a path to it on the 27 line)
- `Face_detection` finds a human face on the video and returns the frame where this face was found

The most complecated program is `Face_and_QR_to_Excel` and that's what it does:
- A user hold a phone or a paper with QR-code on it
- User's face is detected
- QR-code is detected
- User's face photo is placed in a separate folder (line 100)
- QR-code must contain some text. If this text has already been detected some time ago and it's in computer's memory - it will be ignored,but if it's a new text, then it will be saved to the Excel table.
  
  The idea was that this program can be used on some factory for example. So the worker in the beginning of the day comes to the special room with the camera in it, shows his individual QR-code, his face is beeing saved to the first folder, and his personal data - to the other folder. This way it would be easier to control all working hours, number of people working etc.
