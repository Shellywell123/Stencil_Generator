# Stencil Generator
python3 program that coverts an image file into 3 stencils, by cranking up the contrast and isolating different tones.

Input Image            |  Stencil Version
:-------------------------:|:-------------------------:
![](https://github.com/Shellywell123/Stencil_Generator/blob/main/test_image.jpg)  |  ![](https://github.com/Shellywell123/Stencil_Generator/blob/main/combined_stencils.png)

## Usage
The program will automatically greyscale the inputted image if it is not already, it will then increase the contrast, the higher the contrast the less different tones tin the image there will be. The arguments hi_lim,lo_lim are for isolating and grouping the remaining tones into 3 stencils. `0 = black` and `256 = white`, therefore you can adjust the paramaters to best isolate the different layers for a given input image. The program will save the 3 stencils A,B,C to the same `dir` as the python script.

```py

make_stencils(image_name="test_image.jpg",contrast_factor=5,hi_lim=200,lo_lim=10)
```

Stencil A (Darks)         |  Stencil B (Mids)   |  Stencil C (Lights)
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/Shellywell123/Stencil_Generator/blob/main/a_stencil_darks.png)  |  ![](https://github.com/Shellywell123/Stencil_Generator/blob/main/b_stencil_mids.png)|  ![](https://github.com/Shellywell123/Stencil_Generator/blob/main/c_stencil_lights.png)

## Setup

```bash
git clone https://github.com/Shellywell123/Stencil_Generator.git
```