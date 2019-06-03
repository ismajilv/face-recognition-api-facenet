
# Face Recognition API!

This is the implementation of building and evaluating a face detection microservice. 

### Where to get it
The source code is currently hosted on GitHub at: [https://github.com/ismajilv/veriff_test]

### Usage
Clone repository:
```
$ git clone https://github.com/ismajilv/veriff_test
```
Install pipenv for Mac:
```
$ brew install pipenv
``` 
for Windows/Linux:
```
$ pip3 install pipenv
```
Then run
```
$ cd pipenv & pipenv install Pipfile
```
which will create virtual environment and install all dependencies.
You can start the application as a container or by running:
```
$ python app.py
```
To run container, first download archived docker from [https://drive.google.com/open?id=1I_IrAmva0G-gyeQiSSObS4hCv9-HwM9s] to desired location, then load the fdapp-docker.tar with:
```
$ docker load < fdapp-docker.tar
```
or run:
```
$ docker build --tag fdapp .
```
 and then if you run:
```
$ docker images
```
fdapp:latest should be located among docker images (size of 1.87 gb).
To run docker simply run:
```
docker run --name fd-app -p 5000:5000 fdapp:latest 
```
that maps the host’s port 5000 to the containers port of 5000. Then you can access application at: [http://localhost:5000]
## Overview of application
![Main](https://user-images.githubusercontent.com/34252511/56964679-57799c00-6b64-11e9-898f-829b31c4733e.PNG)

Example response with To_Bounded_Box_Image button
![upload](https://user-images.githubusercontent.com/34252511/56965021-f4d4d000-6b64-11e9-950f-a58853974e43.png)
Example response with To_Json button:
```json
{
  "boundingBox": [
    {
      "acc": 0.9999833106994629, 
      "x1": 247.74527037888765, 
      "x2": 311.6788002476096, 
      "y1": 153.96883302927017, 
      "y2": 235.6609631255269
    }, 
    {
      "acc": 0.9988136291503906, 
      "x1": 126.15142646431923, 
      "x2": 211.25640925765038, 
      "y1": 86.57666124403477, 
      "y2": 197.7662461772561
    }, 
    {
      "acc": 0.9966387748718262, 
      "x1": 368.6873416900635, 
      "x2": 438.01915779709816, 
      "y1": 92.99440447241068, 
      "y2": 185.34116929024458
    }, 
    {
      "acc": 0.9964383840560913, 
      "x1": 510.650544911623, 
      "x2": 573.4511119276285, 
      "y1": 153.0793759226799, 
      "y2": 235.7024950683117
    }, 
    {
      "acc": 0.9924536347389221, 
      "x1": 556.4510400295258, 
      "x2": 627.0663306713104, 
      "y1": 97.9593103826046, 
      "y2": 187.21614316664636
    }
  ], 
  "fileName": "make-a-friend-day-fun.jpg", 
  "status": "Succeeded"
}
```
## Overview
The solution seems working, improvement areas would be showing accuracy next to face box, and images are handled without saving in the server bystring to io, io to string and saving in the buffer. I wonder if I saved in the server would I get response faster? Getting image response takes approximately 2 seconds which could be improved if proper image conversion found.

Thanks!
