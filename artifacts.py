import os
import time
from cnvrg import Experiment
e = Experiment()
for commit in range(5):
    file_list = []
    for i in range(25):
        with open(f"output/filet{i}.txt", 'w+') as file:
            file.write('hello')
        with open(f"output/filet{i}.txt_tags.yml", 'w+') as yml:
            yml.write(f"---\nid: \"{i}\"\nsource: \"yann lecun\"")
        file_list.append(f"output/filet{i}.txt")
        file_list.append(f"output/filet{i}.txt_tags.yml")
    e.log_artifacts(file_list)
    time.sleep(5)
    print(f"commited: {commit}")
