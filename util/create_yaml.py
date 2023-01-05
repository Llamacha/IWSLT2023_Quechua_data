import pandas as pd
import librosa
import os

def duration(file):
    du = librosa.get_duration(filename=file)
    return du

def create_files():
    df = pd.read_csv("meta.tsv", sep="\t")
    with open('train.qu','w') as f:
        for index, row in df.iterrows():
            f.write(str(row["source_raw"]))
            f.write("\n")   
    with open('train.es','w') as f:
        for index, row in df.iterrows():
            f.write(str(row["target_raw"]))
            f.write("\n")
        
        
def create_yaml():
    FILEPATH = os.path.dirname("data/dev/wav/")
    raw_dirs = set([d for d in os.listdir(FILEPATH)])
    with open('test.yaml','w') as f:
        flag = 1
        for a in sorted(raw_dirs):
            du = duration(FILEPATH+"/"+a)
            f.write("- {duration:"+str(du)+", offset: 0.0, speaker_id: spk."+str(flag)+", wav:"+a+"}")
            f.write("\n")
            flag+=1
        
create_yaml()