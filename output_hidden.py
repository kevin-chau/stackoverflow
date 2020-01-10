# https://stackoverflow.com/questions/59676082/python-function-returning-objects-insted-of-values

import numpy as np

class output_hidden:

    def feature(self,x1,y1):
        feature=np.array([x1,y1])
        return feature
    def weights(self):
        self.weights = np.random.rand(2,1)
        return self.weights

object_1=output_hidden()
value_of_feature = object_1.feature(0.05, 0.10)