import pandas as pd
import h5py
import numpy as np
# Part 2
# Yu Peng dataset
YPHandheldWalk = pd.read_csv('handheldwalk.csv')
YPHandheldJump = pd.read_csv('handheldjump.csv')
YPFrontPocketWalk = pd.read_csv('frontpocketwalk.csv')
YPFrontPocketJump = pd.read_csv('frontpocketjump.csv')
YPBackPocketWalk = pd.read_csv('backpocketwalk.csv')
YPBackPocketJump = pd.read_csv('backpocketjump.csv')

# Jaime dataset
JaimeBackpackWalk = pd.read_csv('BackPackWalk.csv')
JaimeBackpackJump = pd.read_csv('BackPackJump.csv')
JaimeFrontPocketWalk = pd.read_csv('FrontPocketWalk.csv')
JaimeFrontPocketJump = pd.read_csv('FrontPocketJump.csv')
JaimeBackPocketWalk = pd.read_csv('BackPocketWalk.csv')
JaimeBackPocketJump = pd.read_csv('BackPocketJump.csv')

# Lucas dataset
LucasBackpackWalk = pd.read_csv('BackPack_Walk.csv')
LucasBackpackJump = pd.read_csv('BackPack_Jump.csv')
LucasFrontPocketWalk = pd.read_csv('FrontPocket_Walk.csv')
LucasFrontPocketJump = pd.read_csv('FrontPocket_Jump.csv')
LucasBackPocketWalk = pd.read_csv('BackPocket_Walk.csv')
LucasBackPocketJump = pd.read_csv('BackPocket_Jump.csv')

