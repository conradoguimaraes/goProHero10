# GO PRO HERO 10


## **Sequence Diagram**

Elements:
- **main**: main script
- **goProHero10 API**: [goProHero10] class that handles the HTTP communication with the GoPro Hero 10 Camera (Hardware)
- **camera**: [class] that implements and handles, through _openCV_, the live feed, keypress events, image processing, etc;
- **GoPro Hero 10**: hardware

```mermaid
sequenceDiagram
    main->>main: Set desired Resolution/FOV
    main->>camera: initialize class object
    main->>goProHero10 API: initialize class object
    loop (while failure exists)
      main->>goProHero10 API: HTTP Request: startWebcam{resolution,fov}
      goProHero10 API->>GoPro Hero 10: Change {resolution,fov}
      GoPro Hero 10->>GoPro Hero 10: Try to Adjust Lens
      GoPro Hero 10->>goProHero10 API: HTTP Response
      goProHero10 API->>main: Return Code

      main->>goProHero10 API: HTTP Request: exitWebcam
      goProHero10 API->>GoPro Hero 10: turn off Webcam
      GoPro Hero 10->>goProHero10 API: HTTP Response
      goProHero10 API->>main: Return Code
   end

   main->>camera: start live feed
   camera->>GoPro Hero 10: start USB communication
   
   loop (live feed is available)
     camera->>GoPro Hero 10: capture image
     camera->>main: image preview
   end
    
```


loop Every minute
        John-->Alice: Great!
    end
