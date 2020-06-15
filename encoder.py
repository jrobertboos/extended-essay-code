import os
from PIL import Image
class Encoder(object):
  
  def jpeg(image, compression):
    compressiona = compression * 1
    im = Image.open(f"/home/jrobertboos/Code/extended-essay/data/original/{image}")
    im.save(f"/home/jrobertboos/Code/extended-essay/data/{compression}/JPEG/{image}.JPEG", quality=compressiona)
    pass
                
  def bpg(image, compression):
    compressiona = 51 - (compression * 0.51)
    os.system(f"bpgenc -q {compressiona} /home/jrobertboos/Code/extended-essay/data/original/{image} -o /home/jrobertboos/Code/extended-essay/data/{compression}/BPG/{image}.bpg")
    
  def jpegxr(image, compression):
    compressiona = compression * 0.01
    os.system(f"magick convert -compress none /home/jrobertboos/Code/extended-essay/data/original/{image} out.tiff")
    os.system(f"JxrEncApp -i out.tiff -o /home/jrobertboos/Code/extended-essay/data/{compression}/JPEGXR/{image}.jxr -q {compressiona}")
    
  def heif(image, compression):
    compressiona = compression * 1
    os.system(f"heif-enc -q {compression} /home/jrobertboos/Code/extended-essay/data/original/{image} -o /home/jrobertboos/Code/extended-essay/data/{compression}/HEIF/{image}.heif")
    
  def webp(image, compression):
    compressiona = compression * 1
    os.system(f"cwebp -q {compression} /home/jrobertboos/Code/extended-essay/data/original/{image} -o /home/jrobertboos/Code/extended-essay/data/{compression}/WebP/{image}.webp")
 
