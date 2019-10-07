from mysql import connector
from common.read_config import ReadConfig
from common import project_path


class DoMysql:
    """操作数据库的类"""

    def do_mysql(self, query, flag):
        """
        :query  sql查询语句
        :flag  标志1 获取一条数据  标志2 获取全部数据
        """
        db_config = ReadConfig(project_path.conf_path) .get_data('DB', 'db_config')  # 第一步：链接数据库 # 提供数据库的链接信息
        cnn = connector.connect(**db_config)
        cursor = cnn.cursor()  # 第二步：获取游标，获取操作数据库的权限
        # query = 'select Id,MobilePhone from member where Id <= 23528'  # 第三部：操作数据表
        cursor.execute(query)
        if flag == 1:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()  # 第四步：获取查询的结果 # 返回列表嵌套元组
        return res


if __name__ == '__main__':
    query = 'select Id from member where Id <= 23528'
    query_1 = 'select max(Id) from member where Id <= 23528'
    res = DoMysql().do_mysql(query, 1)
    print('数据库的查询结果是：{}'.format(res))

    res1 = DoMysql().do_mysql(query_1, 2)
    print('数据库的查询结果是：{}'.format(res1))