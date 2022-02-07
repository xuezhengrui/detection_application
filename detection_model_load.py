import json
import os
import numpy as np
import random
import tensorflow as tf
import tensorflow.keras.layers as KL
import time
from sentiment_test import get_sentiment_result
os.environ['TF_CPP_MIN_LOG_LEVEL']="3"
from keras.models import load_model


# load detection model to start prediction
class detectModel(object):
    def __init__(self, data_list):
        self.data_list = data_list
        self.model = load_model('./loading/detection_module/detection_model')
        self.timestep = 100

    def containEmoticon(self,str):
        if '[' in str:
            return 1
        else:
            return 0

    def countQuestionMark(self,str):
        count = 0
        for char in str:
            if char == '?':
                count += 1
        if count == 0:
            for char in str:
                if char == '？':
                    count += 1
        return count

    def countMentionMark(self,str):
        count = 0
        for char in str:
            if char == '@':
                count += 1
        return count

    def one_hot(self,label_list):
        size = len(label_list)
        one_hot_list = np.ones((size, 2))
        count = 0
        for label in label_list:
            if int(label) == 1:
                one_hot_list[count, :] = [1, 0]
            else:
                one_hot_list[count, :] = [0, 1]
            count = count + 1
        return one_hot_list

    def run(self):
        X = []
        Y = np.array([])
        fin = np.zeros((2, self.timestep, 10))
        count = 0
        for i in range(0,2):
            subcount = 0
            f_matrix = np.ones((self.timestep, 10))
            for data in self.data_list:
                f_matrix[subcount, :] = np.array(
                    [data['friends_count'], data['followers_count'], data['verified'], len(data['original_text']),
                     self.containEmoticon(data['original_text']), self.countMentionMark(data['original_text']),
                     self.countQuestionMark(data['original_text']), data['statuses_count'], data['bi_followers_count'],
                     data['emotion_status']])
                subcount = subcount + 1
            if len(self.data_list) < self.timestep:
                for i in range(len(self.data_list), self.timestep):
                    f_matrix[i, :] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            fin[count, :, :] = f_matrix
            y = 1
            Y = np.append(Y, y)
            count += 1
        label = self.one_hot(Y)
        _, res = self.model.evaluate(fin, label)
        if res > 0.5:
            return False
        else:
            return True

