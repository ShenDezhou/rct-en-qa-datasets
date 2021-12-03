import json
import os
import random

import pandas
df = pandas.DataFrame()
sid = 0

for root, folders, files in os.walk('train'):
    for file in files:
        print(file)
        with open(os.path.join(root, file), 'r') as f:
            for line in f:
                item = json.loads(line.strip())
                if 'header' in item:
                    continue
                context = item['context'].split(' ')
                qa_pairs = item['qas']
                for qa_pair in qa_pairs:
                    question = qa_pair['question']
                    answer =  qa_pair['answers'][0]
                    item = {'split': "train", 'dataset': "qa-en", 'sid': sid, 'score': 1, 'sentence1': question, 'sentence2': answer}
                    df = df.append(item, ignore_index=True)
                    sid += 1
                for qa_pair in qa_pairs:
                    question = qa_pair['question']
                    answer = random.choice(context)
                    item = {'split': "train", 'dataset': "qa-en", 'sid': sid, 'score': 0, 'sentence1': question, 'sentence2': answer}
                    df = df.append(item, ignore_index=True)
                    sid += 1

for root, folders, files in os.walk('dev'):
    for file in files:
        with open(os.path.join(root,file), 'r') as f:
            for line in f:
                item = json.loads(line.strip())
                if 'header' in item:
                    continue
                context = item['context'].split(' ')
                qa_pairs = item['qas']
                for qa_pair in qa_pairs:
                    question = qa_pair['question']
                    answer =  qa_pair['answers'][0]
                    item = {'split': "dev", 'dataset': "qa-en", 'sid': sid, 'score': 1, 'sentence1': question, 'sentence2': answer}
                    df = df.append(item, ignore_index=True)
                    sid += 1
                for qa_pair in qa_pairs:
                    question = qa_pair['question']
                    answer = random.choice(context)
                    item = {'split': "dev", 'dataset': "qa-en", 'sid': sid, 'score': 0, 'sentence1': question, 'sentence2': answer}
                    df = df.append(item, ignore_index=True)
                    sid += 1

for root, folders, files in os.walk('test'):
    for file in files:
        with open(os.path.join(root,file), 'r') as f:
            for line in f:
                item = json.loads(line.strip())
                if 'header' in item:
                    continue
                context = item['context'].split(' ')
                qa_pairs = item['qas']
                for qa_pair in qa_pairs:
                    question = qa_pair['question']
                    answer =  qa_pair['answers'][0]
                    item = {'split': "test", 'dataset': "qa-en", 'sid': sid, 'score': 1, 'sentence1': question, 'sentence2': answer}
                    df = df.append(item, ignore_index=True)
                    sid += 1
                for qa_pair in qa_pairs:
                    question = qa_pair['question']
                    answer = random.choice(context)
                    item = {'split': "test", 'dataset': "qa-en", 'sid': sid, 'score': 0, 'sentence1': question, 'sentence2': answer}
                    df = df.append(item, ignore_index=True)
                    sid += 1

df.to_csv("qa-en.tsv", index=False, sep='\t', encoding='utf-8')
print('DONE')