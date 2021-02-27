
def make_stencils(image_name,contrast_factor,hi_lim,lo_lim):
    """
    """

    print('making stencils from {}'.format(image_name))
    #increase contrast
    from PIL import Image,ImageEnhance,ImageOps
    img=Image.open(image_name)
    img_contr_obj=ImageEnhance.Contrast(img)
    e_img=img_contr_obj.enhance(contrast_factor)
    e_img = ImageOps.grayscale(e_img)
    e_img.save('combined_stencils.png')

    print('contrast config = {}'.format(contrast_factor))

    # check num of cols
    from collections import Counter
    colors = Counter(e_img.getdata())
    print(len(colors),'different shades')                  # number of unique colors 

    # make 3 stencils

    black = (0,0,0)
    grey  = (100,100,100)
    light_grey = (200,200,200)
    white =(256,256,256)
    red = (256,0,0)

    print('stencil config hi_lim = {}, load = {}, 3 stencil'.format(hi_lim,lo_lim))
    #stencil A dark cols
    a_img = e_img.copy()
    a_img = a_img.convert('RGB')
    a_pixelsNew = a_img.load()
    import numpy as np
    for i in range(a_img.size[0]):
        for j in range(a_img.size[1]):
      #      print(a_pixelsNew[i,j])

            if np.mean(a_pixelsNew[i,j]) <= lo_lim:
                a_pixelsNew[i,j] = black
            else:
                a_pixelsNew[i,j] = red
                
    a_img.save('a_stencil_darks.png')

    #stencil b mid cols
    b_img = e_img.copy()
    b_img = b_img.convert('RGB')
    b_pixelsNew = b_img.load()
    import numpy as np
    for i in range(b_img.size[0]):
        for j in range(b_img.size[1]):
            #print(pixelsNew[i,j])
            if lo_lim <= np.mean(b_pixelsNew[i,j]) < hi_lim:
                b_pixelsNew[i,j] = grey
            else:
                b_pixelsNew[i,j] = red

    b_img.save('b_stencil_mids.png')

    #stencil c light cols
    c_img = e_img.copy()
    c_img = c_img.convert('RGB')
    c_pixelsNew = c_img.load()
    import numpy as np
    for i in range(c_img.size[0]):
        for j in range(c_img.size[1]):
            #print(pixelsNew[i,j])
            if np.mean(c_pixelsNew[i,j]) >= hi_lim:
                c_pixelsNew[i,j] = white
            else:
                c_pixelsNew[i,j] = red

    c_img.save('c_stencil_lights.png')

make_stencils(image_name="test_image.jpg",contrast_factor=5,hi_lim=200,lo_lim=10)