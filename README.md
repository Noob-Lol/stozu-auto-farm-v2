# Stozu auto farm
Automated credit farm on [stozu](https://dash.stozu.net/), speed is ~5 per minute, per instance. 

Made on Python with Selenium WebDriver.

**This is Adsense version as Linkvertise got nuked. XD**
## Update info
- Captcha solving extension as captcha was too hard.
- Switched to regular Chrome, as I implemented everything without the need for a profile.
- Unlimited speed*
> [!TIP]
> *You can open multiple cmd windows and run the sript in each, this will multiply the speed.
>
> 10x should earn about 50 credits per minute. The maximum speed is limited by your CPU. 
- No more cloudflare, i added a proxy.
- Read [proxy info](#proxy-info) for more.
# Requirements
- [Python](https://www.python.org/downloads/)
- Selenium: ```pip install selenium```
- Google Chrome
- [uBlock Origin](https://chromewebstore.google.com/detail/cjpalhdlnbpafiamejdnhcphjbkeiagm), [Buster](https://chromewebstore.google.com/detail/mpbjkejclgfgadiemmefgebjfooflfhl) extensions in your default chrome profile.
# How to use
- Download the script.
- Run script: ```py stozu_farm_ad.py```
- Guaranteed to work on Windows, other os - idk.
## Proxy info
> [!WARNING]  
> Do NOT misuse or overload the proxy! I will shutdown it if someone does.
- Logged: your IP. (cant do anything about it)
- Uptime: 99.9%. 
- Whitelisted sites: dash, free, status at stozu.net; some required sites for captcha.
- If you have a site that should be whitelisted, please contact me somewhere...
# Contributing
If you know how to improve something - make a pull request.
## Made by
n01b (discord), https://discord.gg/NoobNetwork
