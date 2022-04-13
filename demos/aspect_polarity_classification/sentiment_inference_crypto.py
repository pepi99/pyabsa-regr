from pyabsa import ABSADatasetList, APCCheckpointManager, available_checkpoints
checkpoint = '/Users/petar.ulev/Documents/Python/PyABSA/checkpoints/fast_lcf_bert_Crypto_acc_0.01501880839690505_f1_0'

model = APCCheckpointManager.get_sentiment_classifier(checkpoint=checkpoint)
model.infer('Hey I Think [ASP]bitcoin[ASP] is amazing! But on the other hand, [ASP]eth[ASP] sucks...')
