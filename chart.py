import numpy as np

import matplotlib.pyplot as plt

name = ["SIFT1M", "GIST1M", "DEEP1M", "SIFT10M", "DEEP10M", "TURING10M"]

build_time_ivfflat_faiss_training = [0.37, 1.4 , 0, 7.23, 6, 6.3]
build_time_ivfflat_faiss_adding = [ 3.03,  16.9, 0, 76, 64, 67.2]
build_time_ivfflat_pase_training = [117, 418, 47.62, 1890.23, 1250.48, 1217.43]
build_time_ivfflat_pase_adding = [117, 1109, 266.23, 3013.12, 2222.86, 2320.05]

build_size_ivfflat_faiss = [520, 3851, 0, 5201, 3921, 4081]
build_size_ivfflat_pase = [525, 3912, 1121, 5222, 3919, 3919]

query_time_ivfflat_faiss = [3.06, 6.8, 0, 7.48, 6.2, 5.8]
query_time_ivfflat_pase = [0,0, 14.866, 82.6545, 54.2096, 47.4948]

x = np.arange(len(name))  # the label locations
width = 0.35  # the width of the bars

fig , (ax)= plt.subplots(1,1)

rects1 = ax.bar(x- width/2 , build_time_ivfflat_faiss_adding, width)
rects2 = ax.bar(x- width/2 , build_time_ivfflat_faiss_training, width, bottom=build_time_ivfflat_faiss_adding)
rects3 = ax.bar(x+ width/2 , build_time_ivfflat_pase_adding, width)
rects4 = ax.bar(x+ width/2 , build_time_ivfflat_pase_training, width, bottom=build_time_ivfflat_pase_adding)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_title('IVFFlat Build Time (s)')
ax.set_xticks(x)
ax.set_xticklabels(name)
ax.legend((rects1[0],rects2[0], rects3[0],rects4[0]), ("faiss adding", "faiss training", "pase adding", "pase training"))

plt.show()