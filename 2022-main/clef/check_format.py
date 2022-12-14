# -*- coding: utf-8 -*-

def check_format(df,columns):
  df.columns= df.columns.str.lower()
  for c in columns:
    if not c.lower() in df.columns:
      print('ERROR:\n\tThere is no column named '+c+'\n\t\tPlease check the format. You can find format requirements at https://simpletext-project.com/')
  if not df['manual'].isin([0,1]).prod():
    print('ERROR:\n\tThere is an error in the column MANUAL. The values should be in [0,1]. '+c+'\n\t\tPlease check the format. You can find format requirements at https://simpletext-project.com/')
  if df['run_id'].str.lower().str.split(r"_task_?\d_?",expand=True).shape[1]!=2:
    print('ERROR:\n\tRUN_ID must have the following format: TEAM_ID_TASK_ID_RUN_NAME, e.g. BTU_TASK_2_MANUAL or UBO_TASK3_RUN_1. \n\t\tPlease check the format. You can find format requirements at https://simpletext-project.com/')

def check_json(fn,columns):
  import pandas as pd
  try:
    df=pd.read_json(fn)
    check_format(df,columns)
  except Exception as e:
    print (e)
    print('ERROR:\n\tThe file is not found or it is not in a JSON format\n\t\tPlease check the format. You can find format requirements at https://simpletext-project.com/')

def check_csv(fn,columns):
  import pandas as pd
  try:
    df=pd.read_csv(fn, sep='\t')
    check_format(df,columns)
  except Exception as e:
    print (e)
    print('ERROR:\n\tThe file is not found or it is not in a CSV format with the TAB separator\n\t\tPlease check the format. You can find format requirements at https://simpletext-project.com/')

def joker_check_json_task_1(fn):
  check_json(fn,['RUN_ID','MANUAL','id',"WORDPLAY","TARGET_WORD","DISAMBIGUATION","HORIZONTAL\/VERTICAL","MANIPULATION_TYPE","MANIPULATION_LEVEL","CULTURAL_REFERENCE","CONVENTIONAL_FORM","OFFENSIVE"])

def joker_check_json_task_2(fn):
  check_json(fn,['RUN_ID','MANUAL','id','en','fr'])

def joker_check_json_task_3(fn):
  check_json(fn,['RUN_ID','MANUAL','id','en','fr'])

def joker_check_csv_task_1(fn):
  check_csv(fn,['RUN_ID','MANUAL','id',"WORDPLAY","TARGET_WORD","DISAMBIGUATION","HORIZONTAL\/VERTICAL","MANIPULATION_TYPE","MANIPULATION_LEVEL","CULTURAL_REFERENCE","CONVENTIONAL_FORM","OFFENSIVE"])

def joker_check_csv_task_2(fn):
  check_csv(fn,['RUN_ID','MANUAL','id','en','fr'])

def joker_check_csv_task_3(fn):
  check_csv(fn,['RUN_ID','MANUAL','id','en','fr'])

def simpletext_check_json_task_1(fn):
  check_json(fn,['RUN_ID','MANUAL','topic_id','query_id','doc_id','passage'])

def simpletext_check_json_task_2(fn):
  check_json(fn,['RUN_ID','MANUAL',"snt_id","term","term_rank_snt","score_5","score_3"])

def simpletext_check_json_task_3(fn):
  check_json(fn,['RUN_ID','MANUAL','snt_id','simplified_snt'])

def simpletext_check_csv_task_1(fn):
  check_csv(fn,['RUN_ID','MANUAL','topic_id','query_id','doc_id','passage'])

def simpletext_check_csv_task_2(fn):
  check_csv(fn,['RUN_ID','MANUAL',"snt_id","term","term_rank_snt","score_5","score_3"])

def simpletext_check_csv_task_3(fn):
  check_csv(fn,['RUN_ID','MANUAL','snt_id','simplified_snt'])

import argparse

parser = argparse.ArgumentParser(description='Check CLEF output format.')
parser.add_argument('-filename', dest='fn', required=True, help='Full file name to check')
parser.add_argument('-track', dest='track', required=True, choices=['joker','simpletext'],help='CLEF lab name: joker or simpletext')
parser.add_argument('-task', dest='task', required=True, choices=['1','2','3'],help='Task id: 1, 2 or 3')

args = parser.parse_args()

import os

ext=os.path.splitext(args.fn)[1][1:]

locals()[args.track+"_check_"+ext+"_task_"+str(args.task)](args.fn)
