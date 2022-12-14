
# https://drive.google.com/file/d/1Xm-x0rJDjIOv_V0lrg4jxfF1CWX8tr_I/view?usp=share_link 



#method 1 
import pandas as pd

url='https://drive.google.com/file/d/1Xm-x0rJDjIOv_V0lrg4jxfF1CWX8tr_I/view?usp=share_link'
file_id=url.split('/')[-2]
dwn_url='https://drive.google.com/uc?id=' + file_id
df = pd.read_csv(dwn_url)

print(df.head())

