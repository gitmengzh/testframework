import configparser



config_path = '../config/base_config.ini'

# config_path = 'C:\\Users\\Admin\\Desktop\\dsp\\marking-api\\Config\\base_url.ini'
class ReadConfig():
    def __init__(self):

        self.cf = configparser.ConfigParser()       # 生成cf对象
        self.cf.read(config_path)                   # 读取config文件

    def get_base_data(self, base_data):
        value = self.cf.get("base_data", base_data)
        return value

    # 获取api url路径
    def get_api(self, node_name, api_name):
        value = self.cf.get(node_name, api_name)
        base_url = self.get_base_data('base_url')
        return base_url+value





    # 获取素材路径
    def get_material_path(self,material_name):
        value = self.cf.get('MATERIAL', material_name)
        return value



if __name__ == "__main__":
    rd = ReadConfig()
    print(rd.get_base_data('auth_code'))



