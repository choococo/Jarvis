import torch
import torchvision
from PIL import Image, ImageDraw
from torchvision import transforms

"""
侦测人体，不是人脸
"""
model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
model.eval()

tf = transforms.Compose([
    transforms.ToTensor(),
])

im = Image.open("../images/01.jpg")

# im = im.resize((300, 400))
imDraw = ImageDraw.Draw(im)
x = tf(im)

predictions = model([x])
print(predictions)
boxes = predictions[0]['boxes']
labels = predictions[0]['labels']
scores = predictions[0]['scores']
for box, label, score in zip(boxes, labels, scores):
    print(box)
    _box = box.cpu().detach().numpy()
    print(_box)
    _label = label.cpu().detach().numpy()
    _score = score.cpu().detach().numpy()
    if _label == 1 and _score > 0.5:
        imDraw.rectangle(_box)
im.show()
