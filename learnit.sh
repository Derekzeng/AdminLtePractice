cd C:\Users\Administrator\PycharmProjects\Learnit
git pull origin master
cd C:\User\Administrator\PycharmProjects\Learnit
git add -- .idea.learn.iml .idea/scopes/scope_setting.xml
cd C:\Users\Administrators\PycharmProjects\Learnit
git checkout -b dev
git checkout -b master
git checkout -b dev
git add -- readme.txt
git -rm -f -- .idea.learn.iml .idea/scopes/scope_settings.xml
git commit -m 'add file readme.txt' -- readme.txt
git log HEAD --
git merge dev
git checkout d5e3749
git checkout -b dev1 d5e3749
git add -- learnit.sh
git commit -m 'add learnit.sh' -- learnit.sh
git checkout d5e3749
git merge dev1
git checkout dev1
git commit -m 'xxxx' -- learnit.sh
git checkout d5e3749
git merger dev1
git branch -D dev
git push origin master


