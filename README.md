# Stencil Generator
python3 program that coverts an image file into 3 stencils, by cranking up the contrast and isolating different tones.

Input Image            |  Stencil Version
:-------------------------:|:-------------------------:
![](https://github.com/Shellywell123/Stencil_Generator/blob/main/test_image.jpg)  |  ![](https://github.com/Shellywell123/Stencil_Generator/blob/main/combined_stencils.png)

## Usage

```py

make_stencils(image_name="test_image.jpg",contrast_factor=5,hi_lim=200,lo_lim=10)
```

Stencil A (Darks)         |  Stencil B (Mids)   |  Stencil C (Lights)
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/Shellywell123/Stencil_Generator/blob/main/a_stencil_darks.png)  |  ![](https://github.com/Shellywell123/Stencil_Generator/blob/main/b_stencil_mids.png)|  ![](https://github.com/Shellywell123/Stencil_Generator/blob/main/c_stencil_lights.png)

## install

```bash
git clone https://github.com/Shellywell123/Stencil_Generator.git
```