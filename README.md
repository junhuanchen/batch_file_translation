# batch_file_translation

脚本测试环境为 Windows10 Python3.5.4 依赖请查看 requirements.txt 。

## google_translate.py 

本脚本直接调取谷歌翻译 API ，用以将各类语言转换为英文，或转换为简体中文，感谢 API 作者（我忘了代码是从哪个人那里提取修复的了，有心可以自己搜索得到，并不难找）。

```python
import google_translate
print(get_zh('hello'))
print(get_translate_zh('who?'))
print(get_translate('賈拉爾普爾'))
```

## extract_all_files.py

该脚本用于提取某个文件夹中你想要的文件（主要应用于文本文件），并复现导出到同样结构的文件夹。

```python
extract_file(source_dir='test', goal_dir='result\\')

extract_file(source_dir='test', goal_dir='result\\', function=google_translate.get_translate_zh)
```

前者文件直接读取后写入，后者将内容将读取后经过 翻译函数转换（google_translate.get_translate_zh） 得到后写入。

## Application

最近我们的文档需要由中转英，繁体转简体后，预处理后再交给人工校正。
