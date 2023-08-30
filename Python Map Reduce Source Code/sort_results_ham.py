import pandas as pd;
import glob;

folderPath = "/home/agnideep_mukherjee2/TFIDF_Spam/results";

allFiles = glob.glob(folderPath + "/*.txt");

for completeFilePath in allFiles:
    filename = completeFilePath.split('/tfidResults/')[1];
    print('-------------------------------------');
    print('   '+filename.split('.')[0]+' <- Reviewer ID');
    df = pd.read_csv(completeFilePath, sep="\t",header=None,names=["word","TF-IDF Score"]);
    print('-------------------------------------');
    df["word"] = df["word"].str.split(" ",n=1,expand=True);
    result = df.sort_values(by = ["TF-IDF Score"], ascending=False).head(10);
    print(result);
    print('\n\n');