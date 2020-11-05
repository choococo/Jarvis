from torchsummary import summary
from e2e_resnet34_2b_gfm_tt import e2e_resnet34_2b_gfm_tt
import torch

if __name__ == '__main__':
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    module = e2e_resnet34_2b_gfm_tt(None).to(device)
    summary(module, input_size=(3, 128, 128))


"""
================================================================
Total params: 146,336,452
Trainable params: 146,336,452
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.19
Forward/backward pass size (MB): 1131.31
Params size (MB): 558.23
Estimated Total Size (MB): 1689.73
----------------------------------------------------------------
"""