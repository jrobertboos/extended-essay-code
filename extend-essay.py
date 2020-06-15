from numpy.random import randint
from encoder import Encoder
import shutil
with open("/home/jrobertboos/Media/Data/Datasets/imagenet/ILSVRC/ImageSets/CLS-LOC/val.txt", "r") as file:
    for last_line in file:
        pass
validation_num = last_line.split(' ')[1]
dataset_nums = randint(1, validation_num, size=60)

dataset_strings = []
for num in dataset_nums:
    dataset_strings.append(f"ILSVRC2012_val_{num:08d}.JPEG")


for path in dataset_strings:
    shutil.copy2(f"/home/jrobertboos/Media/Data/Datasets/imagenet/ILSVRC/Data/CLS-LOC/val/{path}", "/home/jrobertboos/Code/extended-essay/data/original")



qualities = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for images in dataset_strings:
    for quality in qualities:
        Encoder.jpeg(images, quality)
        Encoder.bpg(images, quality)
        Encoder.heif(images, quality)
        Encoder.webp(images, quality)
        Encoder.jpegxr(images, quality)


