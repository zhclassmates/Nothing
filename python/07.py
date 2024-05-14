import pandas as pd

# 读取CSV文件
gua_link_df = pd.read_csv('/Users/zhao/Documents/gx/02/data/gua_link.csv')
hexagrams_data_df = pd.read_csv('/Users/zhao/Documents/gx/02/data/hexagrams_data.csv')  # 使用上传的新文件路径

# 确保hexagrams_data_df中的列名是正确的
hexagrams_data_df.columns = [
    'upper_number', 'upper_name', 'upper_pronounce', 'upper_representation', 'upper_meaning',
    'lower_number', 'lower_name', 'lower_pronounce', 'lower_representation', 'lower_meaning',
    'hexagram_name', 'hexagram_image', 'hexagram_meaning', 'zhou_url', 'gao_url'  # 添加新的列名 gao_url
]

def get_hexagram_info(num1, num2, num3):
    # 根据上卦和下卦的编号查找对应的卦信息
    upper_gua = hexagrams_data_df[hexagrams_data_df['upper_number'] == num1].iloc[0]
    lower_gua = hexagrams_data_df[hexagrams_data_df['lower_number'] == num2].iloc[0]

    # 查找对应的卦象信息
    hexagram_info = hexagrams_data_df[
        (hexagrams_data_df['upper_number'] == num1) & (hexagrams_data_df['lower_number'] == num2)
    ].iloc[0]

    hexagram_name = hexagram_info['hexagram_name']
    hexagram_image = hexagram_info['hexagram_image']
    hexagram_meaning = hexagram_info['hexagram_meaning']
    hexagram_url = hexagram_info['zhou_url']
    gao_url = hexagram_info['gao_url']  # 获取额外链接

    # 查找动爻信息
    change_info = gua_link_df[(gua_link_df['gui-name'].str.strip() == hexagram_image.strip()) & (gua_link_df['number3'] == num3)]
    
    if not change_info.empty:
        change_line = change_info.iloc[0]['change-number']
    else:
        change_line = "无动爻信息"

    return {
        "上卦": upper_gua['upper_name'],
        "上卦读音": upper_gua['upper_pronounce'],
        "上卦解释": upper_gua['upper_meaning'],
        "下卦": lower_gua['lower_name'],
        "下卦读音": lower_gua['lower_pronounce'],
        "下卦解释": lower_gua['lower_meaning'],
        "卦": hexagram_name,
        "卦象": hexagram_image,
        "卦象的解释": hexagram_meaning,
        "卦象的链接": hexagram_url,
        "额外链接": gao_url,
        "动爻": change_line
    }

# 输入三个数字
num1 = int(input("请输入上卦的编号: "))
num2 = int(input("请输入下卦的编号: "))
num3 = int(input("请输入动爻的编号: "))

# 获取卦象信息
result = get_hexagram_info(num1, num2, num3)

# 格式化输出结果
output = "\n".join(f"{key}: {value}" for key, value in result.items())
print(output)
