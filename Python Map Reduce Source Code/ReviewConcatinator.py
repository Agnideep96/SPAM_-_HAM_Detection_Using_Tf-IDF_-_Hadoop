import json

with open('SpamDataForTFIDF.json','r') as f:
    data = json.load(f)

data_model = {}
for obj in data:
    reviewerID = obj.get('reviewerID')
    if reviewerID in data_model:
        data_model[reviewerID]+=[obj.get('reviewText')]
    else:
        data_model[reviewerID]=[]

for key,value in data_model.items():
    review = ' '.join(value)
    with open(key+'.txt','w') as reviewObj:
        reviewObj.write(review)