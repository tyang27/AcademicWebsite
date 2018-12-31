# Academic Website for Tony Y

```
source bin/activate.sh
pip install -r requirements.txt
```
If you get this error:
```
error: could not create '/Library/Python/2.7/site-packages/blinker': Permission denied
```
Resolve by running code [ref](https://github.com/sindresorhus/weechat-notification-center/issues/1):
```
sudo chown -R $USER /Library/Python/2.7
```
