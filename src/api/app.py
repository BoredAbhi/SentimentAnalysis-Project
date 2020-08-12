# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 08:40:04 2020

@author: teeji
"""


import sys
import os
import random

from tqdm import tqdm

from flask import Blueprint, request, jsonify, Flask
import torch
import torch.nn.functional as F
import wget

import db
import db_config

from ml.model import CharacterLevelCNN
from ml.utils import predict_sentiment
model_name = 'model_en.pth'
model_path = f'./ml/models/{model_name}'
model = CharacterLevelCNN()

# download the trained PyTorch model from Github
# and save it at src/api/ml/models/
# this is done at the first run of the API

if model_name not in os.listdir('./ml/models/'):
    print(f'downloading the trained model {model_name}')
    wget.download(
        "https://github.com/abhi094/SentimentAnalysis-Project/raw/master/src/training/models/model_en_trustpilot_epoch_3_maxlen_1014_lr_0.005_loss_0.7581_acc_0.6821_f1_0.6812.pth",
        out=model_path
    )
else:
    print('model already saved to api/ml/models')

#####

# load the model
# pass it to GPU / CPU

if torch.cuda.is_available():
    trained_weights = torch.load(model_path)
else:
    trained_weights = torch.load(model_path, map_location='cpu')
model.load_state_dict(trained_weights)
model.eval()
print('PyTorch model loaded !')

#####

@api.route('/predict', methods=['POST'])
def predict_rating():
    '''
    Endpoint to predict the rating using the
    review's text data.
    '''
    if request.method == 'POST':
        if 'review' not in request.form:
            return jsonify({'error': 'no review in body'}), 400
        else:
            parameters = model.get_model_parameters()
            review = request.form['review']
            output = predict_sentiment(model, review, **parameters)
            return jsonify(float(output))