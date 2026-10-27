Assignment One - 上传说明
作者：Yuyang Ge

压缩包包含：
1. assignment 1_yourname.py：唯一的 Python 主提交文件。
2. Assignment1_Submission_Yuyang_Ge.pdf：Moodle 提交用 PDF，含 GitHub 链接和两张运行截图。
3. turtle_drawing.png：实际 Turtle 绘图截图。
4. qa_bot.png：实际问答函数运行记录的截图；测试时向 input() 提供了预设问题。
5. README_UPLOAD.txt：本说明，不必交到 Moodle。

上传步骤：
1. 解压整个压缩包。
2. 打开已创建的公开仓库：
   https://github.com/21echo12/assignment1-python-basics
   当前尚未上传作业代码；请自行上传。
3. 在仓库中选择 uploading an existing file（空仓库）或 Add file > Upload files。
4. 上传 assignment 1_yourname.py，点击 Commit changes。
   请保留文件名中的空格，不要上传 __pycache__ 或其他测试辅助文件。
5. 确认仓库中能看到并打开该 Python 文件。
6. 把 Assignment1_Submission_Yuyang_Ge.pdf 上传到 Moodle 的 Assignment One。
   Moodle 要求的是 PDF；整个 ZIP 是给你下载和整理用的。

PDF 已填入上述仓库链接。若你改用其他 GitHub 仓库，提交前需要把 PDF 中的链接同步改为实际地址。

文件头遵循课件第 38 页的模板：
# Name: Yuyang Ge
# Assignment One

运行要求：Python 3，标准库 turtle/Tk，带图形桌面的环境。
Jetson/Linux 桌面终端：
python3 "assignment 1_yourname.py"
Windows（python 已配置为 Python 3 的终端）：
python "assignment 1_yourname.py"

菜单：1 = Turtle 绘图，2 = QA Bot，3 = 课件选做计算器，0 = 退出。
绘图完成后点击绘图窗口返回菜单。
问答输入 exit 或 quit 返回菜单。
问答支持 HKU、robot、jetson、ai、human，忽略大小写并支持标点。
若一句话包含多个关键词，按代码中 if/elif 的顺序选择第一个匹配主题。

已验证：Python 语法、五个关键词、大小写和标点、未知问题、空输入、退出、菜单，以及计算器运算和异常输入；18 项检查通过。