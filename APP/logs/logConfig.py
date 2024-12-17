import logging
import time
# 配置日志记录器
current_time = time.strftime('%Y-%m-%d', time.localtime())
logging.basicConfig(
    level=logging.ERROR,  # 设置日志级别为ERROR，只记录错误信息
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    #filename=f'..\\..\\logs\\{current_time}_db_operations.log',  # 指定日志文件的名称
    filemode='a'  # 追加模式，每次记录日志在文件末尾添加
)