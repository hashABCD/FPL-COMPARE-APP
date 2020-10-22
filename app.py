# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:44:41 2020

@author: ABCD
"""
import streamlit as st
import pandas as pd
import requests 
import numpy as np
import json
import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import seaborn as sns



alpha_dict={0:0.8,1:0.5}
color_dict={0:'blue',1:'red'}

def get_entry_personal_data(entry_id):
    """ Retrieve the summary/history data for a specific entry/team
    Args:
        entry_id (int) : ID of the team whose data is to be retrieved
    """
    base_url = "https://fantasy.premierleague.com/api/entry/"
    full_url = base_url + str(entry_id) + "/"
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data

def get_entry_data(entry_id):
    """ Retrieve the summary/history data for a specific entry/team
    Args:
        entry_id (int) : ID of the team whose data is to be retrieved
    """
    base_url = "https://fantasy.premierleague.com/api/entry/"
    full_url = base_url + str(entry_id) + "/history/"
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data
entry_list=[1,5]

def total_points_plotter(entry_ids=entry_list):
    fig=plt.figure(figsize=(8,4))
    plt.title("TOTAL POINTS")
    for i,entry in enumerate(entry_ids):
        personal_data=get_entry_personal_data(entry)
        f_name=personal_data['player_first_name']
        l_name=personal_data['player_last_name']
        name=f_name+" "+l_name
        current_data=get_entry_data(entry)['current']
        df_current=pd.DataFrame(current_data)
        #print(name)
        sns.lineplot(x='event', y='total_points', data=df_current, color=color_dict[i], 
                label=name)
    gw=np.arange(1,df_current.event.max()+1)
    plt.xlabel('Game Week')
    plt.ylabel("Total Points")
    plt.grid(axis='y')
    plt.legend()
    plt.xticks(gw)
    plt.tight_layout()
    st.pyplot(fig)
    
    
def gw_points_plotter(entry_ids=entry_list):
    fig=plt.figure(figsize=(8,4))
    plt.title("GAMEWEEK POINTS")
    for i,entry in enumerate(entry_ids):
        personal_data=get_entry_personal_data(entry)
        f_name=personal_data['player_first_name']
        l_name=personal_data['player_last_name']
        name=f_name+" "+l_name
        current_data=get_entry_data(entry)['current']
        df_current=pd.DataFrame(current_data)
        #print(name)
        sns.lineplot(x='event', y='points',data=df_current, color=color_dict[i], 
                label=name)
    gw=np.arange(1,df_current.event.max()+1)
    plt.xlabel('Game Week')
    plt.ylabel("Gameweek Points")
    plt.grid(axis='y')
    plt.ylim(bottom=0)
    plt.legend()
    plt.xticks(gw)
    plt.tight_layout()
    st.pyplot(fig)
    
    
def gw_rank_plotter(entry_ids=entry_list):
    fig=plt.figure(figsize=(8,4))
    plt.title("GAMEWEEK RANK")
    for i,entry in enumerate(entry_ids):
        personal_data=get_entry_personal_data(entry)
        f_name=personal_data['player_first_name']
        l_name=personal_data['player_last_name']
        name=f_name+" "+l_name
        current_data=get_entry_data(entry)['current']
        df_current=pd.DataFrame(current_data)
        #print(name)
        sns.lineplot(x='event', y='rank',data=df_current, color=color_dict[i], 
                label=name)
    gw=np.arange(1,df_current.event.max()+1)
    plt.xlabel('Game Week')
    plt.ylabel("Gameweek Rank")
    plt.grid(axis='y')
    plt.ylim(bottom=0)
    plt.legend()
    plt.xticks(gw)
    plt.tight_layout()
    st.pyplot(fig)
    
def overall_rank_plotter(entry_ids=entry_list):
    fig=plt.figure(figsize=(8,4))
    plt.title("OVERALL RANK")
    for i,entry in enumerate(entry_ids):
        personal_data=get_entry_personal_data(entry)
        f_name=personal_data['player_first_name']
        l_name=personal_data['player_last_name']
        name=f_name+" "+l_name
        current_data=get_entry_data(entry)['current']
        df_current=pd.DataFrame(current_data)
        #print(name)
        sns.lineplot(x='event', y='overall_rank',data=df_current, color=color_dict[i], 
                label=name)
    gw=np.arange(1,df_current.event.max()+1)
    plt.xlabel('Game Week')
    plt.ylabel("Overall Rank")
    plt.grid(axis='y')
    plt.ylim(bottom=0)
    plt.legend()
    plt.xticks(gw)
    plt.tight_layout()
    st.pyplot(fig)
    
    
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1428200698796-38743f953a43");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.header("FANTASY PREMIER LEAGUE COMPARE")
st.markdown("Enter your Entry Id and competitor's ID to compare.")
    
entry_list=[]
entry_list.append(st.text_input("Enter your Entry ID (Default ABCD XI):",6218940))
entry_list.append(st.text_input("Enter competitor Entry ID (Default Joshua Bull Defending Champion):",216079))
st.markdown("You can find entry id on points page URL")
st.image("entry_id_help.png")
total_points_plotter(entry_list)
gw_points_plotter(entry_list)
gw_rank_plotter(entry_list)
overall_rank_plotter(entry_list)

st.markdown("\N{COPYRIGHT SIGN} Abhijith Chandra Das")
st.markdown("[Follow me on Twitter for more FPL Content](https://twitter.com/intent/user?screen_name=abhijith_abcd)")
st.markdown("[Check out my articles on Medium](https://medium.com/@abhijithchandradas)")