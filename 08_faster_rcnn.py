# pip install torch torchvision
import torch, torchvision, cv2
from torchvision.transforms.functional import to_tensor

model = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights='DEFAULT').eval()
img = cv2.imread('image.jpg')

with torch.no_grad():
    out = model([to_tensor(img[..., ::-1].copy())])[0]  # BGR -> RGB

for box, score in zip(out['boxes'], out['scores']):
    if score > 0.6:
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('Faster R-CNN', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
