"""
Chicago-Crime-118 (PSIT Data Analysis Project)
Overview Amount Crime each year
"""
import pandas as pd
import numpy as np
import pygal
def main():
    """ Main function """
    df_1 = np.array(pd.read_csv('2001to2004.csv', error_bad_lines=False, low_memory=False)).tolist()
    df_2 = np.array(pd.read_csv('2005to2007.csv', error_bad_lines=False, low_memory=False)).tolist()
    df_3 = np.array(pd.read_csv('2008to2011.csv', error_bad_lines=False, low_memory=False)).tolist()
    df_4 = np.array(pd.read_csv('2012to2017.csv', error_bad_lines=False, low_memory=False)).tolist()
    creat_chart(df_1, df_2, df_3, df_4)

def creat_chart(df_1, df_2, df_3, df_4):
    """ Amount Crime """
    list_year = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # list_amount_crime_2001-2017
    # amount_crime_2001to2004
    for i in df_1:
        if i[6] == 2001:
            list_year[0] += 1
        elif i[6] == 2002:
            list_year[1] += 1
        elif i[6] == 2003:
            list_year[2] += 1
        elif i[6] == 2004:
            list_year[3] += 1

    # amount_crime_2005to2007
    for i in df_2:
        if i[6] == 2005:
            list_year[4] += 1
        elif i[6] == 2006:
            list_year[5] += 1
        elif i[6] == 2007:
            list_year[6] += 1

    # amount_crime_2008to2011
    for i in df_3:
        if i[6] == 2008:
            list_year[7] += 1
        elif i[6] == 2009:
            list_year[8] += 1
        elif i[6] == 2010:
            list_year[9] += 1
        elif i[6] == 2011:
            list_year[10] += 1

    # amount_crime_2012to2017
    for i in df_4:
        if i[6] == 2012:
            list_year[11] += 1
        elif i[6] == 2013:
            list_year[12] += 1
        elif i[6] == 2014:
            list_year[13] += 1
        elif i[6] == 2015:
            list_year[14] += 1
        elif i[6] == 2016:
            list_year[15] += 1
        elif i[6] == 2017:
            list_year[16] += 1

    # creat_bar_chart_style
    amount_chart = pygal.Bar()  # creat_chart
    sum_crime = sum(list_year)  # total_crime_record
    # adding_value
    amount_chart.add('2001', [{'value':list_year[0], 'label': '{:.2f}%'.format(100*list_year[0]/sum_crime)}]).add('2002', [{'value':list_year[1], 'label': '{:.2f}%'.format(100*list_year[1]/sum_crime)}])\
    .add('2003', [{'value':list_year[2], 'label': '{:.2f}%'.format(100*list_year[2]/sum_crime)}]).add('2004', [{'value':list_year[3], 'label': '{:.2f}%'.format(100*list_year[3]/sum_crime)}])\
    .add('2005', [{'value':list_year[4], 'label': '{:.2f}%'.format(100*list_year[4]/sum_crime)}]).add('2006', [{'value':list_year[5], 'label': '{:.2f}%'.format(100*list_year[5]/sum_crime)}])\
    .add('2007', [{'value':list_year[6], 'label': '{:.2f}%'.format(100*list_year[6]/sum_crime)}]).add('2008', [{'value':list_year[7], 'label': '{:.2f}%'.format(100*list_year[7]/sum_crime)}])\
    .add('2009', [{'value':list_year[8], 'label': '{:.2f}%'.format(100*list_year[8]/sum_crime)}]).add('2010', [{'value':list_year[9], 'label': '{:.2f}%'.format(100*list_year[9]/sum_crime)}])\
    .add('2011', [{'value':list_year[10], 'label': '{:.2f}%'.format(100*list_year[10]/sum_crime)}]).add('2012',[{'value':list_year[11], 'label': '{:.2f}%'.format(100*list_year[11]/sum_crime)}])\
    .add('2013', [{'value':list_year[12], 'label': '{:.2f}%'.format(100*list_year[12]/sum_crime)}]).add('2014', [{'value':list_year[13], 'label': '{:.2f}%'.format(100*list_year[13]/sum_crime)}])\
    .add('2015', [{'value':list_year[14], 'label': '{:.2f}%'.format(100*list_year[14]/sum_crime)}]).add('2016', [{'value':list_year[15], 'label': '{:.2f}%'.format(100*list_year[15]/sum_crime)}])\
    .add('2017', [{'value':list_year[16], 'label': '{:.2f}%'.format(100*list_year[16]/sum_crime)}])
    amount_chart.legend_at_bottom = True
    # render_to_ov_amount.svg
    amount_chart.render_to_file('ov_amount.svg')
main()
