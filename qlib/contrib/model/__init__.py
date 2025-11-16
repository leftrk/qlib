# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
try:
    from qlib.contrib.model.catboost_model import CatBoostModel
except ModuleNotFoundError:
    CatBoostModel = None
    print("ModuleNotFoundError. CatBoostModel are skipped. (optional: maybe installing CatBoostModel can fix it.)")
try:
    from qlib.contrib.model.double_ensemble import DEnsembleModel
    from qlib.contrib.model.gbdt import LGBModel
except ModuleNotFoundError:
    DEnsembleModel, LGBModel = None, None
    print(
        "ModuleNotFoundError. DEnsembleModel and LGBModel are skipped. (optional: maybe installing lightgbm can fix it.)"
    )
try:
    from qlib.contrib.model.xgboost import XGBModel
except ModuleNotFoundError:
    XGBModel = None
    print("ModuleNotFoundError. XGBModel is skipped(optional: maybe installing xgboost can fix it).")
try:
    from .linear import LinearModel
except ModuleNotFoundError:
    LinearModel = None
    print("ModuleNotFoundError. LinearModel is skipped(optional: maybe installing scipy and sklearn can fix it).")
# import pytorch models
try:
    from qlib.contrib.model.pytorch_alstm import ALSTM
    from qlib.contrib.model.pytorch_gats import GATs
    from qlib.contrib.model.pytorch_gru import GRU
    from qlib.contrib.model.pytorch_lstm import LSTM
    from qlib.contrib.model.pytorch_nn import DNNModelPytorch
    from qlib.contrib.model.pytorch_tabnet import TabnetModel
    from qlib.contrib.model.pytorch_sfm import SFM_Model
    from qlib.contrib.model.pytorch_tcn import TCN
    from qlib.contrib.model.pytorch_add import ADD

    pytorch_classes = (ALSTM, GATs, GRU, LSTM, DNNModelPytorch, TabnetModel, SFM_Model, TCN, ADD)
except ModuleNotFoundError:
    pytorch_classes = ()
    print("ModuleNotFoundError.  PyTorch models are skipped (optional: maybe installing pytorch can fix it).")

all_model_classes = (CatBoostModel, DEnsembleModel, LGBModel, XGBModel, LinearModel) + pytorch_classes
