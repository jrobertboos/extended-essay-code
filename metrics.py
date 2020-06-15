import os
from wand.image import Image
class Metric(object):
  def cr(imageA, imageB):
      a = os.path.getsize(imageA)
      b = os.path.getsize(imageB)
      return a/b

  def mse(imageA, imageB, write_result=False):
      with Image(filename=imageA) as a:
          with Image(filename=imageB) as b:
              result_image, result_metric = a.compare(b, metric="mean_squared")
              if write_result == True:
                  with result_image:
                      result_image.save(filename='diff.JPEG')
      return result_metric

  def psnr(imageA, imageB, write_result=False):
       with Image(filename=imageA) as a:
           with Image(filename=imageB) as b:
               result_image, result_metric = a.compare(b, metric="peak_signal_to_noise_ratio")
               if write_result == True:
                   with result_image:
                       result_image.save(filename='diff.JPEG')
       return result_metric

  def ssim(imageA, imageB, write_result=False):
       with Image(filename=imageA) as a:
           with Image(filename=imageB) as b:
               result_image, result_metric = a.compare(b, metric="structural_similairity")
               if write_result == True:
                   with result_image:
                       result_image.save(filename='diff.JPEG')
       return result_metric
