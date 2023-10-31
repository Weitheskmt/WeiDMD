import numpy as np
import matplotlib.pyplot as plt
from .hodmd import HODMD
import os
import warnings
warnings.filterwarnings("ignore")

class WeiDMD():
    def __init__(self,time,kernel,num_snapshots,nskip=1):
        self.time = time
        self.kernel = kernel
        assert num_snapshots<=self.kernel.shape[0], "num_snapshots cannot be larger than {0}!".format(self.kernel.shape[0])
        self.num_snapshots = num_snapshots
        assert nskip<self.num_snapshots, "nskip must be smaller than {0}!".format(self.num_snapshots)
        self.nskip = nskip
        
    def get_snapshots(self):
        time2 = self.time[:self.num_snapshots][::self.nskip]
        data2 = self.kernel[:self.num_snapshots][::self.nskip]
        snapshots = [d for d in data2]
        return time2, snapshots

    def plot_dmd_results(self,tf,hodmd, time_snap, kai_DD_snap, name):
        hodmd.original_time["dt"] = hodmd.dmd_time["dt"] = time_snap[1] - time_snap[0]
        hodmd.original_time["t0"] = hodmd.dmd_time["t0"] = time_snap[0]
        hodmd.original_time["tend"] = time_snap[-1]
        hodmd.dmd_time["tend"] = tf
        endl = len(hodmd.reconstructed_data[0].real)
        plt.tick_params(axis='both', which='both', direction='in')
        plt.plot(time_snap[:], kai_DD_snap[:], ".", label="Snapshots",color='blue')
        plt.plot(self.time, self.kernel, "-", color='green', label="RawData")
    
        plt.plot(
            hodmd.dmd_timesteps[:(endl)],
            hodmd.reconstructed_data[0].real,
            "--",
            label="WeiDMD",color='red'
        )

        folder_name = "./DMD_results"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        np.save('{0}/time_{1}.npy'.format(folder_name,name),hodmd.dmd_timesteps[:(endl)])
        np.save('{0}/kernel_{1}.npy'.format(folder_name,name),hodmd.reconstructed_data[0].real)
        # plt.xlim(0,lim)
        plt.tick_params(top=True,right=True)
        plt.xlabel('time',fontsize=12)
        plt.ylabel('kernel',fontsize=12)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(frameon=True,edgecolor='black',fontsize=12)
        plt.rc('font',family='serif', size=12)

    def fit(self,tf,name,d='default'):
        if d=='default':
            num_str = str(int(self.num_snapshots/self.nskip))
            num_digits = len(num_str)
            d=int(self.num_snapshots/(10^(num_digits-1)*self.nskip))
        assert isinstance(d, int), "d must be an integer!"
        assert d < self.num_snapshots/self.nskip, 'd must be smaller than {0}!'.format(int(self.num_snapshots/self.nskip))
        kernel_time_snap, kernel_snap = WeiDMD.get_snapshots(self)
        hodmd_kernel = HODMD(svd_rank=0, exact=True, opt=True, d=d).fit(np.array(kernel_snap).reshape(1,-1))
        WeiDMD.plot_dmd_results(self,tf,hodmd_kernel,kernel_time_snap, kernel_snap, name)


