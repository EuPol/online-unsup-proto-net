import numpy as np
import os

def _read_dat(feature_dir):
    feature_data = []
    for root, dirs, files in os.walk(feature_dir):
        for name in files:
            if name.endswith('.dat'):
                file_path = os.path.join(root, name)
                #features = np.load(file_path, allow_pickle=True, fix_imports=True)
                features = np.fromfile(file_path)
                feature_data.append(features)
    return feature_data

def read_feature_data(feature_dir):
    feature_data = _read_dat(feature_dir)
    feature_data = np.stack(feature_data)
    return feature_data