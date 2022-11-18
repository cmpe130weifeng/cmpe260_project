from torch.autograd import Variable
import torchvision.transforms as transforms
from PIL import Image

def reshape_image(path):

    img = Image.open(path)

    transform=transforms.Compose([
        transforms.Resize([100,100]),
        transforms.ToTensor()])

    #Apply transforms
    if transform is not None:
        img=transform(img)

    # normalization
    mean, std = img.mean(), img.std()
    normalize = transforms.Normalize(mean, std)
    norm_tensor = normalize(img)
    norm_tensor.unsqueeze_(0)
    input_img = Variable(norm_tensor)

    label_str = None
    if ("rock" in path.split("/")[-1]):
        label_str = "R"
    elif ("paper" in path.split("/")[-1]):
        label_str = "P"
    elif ("scissors" in path.split("/")[-1]):
        label_str = "S"
    else:
        pass
    
    return label_str, input_img
