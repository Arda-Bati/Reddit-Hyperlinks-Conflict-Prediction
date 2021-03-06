# -*- coding: utf-8 -*-
"""Input.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ijUVVRjcXqDRz4uIJVn6UMsDJKogPQaH
"""

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/shivamlakhotia/RedditGraph.git
# %cd RedditGraph/
!sh download_data.sh

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt



# Commented out IPython magic to ensure Python compatibility.
# %cd RedditGraph/

# data_file = open("data/reddit-hyperlinks-body.tsv")

data_frame = pd.read_csv('data/reddit-hyperlinks-body.tsv', sep='\t')

source_set = set(data_frame['SOURCE_SUBREDDIT'])

target_set = set(data_frame['TARGET_SUBREDDIT'])



edges = []
for index, row in data_frame.iterrows():
    #print(row['SOURCE_SUBREDDIT'], row['TARGET_SUBREDDIT'])
    if row['SOURCE_SUBREDDIT'] != row['TARGET_SUBREDDIT']:
        edges.append((row['SOURCE_SUBREDDIT'], row['TARGET_SUBREDDIT']))

print(len(set(edges)))

print(list(source_set)[:10])



G = nx.Graph()
G.add_nodes_from(list(source_set))
G.add_nodes_from(list(target_set))

G.add_edges_from(list(set(edges)))



plt.figure(figsize=(15, 15))
plt.subplot(111)
nx.draw(G, with_labels=False, font_weight='bold')
plt.show()





