# PipTUI
Pip GUI in your terminal!

![main](https://user-images.githubusercontent.com/41646249/61582508-8c2e3b80-ab34-11e9-8e53-a8439c0f2e04.png)
![search](https://user-images.githubusercontent.com/41646249/61582525-a5cf8300-ab34-11e9-8724-fe09d8471e12.png)


### Installation

```bash
pip3 install PipTUI
```


### Running it:
```bash
piptui
```

### Shortcuts

* Install package: `Ctrl-A`
* Uninstall package: `Ctrl-R`
* Update package: `Ctrl-U`



### DISCLAIMER

This app only works if `pip` is installed and it's not a pip alternative, it's just GUI wrapper for the pip commands! 

If you're using other ways to install python packages some changes should be made in your end. A little example is to set a pip alias if you're using apps like `pipx` to install python packages!


### Theming


To theme the app create a json file in `your home dir/.piptui/theme.json` then copy and edit the content of `theme_example.json`


Available Colors:

* BLACK_RED
* MAGENTA_BLACK
* BLUE_BLACK
* YELLOW_BLACK
* BLACK_YELLOW
* BLACK_GREEN
* RED_BLACK
* YELLOW_WHITE
* CYAN_BLACK
* GREEN_WHITE
* RED_WHITE
* CYAN_WHITE
* BLUE_WHITE
* GREEN_BLACK
* MAGENTA_WHITE
* BLACK_WHITE


Export `PIPTUI_TRANSPARENT=True` to your env variables and enable transparent color sets:

* CYAN_ON_DEFAULT
* BLUE_ON_DEFAULT
* WHITE_ON_DEFAULT
* GREEN_ON_DEFAULT
* BLACK_ON_DEFAULT
* MAGENTA_ON_DEFAULT
* YELLOW_ON_DEFAULT
* RED_ON_DEFAULT

