cuda = True

dict_path = "/data/wangshuhe/test_mmi/mmi.dict"
data_dir = "/data/wangshuhe/test_mmi"
save_path = "/home/wangshuhe/shuhework/OpenViDial/mmi_model/feature/result"
model_path = "/home/wangshuhe/shuhework/OpenViDial/mmi_model/feature/result"

train_batch_size = 96
feature_dim = 1000
d_model = 512
nhead = 8
dim_feedforward = 2048
layer = 6
dropout = 0.1
wram_up = 4000
max_epoch = 20

dev_batch_size = 64

test_batch_size = 32