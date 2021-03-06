# from pyabsa.functional import Trainer
# from pyabsa.functional import APCConfigManager
# from pyabsa.functional import ABSADatasetList
# from pyabsa.functional import APCModelList
# import random
# import warnings
#
#
#
# warnings.filterwarnings('ignore')
#
# seeds = [random.randint(0, 10000) for _ in range(2)]
#
# apc_config_english = APCConfigManager.get_apc_config_english()
# apc_config_english.model = APCModelList.FAST_LCF_BERT
# apc_config_english.lcf = 'cdw'
# apc_config_english.similarity_threshold = 1
# apc_config_english.max_seq_len = 80
# apc_config_english.dropout = 0
# apc_config_english.optimizer = 'adam'
# apc_config_english.cache_dataset = False
# apc_config_english.patience = 10
# apc_config_english.pretrained_bert = 'microsoft/deberta-v3-base'
# apc_config_english.hidden_dim = 768
# apc_config_english.embed_dim = 768
# apc_config_english.num_epoch = 7
# apc_config_english.log_step = 10
# apc_config_english.SRD = 3
# apc_config_english.learning_rate = 1e-5
# apc_config_english.batch_size = 16
# apc_config_english.evaluate_begin = 3
# apc_config_english.l2reg = 1e-8
# apc_config_english.seed = seeds
#
# apc_config_english.cross_validate_fold = -1  # disable cross_validate
#
#
#
# Crypto1 = ABSADatasetList.CryptoDataset
#
# sent_classifier = Trainer(config=apc_config_english,
#                           dataset=Crypto1,  # train set and test set will be automatically detected
#                           checkpoint_save_mode=2,  # =None to avoid save model
#                           auto_device=True  # automatic choose CUDA or CPU
#             ).load_trained_model()
#
# examples = [
#     '[ASP]Bitcoin[ASP] to the moon. [ASP]Ethereum[ASP] is bearish.'
# ]
#
# for ex in examples:
#     result = sent_classifier.infer(ex, print_result=True)
import random

from pyabsa.functional import Trainer
from pyabsa.functional import APCConfigManager
from pyabsa.functional import ABSADatasetList
from pyabsa.functional import APCModelList

import warnings

warnings.filterwarnings('ignore')

seeds = [random.randint(0, 10000) for _ in range(2)]

apc_config_english = APCConfigManager.get_apc_config_english()
apc_config_english.model = APCModelList.FAST_LCF_BERT
apc_config_english.lcf = 'cdw'
apc_config_english.similarity_threshold = 1
apc_config_english.max_seq_len = 80
apc_config_english.dropout = 0
apc_config_english.optimizer = 'adam'
apc_config_english.cache_dataset = False
apc_config_english.patience = 10
apc_config_english.pretrained_bert = 'microsoft/deberta-v3-base'
apc_config_english.hidden_dim = 768
apc_config_english.embed_dim = 768
apc_config_english.num_epoch = 7
apc_config_english.log_step = 10
apc_config_english.SRD = 3
apc_config_english.learning_rate = 1e-5
apc_config_english.batch_size = 16
apc_config_english.evaluate_begin = 3
apc_config_english.l2reg = 1e-8
apc_config_english.seed = seeds

apc_config_english.cross_validate_fold = -1  # disable cross_validate

CryptoDataset = ABSADatasetList.CryptoDataset
Trainer(config=apc_config_english,
        dataset=CryptoDataset,  # train set and test set will be automatically detected
        checkpoint_save_mode=1,  # =None to avoid save model
        auto_device=True  # automatic choose CUDA or CPU
        )
