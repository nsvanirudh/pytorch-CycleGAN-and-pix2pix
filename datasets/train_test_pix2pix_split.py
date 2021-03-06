# setup before running the fold:
# python scripts/combine_A_and_B.py --fold_A /path/to/data/A --fold_B /path/to/data/B --fold_AB /path/to/data

import os
import random as r

import pdb

A_SRC_DIR = '/scratch0/public/rsna-bone-age/50_views'
B_SRC_DIR = '/scratch0/public/rsna-bone-age/512/train'
DEST_DIR = '/scratch0/public/rsna-bone-age/pix2pix_50_views'

data_root = '/'.join(DEST_DIR.split('/')[:-1])

VAL_SZ = 100
TEST_SZ = 100
MAX_TRAIN_SZ = None or 1000

train = os.listdir(A_SRC_DIR)
test = r.sample(train, TEST_SZ)
for x in test:
	train.remove(x)
val = r.sample(train, VAL_SZ)
for x in val:
	train.remove(x)
if MAX_TRAIN_SZ:
	train = r.sample(train, MAX_TRAIN_SZ)

os.system('mkdir %s/A' % DEST_DIR)
os.system('mkdir %s/B' % DEST_DIR)
os.system('mkdir %s/A/train' % DEST_DIR)
os.system('mkdir %s/B/train' % DEST_DIR)
os.system('mkdir %s/A/test' % DEST_DIR)
os.system('mkdir %s/B/test' % DEST_DIR)
os.system('mkdir %s/A/val' % DEST_DIR)
os.system('mkdir %s/B/val' % DEST_DIR)

for name in train:
	os.system('cp %s/%s %s/A/train/%s' % (A_SRC_DIR, name, DEST_DIR, name))
	os.system('cp %s/%s %s/B/train/%s' % (B_SRC_DIR, name, DEST_DIR, name))

for name in test:
	os.system('cp %s/%s %s/A/test/%s' % (A_SRC_DIR, name, DEST_DIR, name))
	os.system('cp %s/%s %s/B/test/%s' % (B_SRC_DIR, name, DEST_DIR, name))

for name in val:
	os.system('cp %s/%s %s/A/val/%s' % (A_SRC_DIR, name, DEST_DIR, name))
	os.system('cp %s/%s %s/B/val/%s' % (B_SRC_DIR, name, DEST_DIR, name))
 
print('now run: (in venvconda)\n')
print('python datasets/combine_A_and_B.py --fold_A %s/A --fold_B %s/B --fold_AB %s/pix2pixmerged' % (DEST_DIR, DEST_DIR, data_root))
