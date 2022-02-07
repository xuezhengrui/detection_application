import json
import os
import numpy as np
import random
import tensorflow as tf
import tensorflow.keras.layers as KL
os.environ['TF_CPP_MIN_LOG_LEVEL']="3"
from sentiment_test import get_sentiment_result

def containEmoticon(str):
    if '[' in str:
        return 1
    else:
        return 0

def countQuestionMark(str):
    count = 0
    for char in str:
        if char == '?':
            count += 1
    return count

def countMentionMark(str):
    count = 0
    for char in str:
        if char == '@':
            count += 1
    return count

# conduct one-hot representation for label vectors
def one_hot(label_list):
    size = len(label_list)
    one_hot_list = np.ones((size,2))
    count = 0
    for label in label_list:
        if int(label) == 1:
            one_hot_list[count,:]=[1,0]
        else:
            one_hot_list[count,:]=[0,1]
        count = count + 1
    return one_hot_list

# invoke sentiment prediction
def emotion_pre(data_list):
    count = 0
    with open("./datasets/comments/test.txt", "w", encoding='utf-8') as f:
        for tweet_chain in data_list:
            for tweet in tweet_chain:
                f.write(tweet['original_text'] + '\n')
                count = count + 1
    pre_list = get_sentiment_result().tolist()

    if (count != len(pre_list)):
        print("Error")
        return None
    index = 0
    for tweet_chain in data_list:
        for data in tweet_chain:
            data['emotion_status'] = pre_list[index]
            index = index + 1


# read dataset key info
dataset = []
with open("./datasets/tweets/Tweets Dataset.txt","r") as f:
    for line in f:
        mid = line.split()[0].split(':')[1]
        label = line.split()[1].split(':')[1]
        temp = [mid,label]
        dataset.append(temp)

# specify required length of propagation pattern
timestep=100

# extract features
data_list = []
for item in dataset:
    str = './datasets/tweets/data/'+item[0]+'.json'
    with open(str) as f:

        event_list = []
        load_dict = json.load(f)
        count = len(load_dict)

        if count < timestep:
            for i in range(0, count):
                data = {}
                if i == 0:
                    data['picture'] = load_dict[i]['picture']
                    data['label'] = item[1]
                    data['length'] = count
                data['mid'] = load_dict[i]['mid']
                data['uid'] = load_dict[i]['uid']
                data['friends_count'] = load_dict[i]['friends_count']
                data['original_text'] = load_dict[i]['original_text']
                data['verified'] = load_dict[i]['verified']
                data['followers_count'] = load_dict[i]['followers_count']
                data['reposts_count'] = load_dict[i]['reposts_count']
                data['statuses_count'] = load_dict[i]['statuses_count']
                data['bi_followers_count'] = load_dict[i]['bi_followers_count']
                data['emotion_status'] = -1
                event_list.append(data)
        else:
            for i in range(0, timestep):
                data = {}
                if i == 0:
                    data['picture'] = load_dict[i]['picture']
                    data['label'] = item[1]
                    data['length'] = count
                data['mid'] = load_dict[i]['mid']
                data['uid'] = load_dict[i]['uid']
                data['friends_count'] = load_dict[i]['friends_count']
                data['original_text'] = load_dict[i]['original_text']
                data['verified'] = load_dict[i]['verified']
                data['followers_count'] = load_dict[i]['followers_count']
                data['reposts_count'] = load_dict[i]['reposts_count']
                data['statuses_count'] = load_dict[i]['statuses_count']
                data['bi_followers_count'] = load_dict[i]['bi_followers_count']
                data['emotion_status'] = -1
                event_list.append(data)
        data_list.append(event_list)

# invoke sentiment analysis module
emotion_pre(data_list)

# construct propagation pattern
X = []
Y = np.array([])
fin = np.zeros((len(data_list),timestep,10))
count = 0
random.shuffle(data_list)

for data in data_list:
    subcount = 0
    event_matrix = np.ones((timestep,10))

    for event in data:
        event_matrix[subcount,:] = np.array([event['friends_count'], event['followers_count'],event['verified'],len(event['original_text']),containEmoticon(event['original_text']),countMentionMark(event['original_text']),countQuestionMark(event['original_text']),event['statuses_count'],event['bi_followers_count'],event['emotion_status']])
        subcount = subcount+1

    if data[0]['length'] < timestep:
        for i in range(data[0]['length'],timestep):
            event_matrix[i,:] = [0,0,0,0,0,0,0,0,0,0]

    fin[count,:,:] = event_matrix
    y = data[0]['label']
    Y = np.append(Y,y)
    count += 1

# data samples separation
x_train = fin[0:3000,:,:]
y_train = one_hot(Y[0:3000])

x_test = fin[3000:,:,:]
y_test = one_hot(Y[3000:])

# model configuration
inputs = KL.Input(shape=(100,10))
x=KL.SimpleRNN(128)(inputs)
outputs=KL.Dense(2,activation="sigmoid")(x)

model = tf.keras.models.Model(inputs, outputs)
model.summary()
opt = tf.keras.optimizers.Adam(
    learning_rate=0.001,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-07,
    amsgrad=False,
    name="Adam"
)

model.compile(optimizer=opt,
              loss="binary_crossentropy",
              metrics=["acc"])
model.fit(x_train, y_train, batch_size=100,epochs=180)
test_loss, test_acc=model.evaluate(x_test,y_test)
print("Loss: {0} - Acc: {1}".format(test_loss,test_acc))