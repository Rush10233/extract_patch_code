# extract_patch_code
c++编译器补丁源码爬取脚本
## 如何启动
- Pycharm（或其他任何python开发环境）新建一个项目
- 设置命令行参数为add.txt(或者其他任何存放补丁链接的文档的位置）
- 把所有需要爬取的补丁页链接粘贴在add.txt（命令行参数设置的文档）中，一行粘贴一个链接
- 运行，等待结果
- 如果中途出错，检查一下补丁页的title是否包含不能用于文件命名的字符（比如：和<,>），可以尝试通过在extract_source.py的末尾添加替换命令来解决
