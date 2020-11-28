# Stencil Generator
python3 program that coverts an image file into 3 stencils, by cranking up the contrast and isolating different tones.


<p float="middle">
  <img src="test_image.jpg" width="265" title="test title" alt="accessibility text"/>
  <img src="arrow.png" width="265" />
  <img src="combined_stencils.png" width="265" />  
</p>

Input Image            |  Stencil Version
:-------------------------:|:-------------------------:
![](https://github.com/Shellywell123/Stencil_Generator/blob/main/test_image.jpg)  |  ![](https://github.com/Shellywell123/Stencil_Generator/blob/main/combined_stencils.png)

## usage

```py

make_stencils(image_name="test_image.jpg",contrast_factor=5,hi_lim=200,lo_lim=10)
```

<p float="middle">
  <img src="a_stencil_darks.png" width="265" />
  <img src="b_stencil_mids.png" width="265" />
  <img src="c_stencil_lights.png" width="265" />
</p>