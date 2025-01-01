from ydata_profiling import ProfileReport
import pandas as pd
import os

path = "C:/Users/galla/Dropbox/PC/Documents/1 Pedro G Gallardo/Master IA y Big Data/Casa/proyecto tesla/ProyectoTesla/data/data_prepared/"
os.chdir(path)

df = pd.read_csv('union.csv', sep=';')
profile = ProfileReport(df, title="Data_union Report")
profile.to_file("C:/Users/galla/Dropbox/PC/Documents/1 Pedro G Gallardo/Master IA y Big Data/Casa/proyecto tesla/ProyectoTesla/data/data_prepared/union.html")

df = pd.read_csv('data_prepared_fact.csv', sep=';')
profile = ProfileReport(df, title="data_prepared_fact Report")
profile.to_file("C:/Users/galla/Dropbox/PC/Documents/1 Pedro G Gallardo/Master IA y Big Data/Casa/proyecto tesla/ProyectoTesla/data/data_prepared/data_prepared_fact.html")

df = pd.read_csv('data_prepared_dummies.csv', sep=';')
profile = ProfileReport(df, title="data_prepared_dummies Report")
profile.to_file("C:/Users/galla/Dropbox/PC/Documents/1 Pedro G Gallardo/Master IA y Big Data/Casa/proyecto tesla/ProyectoTesla/data/data_prepared/data_prepared_dummies.html")