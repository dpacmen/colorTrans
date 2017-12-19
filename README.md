# colorTrans
  Color transfer from source image to target image using opencv

## Learn open cv from [openCV documentation](https://docs.opencv.org/3.2.0/d9/df8/tutorial_root.html)


##  TransferColor Module
  
  This module is imported in color.py
   
### trans_color function 
  
  1. Convert the images from the RGB to L\*a\*b\* color space
  
  2. Compute color statistics for the source and target images
  
  3. Subtract the means from the target image. Scale by the standard deviations
  
  4. Add in the source mean
  
  5. Merge the channels together and convert back to the RGB colorspace
  
## In order to run this script
  
  1. Open terminal
  2. Run command in this sequence : 
  <code>$ python color.py -source source.jpg -target target.jpg</code>
  
#### SOURCE IMAGE  
  ![image](images/source.jpg)

#### TARGET IMAGE
  ![image](images/target.jpg)
  
#### RESULTANT TRANSFER IMAGE  
  ![image](images/transfer.png)
  
  
  
