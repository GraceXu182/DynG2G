#!/bin/bash

mkdir datasets
cd datasets

wget -O sbm_50t_1000n_adj.csv.tar.gz https://github.com/IBM/EvolveGCN/blob/master/data/sbm_50t_1000n_adj.csv.tar.gz\?raw\=true
tar -xvf sbm_50t_1000n_adj.csv.tar.gz 

wget https://snap.stanford.edu/data/soc-sign-bitcoinotc.csv.gz

find . -name '*.csv.gz' -exec gzip -d {} \;
wget http://konect.cc/files/download.tsv.opsahl-ucsocial.tar.bz2

mkdir as_data
cd as_data
wget http://snap.stanford.edu/data/as-733.tar.gz
tar -xvf as-733.tar.gz
cd ..

wget -O slashdot_monthly_dynamic.pkl https://github.com/moranbel/tdGraphEmbed/blob/master/data/slashdot/slashdot_monthly_dynamic.pkl?raw=true

wget -O graphs_enron_dynamic.pkl https://github.com/moranbel/tdGraphEmbed/blob/master/data/enron/graphs_enron_dynamic.pkl?raw=true

wget -O facebook_graph_dynamic.pkl https://github.com/moranbel/tdGraphEmbed/blob/master/data/facebook/facebook_graph_dynamic.pkl?raw=true

wget http://konect.cc/files/download.tsv.mit.tar.bz2

wget http://konect.cc/files/download.tsv.stackexchange-stackoverflow.tar.bz2

wget http://konect.cc/files/download.tsv.munmun_digg_reply.tar.bz2

wget http://konect.cc/files/download.tsv.delicious-ut.tar.bz2

wget http://konect.cc/files/download.tsv.dblp_coauthor.tar.bz2