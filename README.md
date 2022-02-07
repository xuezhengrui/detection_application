# detection_application
Detection Fake Content on Weibo using Recurrent Nerual Network

## Project Overview:
Three RNN-based models have been trained using Weibo Dataset. The detection program is built on an LSTM network with the simple GUI, which can achieve veracity prediction given the URL of an image tweet on Weibo. This detection program is version 1.0, for which the main goal is to achieve high accuracy on Dataset and have the detection ability for real tweets on Weibo without labels to some extend. As the version of the program upgrades in the future, the detection accuracy of the model for real tweets on Weibo will be improved.


## Package Introduction
./
main.py：		start-up file of the detection program
readdata.py: 		provides a variety of data-loading APIs for sentiment analysis on user comments
word2vec.py: 		provides a variety of word-vector APIa for sentiment analysis on user comments
sentiment_train.py: 	implements training for sentiment analysis model and saves well-trained model
sentiment_test.py: 	implements testing for sentiment analysis model
sentiment_lstm_model.py: 	implements LSTM network for sentiment analysis
detection_model_load.py:	restores well-trained detection model 
detection_lstm_train.py:	implements training for LSTM-based detection model and saves the model
detection_rnn_train.py:	implements training for tank-RNN detection model
detection_gru_train.py:	implements training for GRU-based detection model
traceCrawler.py:		implements data extraction from Weibo for source tracing
preCrawler.py:		implements data extraction from Weibo for veracity prediction
homePage.py:		home interface of the detection program


./datasets/tweets
Tweets Dataset.txt:	contains tweet mid and label(0: true; 1: fake)
data file:		contains detail information of each tweet

./datasets/comments
neg.txt:			contains negative user comments 
pos.txt:			contains positive user comments
test.txt:		contains user comments for real prediction

NOTE: If datasets file is missing, please check MS Forms Submission or download it from https://pan.baidu.com/s/1uXXr38njeqKyUANZzlP7Ag (Password: govr)

./loading
embedding_64.bin: 	well-trained word vector module
detection_module file:	stores LSTM-based detection model
sentiment_module file:	stores parameters, training and testing logs of sentiment analysis model

NOTE: embedding_64.bin exceeds the maximum limit of uploading FYP source files, please download it from https://pan.baidu.com/s/1dtA_1nQM4AlAPbd4jQ2tCg (Password: tue3) and move it to the 'loading' directory.



## Running Environment:
Python 3.0 or higher
Tensorflow 2.0 or higher
macOS 64 Bit / Linux 64 Bit


## Usage:
1. To start the detection program: 	run main.py
2. To check training process of each model: 	run sentiment_train.py, detection_lstm_train.py, detection_rnn_train.py or detection_gru_train.py respectively
 

## Important Notes for Running Detection Program:
1. Please set the Chrome browser as the default browser before running the detection Program
2. Download chromedriver that matches the version of your Chrome browser (e.g http://npm.taobao.org/mirrors/chromedriver)
3. After unzipping the chromedriver package, add the executable program to PATH environment variable 
4. As the input URL of the detection program, you should copy the URL of a tweet with the format such as 'https://weibo.com/2146226217/Ithnlkypn'
5. Please do not perform any other operation while the detection program is running
6. Each round of detection usually takes 4-5 minutes to be finished, which depends on the network and memory usage
7. Logging in to Weibo account and keeping cookies before the detection can speed up the detection process
8. Do not switch Weibo to English mode
9. Try to restart the detection program if you meet some problems
10. For fast checking, you could start the detection program using following URLs:
https://weibo.com/2146226217/Ithnlkypn
https://weibo.com/2146226217/I10Rs06kk
11. Feel free to contact scyzx1@nottingham.edu.cn if you need extra support



