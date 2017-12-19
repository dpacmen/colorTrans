# colorTrans
  Color transfer from source image to target image using opencv

## Learn open cv from here : https://docs.opencv.org/3.2.0/d9/df8/tutorial_root.html


##  TransferColor Module
  
  This module is imported in color.py
   
### trans_color function 
  
  1. Convert the images from the RGB to L * ab * color space
  
  2. Compute color statistics for the source and target images
  
  3. Subtract the means from the target image. Scale by the standard deviations
  
  4. Add in the source mean
  
  5. Merge the channels together and convert back to the RGB colorspace
  
## In order to run this script
  
  1. Open terminal
  2. Run command in this sequence --> python color.py -s  source.jpg -t target.jpg 
    (check argparse code)
