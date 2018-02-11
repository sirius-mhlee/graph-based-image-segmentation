Graph-Based Image Segmentation
==============================

Python implementation of the algorithm described in the paper Efficient Graph-Based Image Segmentation.
http://cs.brown.edu/~pff/segment/

    Efficient Graph-Based Image Segmentation
    P. Felzenszwalb, D. Huttenlocher
    International Journal of Computer Vision, Vol. 59, No. 2, September 2004

Usage
-----

    python ImageSegmentation.py sigma k min_size input_image_file output_image_file
    
    ex)
    python ImageSegmentation.py 0.5 500 50 ./example/lena.jpg ./example/lena_result.jpg

Result
------

![lena.jpg](./example/lena.jpg) ![lena_result.jpg](./example/lena_result.jpg)
