from __future__ import print_function
import numpy as np
from data_preprocessing import data_mu, process_mu

def calculate(high=[90, 0.1, 100, 0.2, 110, 0.4, 120, 0.2, 130, 0.1],low=[40, 0.1, 50, 0.2, 60, 0.4, 70, 0.2, 80, 0.1], component = []):
    # *component: [name, length, name, length, ...]
    att_low = 0
    att_high = 0
    intensity_high = high[1::2]
    intensity_low = low[1::2]

    print(zip (component[::2], component[1::2]))
    for name,length in zip(component[::2], component[1::2]):
        mu_high = process_mu(data_mu[name][0], high)
        mu_low = process_mu(data_mu[name][0], low)

        rho = data_mu[name][1]
        for ind, mu in enumerate(mu_low):
            intensity_low[ind] *=  np.power(np.e, - rho * mu * length)
        for ind, mu in enumerate(mu_high):
            intensity_high[ind] *=  np.power(np.e, - rho * mu * length)

    #### detector efficiency decrease dramatically after 100 keV
    # intensity_high[-1] *= 0.4
    # intensity_high[-2] *= 0.55
    # intensity_high[-3] *= 0.75

    intensity_low = np.sum(intensity_low)
    intensity_high = np.sum(intensity_high)
    print('intensity_high', intensity_high)
    print('intensity_low', intensity_low)

    return np.log(intensity_high) / np.log(intensity_low)

if __name__ == '__main__':
    # component=['AIR', 60]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')

    # single items
    # component=['Fe', 0.5]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')
    # component=['Fe', 1.5]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')
    # component=['H2O', 10]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')
    # component=['H2O', 5.]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')
    # component=['SiO2', 5]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')
    # component=['SiO2', 10]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')
    # component=['C2H5OH', 5]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')
    # component=['C2H5OH', 10]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')
    # component=['TNT', 1]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')
    # component=['TNT', 5]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')

    # component=['AIR', 59.8, 'Fe', 0.2]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')
    # component=['AIR', 54.8, 'H2O', 5., 'Fe', 0.2]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')

    # component=['AIR', 49.8, 'H2O', 10., 'Fe', 0.2]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')

    # simulate bottle and water
    # component=['AIR', 90., 'H2O', 10., 'PP', 0.5]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')
    # component=['AIR', 95., 'H2O', 5., 'PP', 0.5]
    # res = calculate(component=component)
    # print('mu_high / mu_low', res, '\n-----------------')

    # some GB examples
    # Al alloy
    for i in range(1,21):
        i = float(i)
        component=['AIR', 60 - i / 10, '5A02', i / 10]
        res = calculate(component=component)
        print('mu_high / mu_low', res, '\n-----------------')
    component=['AIR', 56, '2A12', 4]
    res = calculate(component=component)
    print('mu_high / mu_low', res, '\n-----------------')
    component=['AIR', 54, '2A12', 6]
    res = calculate(component=component)
    print('mu_high / mu_low', res, '\n-----------------')

    # test9 and 10
    component=['AIR', 59.05, 'PVC', 0.95]
    res = calculate(component=component)
    print('mu_high / mu_low', res, '\n-----------------')
    component=['AIR', 57.5, 'Nylon6', 2.5]
    res = calculate(component=component)
    print('mu_high / mu_low', res, '\n-----------------')
    component=['AIR', 50., 'H2O', 10.]
    res = calculate(component=component)
    print('mu_high / mu_low', res, '\n-----------------')

