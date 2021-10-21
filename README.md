# 🗡 Saber for sublime text
a plugin generate random css name for sublime

## 😇 How to install
1. Clone or [download](https://github.com/nixend/saber) git repo into your packages folder (in SublimeText find Browse Packages... menu item to open this folder)
2. Restart SublimeText editor

## 🥲 How to use
Focus somewhere you want to insert the css name and then press the keys.
1. Mac: ```shift+command+s```
2. Windows: ```shift+ctrl+s```

The generated name has been copied, just paste it in your css file.

## 🤩 Enjoy yourself!
---

# 🛠 Setting
👇 Copy this to SublimeText > Preferences > Settings
```js
{
	"saber_str":"abcdefghijklmnopqrstuvwxyz1234567890",  //name generate from this string
	"saber_prefix":"sa",  //name prefix, ex: sa-maevmk, if empty the prefix is ignore, ex: maevmk
	"saber_length":6  //name lenth, not include the prefix
}
```
