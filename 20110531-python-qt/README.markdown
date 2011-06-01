Ce code utilise [PySide](http://www.pyside.org/)

Les versions compilées des fichiers ui et qrc ne sont pas inclues. Pour les regénerer, les commandes suivantes : 

```bash
pyside-uic exemple2.ui -o ui_exemple2.py
pyside-uic metaFooMash.ui -o ui_metaFooMash.py
pyside-rcc metaFooMash.qrc -o rc_metaFooMash.py
```
