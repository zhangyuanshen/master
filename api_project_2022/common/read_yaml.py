import yaml
import os
from config.config import ROOT_PATH
# from nb_log import LogManager
# logpath = os.path.join(ROOT_PATH,"log")
# logger = LogManager("ceshi").get_logger_and_add_handlers(
#     log_filename="yuanshen.log",log_path=logpath)

def yaml_to_python(yaml_path):
    """yaml转python类型"""
    # logger.debug("读取yml文件，转python类型")
    # logger.info("读取yml文件获取文件地址：%s"% yaml_path)
    f = open(yaml_path, "r", encoding="utf-8")
    fp = f.read()
    d = yaml.safe_load(fp)
    f.close()
    return d

if __name__ == '__main__':
    # 当前文件的位置（不同文件夹内时要一层一层获取位置）
    curpath = os.path.realpath(__file__)
    # print(curpath)
    # 向上寻找两层 找到项目文件夹的位置
    root_path = os.path.dirname(os.path.dirname(curpath))
    # print(root_path)
    # 从项目文件夹位置向下加入 yml所在文件夹和文件名 获得最终位置（如果yml文件在同一个文件夹里，使用相对路径 可直接根据名称获取位置即 yaml_path="文件名"）
    yaml_path = os.path.join(ROOT_PATH, "data", "login_data.yml")
    result = yaml_to_python(yaml_path)
    print(result)