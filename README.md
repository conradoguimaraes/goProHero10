# GO PRO HERO 10

## Table of Contents
- [Sequence Diagram](#sequence-diagram)
    - [Elements](#elements)
    - [Diagram](#diagram)
- [Webcam Constraints](#webcam-constraints)
- [Preview Stream](#preview-stream)
- [Useful Links](useful-links)


## **Sequence Diagram**

### Elements:
- **main** (`main.py`): main script
- **goProHero10 API** (`goProHero10.py`): _goProHero10 class_ that handles the HTTP communication with the GoPro Hero 10 Camera (Hardware)
- **camera** (`camera.py`): _class_ that implements and handles, through _openCV_, the live feed, keypress events, image processing, etc;
- **GoPro Hero 10**: hardware

### Diagram

```mermaid
sequenceDiagram
    main->>main: Set desired Resolution/FOV
    main->>camera: initialize class object
    main->>goProHero10 API: initialize class object
    loop while failure exists
      main->>goProHero10 API: Change {resolution,fov}
      goProHero10 API->>GoPro Hero 10: HTTP Request: startWebcam{resolution,fov}
      GoPro Hero 10->>GoPro Hero 10: Try to Adjust Lens
      GoPro Hero 10->>goProHero10 API: HTTP Response
      goProHero10 API->>main: Return Code
      alt failure was detected
          main->>goProHero10 API: HTTP Request: exitWebcam
          goProHero10 API->>GoPro Hero 10: turn off Webcam
          GoPro Hero 10->>goProHero10 API: HTTP Response
          goProHero10 API->>main: Return Code
      end
   end

   main->>camera: start live feed
   camera->>GoPro Hero 10: start USB communication
   GoPro Hero 10->>camera: camera is available and ready

   loop while live feed is available
     camera->>GoPro Hero 10: capture image
     GoPro Hero 10->>camera: return captured image
     camera->>main: image preview
   end
    
```

## Webcam Constraints

From [GoPro Support](https://community.gopro.com/s/article/GoPro-Webcam?language=en_US):
```
Webcam Mode resolution limitations: "Here you can choose between [1080p] (default) or [720p]."

    Webcam Resolution
    ID 	Resolution 	Supported Cameras
    4 	480p 	Hero 10 Black, Hero 9 Black
    7 	720p 	Hero 12 Black, Hero 9 Black, Hero 10 Black, Hero 11 Black
    12 	1080p 	Hero 12 Black, Hero 9 Black, Hero 10 Black, Hero 11 Black

    Webcam Field-of-View
    ID 	FOV 	Supported Cameras
    0 	Wide 	Hero 12 Black, Hero 9 Black, Hero 10 Black, Hero 11 Black
    2 	Narrow 	Hero 12 Black, Hero 9 Black, Hero 10 Black, Hero 11 Black
    3 	Superview 	Hero 12 Black, Hero 9 Black, Hero 10 Black, Hero 11 Black
    4 	Linear 	Hero 12 Black, Hero 9 Black, Hero 10 Black, Hero 11 Black
```
## Preview Stream

OBS: **Preview Stream** is not supported on GoPro Hero 10

```
When the preview stream is started, the camera starts up a UDP client and begins writing MPEG Transport Stream data to the client on port 8554. In order to stream this data, the client must implement a UDP connection that binds to the same port and decode the data.

**Start Preview Stream**

Supported Protocols:
USB
WIFI

query Parameters
port, integer
Example: port=8556

Port to use for Preview Stream. Defaults to 8554 if not set

Not supported on:
    Hero 11 Black Mini
    Hero 11 Black
    **Hero 10 Black**
    Hero 9 Black


```

## Useful Links

- Open GoPro HTTP API: [OpenGoPro/HTTP](https://gopro.github.io/OpenGoPro/http)
- GoPro Support webpage: [GoPro-Webcam](https://community.gopro.com/s/article/GoPro-Webcam?language=en_US)

