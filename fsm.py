from transitions.extensions import GraphMachine
import numpy as np
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader.data import Options
import datetime
import matplotlib.pyplot as plt

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        try :
            text = update.message.text
        except:
            return False
        return text.lower() == 'a'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'c'

    def is_going_to_state4(self, update):
        text = update.message.text
        keyword4 = text.split(',')[0]
        return keyword4 == 'findstock'

    def is_going_to_state5(self, update):
        text = update.message.text
        keyword5 = text.split(',')[0]
        return keyword5 == 'findoption'

    def is_going_to_state6(self, update):
        text = update.message.text
        keyword6 = text.split(',')[0]
        return keyword6 == 'findcurrent'

    def on_enter_state1(self, update):
        update.message.reply_text("(In state1)\n"
                                   +"please enter stock code and duration\n"
                                   +"Ex: findstock,FB,2017-01-01,2017-05-01\n"
                                   +"(FB) for facebook,\n"
                                   +"(2017-01-01, 2017-05-01) for start date and end date\n")
        # self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("(In state2)\n"
                                   +"please enter stock code\n"
                                   +"Ex: findcurrent,FB\n"
                                   +"(FB) for facebook\n")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("(In state3)\n"
                                   +"please enter stock code\n"
                                   +"Ex: findoption,FB\n"
                                   +"(FB) for facebook\n")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        update.message.reply_text("pls wait a moment...")
        text = update.message.text
        stock_name = text.split(',')[1]
        # input start_time
        start_time = text.split(',')[2]
        start_year = int(start_time.split('-')[0])
        start_month = int(start_time.split('-')[1])
        start_day = int(start_time.split('-')[2])
        # input end_time
        end_time = text.split(',')[3]
        end_year = int(end_time.split('-')[0])
        end_month = int(end_time.split('-')[1])
        end_day = int(end_time.split('-')[2])
        # get stock data
        start = datetime.datetime(start_year,start_month,start_day)
        end = datetime.datetime(end_year,end_month,end_day)
        stock = web.DataReader(stock_name,'google',start,end)

        # save time series figure
        print('Adjusted Closing Prices')
        print(stock['Close'].describe())
        ax = stock['Close'].plot(grid=True, fontsize=10, rot=45.)
        ax.set_ylabel('Adjust Closing Price($)')
        # ax.set_title(stock_name)
        plt.legend(loc='upper center', ncol=2, bbox_to_anchor=(0.5, 1.1), shadow=True, fancybox=True, prop={'size':10})
        plt.savefig('a.png')

        # send picture
        fig = open('a.png', 'rb')
        update.message.reply_photo(fig)
        fig.close()
        #print(stock.head())

        #update.message.reply_text("do you want to search more?[yes/no]\n")
        self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')

    def on_enter_state5(self, update):
        update.message.reply_text("I'm entering state5")
        text = update.message.text
        stock_name = text.split(',')[1]
        #stock_options = Options(stock_name,'google')
        #options_df = stock_options.get_options_data(expiry=stock_options.expiry_dates[0])
        #print(options_df.head())
        self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')

    def on_enter_state6(self, update):
        update.message.reply_text("I'm entering state6")
        text = update.message.text
        stock_name = text.split(',')[1]
        # cur_year = datetime.datetime.now().yaer
        # cur_month = datetime.datetime.now().month
        # cur_day = datetime.datetime.now().day

        # start = datetime.datetime(cur_year,cur_month,cur_day)
        # end = datetime.datetime(cur_year,cur_month,cur_day)
        # stock = web.DataReader(stock_name,'google',start,end)
        # print(stock.head())
        self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state6')
