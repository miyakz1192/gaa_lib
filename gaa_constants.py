
from collections import defaultdict

gaa_service_remote_weights_path = defaultdict()
GAA_SSD = "ssd"
GAA_RESNET34 = "resnet34"
GAA_SERVICE_REMOTE_WEIGHTS_PATH_SSD = "/home/a/pytorch_ssd/weights/"
GAA_SERVICE_REMOTE_WEIGHTS_PATH_RESNET34 = "/home/a/resset/weights/"

gaa_service_remote_weights_path[GAA_SSD] = GAA_SERVICE_REMOTE_WEIGHTS_PATH_SSD
gaa_service_remote_weights_path[GAA_RESNET34] = GAA_SERVICE_REMOTE_WEIGHTS_PATH_RESNET34

gaa_dl_services = [GAA_SSD, GAA_RESNET34]

gaa_best_weight_file_name = "best_weight.pth"

