from model import Model
from train import Classifier

model= Model()
model.train_and_save()

cls = Classifier()
print(cls.load_and_test({}))