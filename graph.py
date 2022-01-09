import pickle
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("-d", "--dataset", default="as", help="Dataset Name")
parser.add_argument("-f", "--config_file", default="configs/config-1.yaml", help="Configuration file to load.")
ARGS = parser.parse_args()
if ARGS.dataset == 'as':
    name_dat = 'AS'
    time_list = [81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]

elif ARGS.dataset == 'sbm':
    name_dat = 'SBM'
    time_list = [41, 42, 43, 44, 45, 46, 47,48,49,50]

elif ARGS.dataset == 'otc':
    name_dat = 'OTC'
    time_list = [110,111,112, 113, 114, 115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137]
elif ARGS.dataset == 'uci':
    time_list = [72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87]

    name_dat = 'UCI'
    
    
elif ARGS.dataset == 'mit':
    time_list = range(72,90)

    name_dat = 'Reality_Mining'
    
    
elif ARGS.dataset == 'digg':
    time_list = range(72,90)

    name_dat = 'Digg'

    
elif ARGS.dataset == 'fb':
    time_list = range(72,90)

    name_dat = 'Facebook'

name = 'Results/'+ARGS.config_file.split('/')[1].split('.')[0] +'_' +name_dat +'/Evaluation/saved_array'

with open(name+'/MAP','rb') as f: MAP_all = pickle.load(f)
with open(name+'/MRR','rb') as f: MRR_all = pickle.load(f)
    
print(np.array(MAP_all).shape) 
    
labels = time_list




x = np.arange(len(labels))  # the label locations
width = 0.12  # the width of the bars

fig, ax = plt.subplots(figsize=(13,5))
rects1 = ax.bar(x - 2*width, MAP_all[0], width, label='16',align='center')
rects2 = ax.bar(x - width, MAP_all[1], width, label='32',align='center')
rects3 = ax.bar(x , MAP_all[2], width, label='64',align='center')
rects4 = ax.bar(x + width, MAP_all[3], width, label='128',align='center')
rects5 = ax.bar(x + 2*width, MAP_all[4], width, label='256',align='center')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('MAP', fontsize=14)
ax.set_xlabel('Timestamps', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=14)
ax.tick_params(axis="y", labelsize=14)
ax.legend(title="Embedding Size (L)", loc='upper left',ncol=5, fontsize=14)
fig.tight_layout()
plt.savefig(name+'/MAP.png', dpi=300)




x = np.arange(len(labels))  # the label locations
width = 0.12  # the width of the bars

fig, ax = plt.subplots(figsize=(13,5))
rects1 = ax.bar(x - 2*width, MRR_all[0], width, label='16',align='center')
rects2 = ax.bar(x - width, MRR_all[1], width, label='32',align='center')
rects3 = ax.bar(x , MRR_all[2], width, label='64',align='center')
rects4 = ax.bar(x + width, MRR_all[3], width, label='128',align='center')
rects5 = ax.bar(x + 2*width, MRR_all[4], width, label='256',align='center')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('MRR', fontsize=14)
ax.set_xlabel('Timestamps', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=14)
ax.tick_params(axis="y", labelsize=14)

ax.legend(title="Embedding Size (L)", loc='upper left',ncol=5, fontsize=14)
fig.tight_layout()
plt.savefig(name+'/MRR.png', dpi=300)