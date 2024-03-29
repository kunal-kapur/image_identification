from torch.nn import Module
from torch.nn import Conv2d
from torch.nn import Dropout
from torch.nn import Linear
from torch.nn import MaxPool2d
from torch.nn import ReLU
from torch.nn import LogSoftmax
from torch import flatten
from torch.nn import AvgPool2d
from torch.nn import ParameterList

class CNN(Module):
    
	def __init__(self, num_classes):
		"""
		customizable class to create a convolutional neural network using PyTorch. Activation function for each layer is ReLU

		Args:
			num_filter_list (list[int]): list of the number of filters for the coressponding layer
			kernal_size_list (list[int]): list of the size of each filter for the coressponding convloutional layer
			stride_list (list[int]): list of the stride length of each filter for the coressponding convolutional layer 
			padding_list (list[int]): list of the amount of padding the coressponding convolutional layer
			pooling_list (list[int]): list of the pooling layers applied to each convolutional layer
			drop_list (list[bool]): list of if we want to drop random nodes on the coressponding convolutional layer
			linear_layer_outputs (list[int]): the output nodes on each linear layer (after flattenning)
			classes (list[int]): number of classes
			intput_size (int): input size of image
		"""
		super().__init__()


		self.conv1 = Conv2d(in_channels=1, out_channels=16, kernel_size=2, stride=2, padding=0)
		self.drop1 = Dropout(p=0.3)
		self.relu1 = ReLU()
		self.pool1 = MaxPool2d(kernel_size=2)

		self.conv2 = Conv2d(in_channels=16, out_channels=32, kernel_size=2, stride=1, padding=0)
		#self.drop2 = Dropout(p=0.5)
		self.relu2 = ReLU()
		self.pool2 = MaxPool2d(kernel_size=2)
		
		self.linear4 = Linear(in_features=800, out_features=400)
		self.relu4 = ReLU()

		self.linear5 = Linear(in_features=400, out_features=num_classes)
		
		self.logsoftmax = LogSoftmax()




	def forward(self, x):
		print(x.size())
		x = self.conv1(x)
		x = self.drop1(x)
		x = self.relu1(x)
		x = self.pool1(x)

		x = self.conv2(x)
		# x = self.drop2(x)
		x = self.relu2(x)
		x = self.pool2(x)


		x = flatten(x, 1)

		x = self.linear4(x)
		x = self.relu4(x)

		x = self.linear5(x)
		
		out = self.logsoftmax(x)
		
		return out


				








		


