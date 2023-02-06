
from collections import defaultdict

gaa_service_remote_weights_path = defaultdict()
gaa_service_remote_data_set_path = defaultdict()
gaa_service_remote_data_set_temp_path = defaultdict()

GAA_SSD = "ssd"
GAA_RESNET34 = "resnet34"
GAA_SERVICE_REMOTE_WEIGHTS_PATH_SSD = "/home/a/pytorch_ssd/weights/"
GAA_SERVICE_REMOTE_WEIGHTS_PATH_RESNET34 = "/home/a/resset/weights/"

GAA_SERVICE_REMOTE_DATA_SET_PATH_SSD = "/home/a/pytorch_ssd/VOCdevkit/BCCD/"
GAA_SERVICE_REMOTE_DATA_SET_PATH_RESNET34 = "/home/a/resset/dataset/GAA_DATA/data_set/"

GAA_SERVICE_REMOTE_DATA_SET_TEMP_PATH_SSD = "/tmp/"
GAA_SERVICE_REMOTE_DATA_SET_TEMP_PATH_RESNET34 = "/tmp/"

GAA_DATA_SET_FILE_INTERNAL_DIR = "data_set/"


gaa_service_remote_weights_path[GAA_SSD] = GAA_SERVICE_REMOTE_WEIGHTS_PATH_SSD
gaa_service_remote_weights_path[GAA_RESNET34] = GAA_SERVICE_REMOTE_WEIGHTS_PATH_RESNET34

gaa_service_remote_data_set_path[GAA_SSD] = GAA_SERVICE_REMOTE_DATA_SET_PATH_SSD
gaa_service_remote_data_set_path[GAA_RESNET34] = GAA_SERVICE_REMOTE_DATA_SET_PATH_RESNET34

gaa_service_remote_data_set_temp_path[GAA_SSD] = GAA_SERVICE_REMOTE_DATA_SET_TEMP_PATH_SSD
gaa_service_remote_data_set_temp_path[GAA_RESNET34] = GAA_SERVICE_REMOTE_DATA_SET_TEMP_PATH_RESNET34

gaa_dl_services = [GAA_SSD, GAA_RESNET34]

gaa_best_weight_file_name = "best_weight.pth"
gaa_data_set_file_name = "data_set.tar.gz"

