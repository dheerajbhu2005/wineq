-- create env
    cmd - conda create -n wineq python=3.7 -y
-- activate env
    cmd - conda activate wineq
-- created a req file
    cmd - echo ""> requirements.txt  
-- install the req
    cmd - pip install -r requirements.txt
-- create floder 
    cmd -     
-- download the data from
    https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing
--  git 
    cmd - git init
          dvc init
          dvc add data_given/winequality.csv
          git add . && git commit -m "messages" && git push 
          ## git@github.com:dheerajbhu2005/wineq.git## test

          


