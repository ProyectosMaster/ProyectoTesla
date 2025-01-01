from ydata_profiling import ProfileReport
import pandas as pd
import os

path = "C:/Users/galla/Dropbox/PC/Documents/1 Pedro G Gallardo/Master IA y Big Data/Casa/proyecto tesla/ProyectoTesla/data/data_prepared/"
os.chdir(path)

df = pd.read_csv('autocasion_prepared.csv', sep=';')
profile = ProfileReport(df, title="Autocasion Report")
profile.to_file("C:/Users/galla/Dropbox/PC/Documents/1 Pedro G Gallardo/Master IA y Big Data/Casa/proyecto tesla/ProyectoTesla/data/data_prepared/autocasion_prepared.html")

df = pd.read_csv('tesla_prepared.csv', sep=';')
profile = ProfileReport(df, title="Tesla Report")
profile.to_file("C:/Users/galla/Dropbox/PC/Documents/1 Pedro G Gallardo/Master IA y Big Data/Casa/proyecto tesla/ProyectoTesla/data/data_prepared/tesla_prepared.html")

df = pd.read_csv('teslahunt_prepared.csv', sep=';')
profile = ProfileReport(df, title="Teslahunt Report")
profile.to_file("C:/Users/galla/Dropbox/PC/Documents/1 Pedro G Gallardo/Master IA y Big Data/Casa/proyecto tesla/ProyectoTesla/data/data_prepared/teslahunt_prepared.html")

df = pd.read_csv('union.csv', sep=';')
profile = ProfileReport(df, title="Data_union Report")
profile.to_file("C:/Users/galla/Dropbox/PC/Documents/1 Pedro G Gallardo/Master IA y Big Data/Casa/proyecto tesla/ProyectoTesla/data/data_prepared/union.html")