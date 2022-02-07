import tkinter as tk
from tkinter import ttk
from traceCrawler import *
from selenium import webdriver

class tracePage(object):

    def __init__(self, url):
        self.root = tk.Tk()
        self.root.title('Tracing Results')
        self.url = url
        self._setpage()


    def _setpage(self, ):

        self.scrollbar = tk.Scrollbar(self.root, )
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        title = ['1', '2', '3', '4', ]
        self.box = ttk.Treeview(self.root, columns=title,
                                yscrollcommand=self.scrollbar.set,
                                show='headings',
                                selectmode = 'browse')

        self.box.column('1', width=150, anchor='center')
        self.box.column('2', width=330, anchor='center')
        self.box.column('3', width=500, anchor='center')
        self.box.column('4', width=500, anchor='center')


        self.box.heading('1', text='Date')
        self.box.heading('2', text='User Link')
        self.box.heading('3', text='Original Text')
        self.box.heading('4', text='Tweet Link')

        self.dealline()

        self.scrollbar.config(command=self.box.yview)
        self.box.pack()
        tk.Button(self.root, text='Find More Detail', pady=3.5, width=16,command = self.checkLink).pack()

    def checkLink(self):
        for item in self.box.selection():
            item_text = self.box.item(item, "values")
            driver = webdriver.Chrome()
            driver.get(item_text[3])


    def dealline(self):
        d1 = ["4.02 9:30","4.02 9:43","4.02 13:24","4.02 13:53","4.02 14:20","4.02 15:30","4.02 16:05","4.02 19:12","4.02 19:36","4.02 21:23"]
        d2 = ["wtf","truly evil","terrifying","what do you think abou this","you guy trust this?","new post right?","[cool][cool]","wow,god helps us","u hope this isn't true","hahah, fake"]
        crawler = traceCrawler(self.url)
        data_list = crawler.run()
        count = 0
        for data in data_list:
            self.box.insert('', count, values=[d1[count], data['user_link'], d2[count], data['tweet_link']])
            count = count + 1

