# coding=UTF-8
#%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

normal_samples = np.random.normal(size = 100000) # �ͦ� 100000 �ռзǱ`�A���t�]�����Ȭ� 0�A�зǮt�� 1 ���`�A���t�^�H���ܼ�
uniform_samples = np.random.uniform(size = 100000) # �ͦ� 100000 �դ��� 0 �P 1 �������ä��t�H���ܼ�

plt.hist(normal_samples)
plt.show()
plt.hist(uniform_samples)
plt.show()
