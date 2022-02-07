from tkinter import *
from tkinter.messagebox import *
from selenium import webdriver
import tkinter as tk
import tkinter.messagebox
from predCrawler import *
from detection_model_load import *
from tracePage import *

class homePage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (350, 180))
        self.url = StringVar()
        self.timestep = 100
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page, text='').grid(row=1, stick=W, pady=10)
        Label(self.page, text='Tweet URL: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.url).grid(row=2, column=1, stick=E)
        Button(self.page, text='Start', command=self.start).grid(row=3, stick=W, pady=10)
        Button(self.page, text='Quit', command=self.page.quit).grid(row=3, column=1, stick=E)

    def start(self):
        url = self.url.get()
        # crawler = predCrawler(url+"?type=comment",self.timestep)
        # data_list = crawler.run()
        # model = detectModel(data_list)
        # if model.run() == True:
        #     tk.messagebox.showinfo(title='Detection Result',message='Detection Result: True')
        # else:
        #     feedback = tk.messagebox.askquestion(title='Detection Result',message='Detection Result: Fake\n\n Do you want to trace its propagation path?')
        #     if feedback == 'yes':
        #         trace = tracePage(url+"?type=repost")
        trace = tracePage(url + "?type=repost")

