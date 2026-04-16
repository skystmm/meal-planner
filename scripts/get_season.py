#!/usr/bin/env python3
"""
季节判断脚本 - 根据城市和月份判断季节
"""

import sys
from datetime import datetime

# 城市纬度分类
CITY_ZONES = {
    # 北方（纬度 > 35）
    'north': [
        '北京', '天津', '石家庄', '太原', '沈阳', '大连',
        '长春', '哈尔滨', '济南', '青岛', '郑州', '西安',
        '兰州', '银川', '呼和浩特', '乌鲁木齐'
    ],
    # 华东（纬度 25-35）
    'east': [
        '上海', '南京', '杭州', '苏州', '无锡', '宁波',
        '合肥', '福州', '厦门', '南昌', '武汉', '长沙'
    ],
    # 华南（纬度 < 25）
    'south': [
        '广州', '深圳', '东莞', '佛山', '珠海', '中山',
        '南宁', '海口', '三亚', '昆明', '贵阳', '香港', '澳门'
    ],
    # 西南/西部
    'west': [
        '成都', '重庆', '拉萨', '西宁'
    ]
}

# 季节月份范围（按地区）
SEASON_MONTHS = {
    'north': {
        'spring': [3, 4, 5],
        'summer': [6, 7, 8],
        'autumn': [9, 10, 11],
        'winter': [12, 1, 2]
    },
    'east': {
        'spring': [3, 4, 5],
        'summer': [6, 7, 8, 9],  # 华东夏季稍长
        'autumn': [10, 11],
        'winter': [12, 1, 2]
    },
    'south': {
        'spring': [3, 4],
        'summer': [5, 6, 7, 8, 9, 10],  # 华南夏季很长
        'autumn': [11],
        'winter': [12, 1, 2]  # 华南冬季很短
    },
    'west': {
        'spring': [3, 4, 5],
        'summer': [6, 7, 8],
        'autumn': [9, 10, 11],
        'winter': [12, 1, 2]
    }
}

def get_city_zone(city: str) -> str:
    """判断城市所属区域"""
    city_lower = city.lower().replace('市', '')
    
    for zone, cities in CITY_ZONES.items():
        for c in cities:
            if city_lower in c.lower() or c.lower() in city_lower:
                return zone
    
    # 默认华东
    return 'east'

def get_season(city: str, month: int = None) -> dict:
    """
    获取季节信息
    
    Args:
        city: 城市名称
        month: 月份（默认当前月份）
    
    Returns:
        dict: {
            'season': 'spring/summer/autumn/winter',
            'season_cn': '春季/夏季/秋季/冬季',
            'zone': 'north/east/south/west',
            'month': int
        }
    """
    if month is None:
        month = datetime.now().month
    
    zone = get_city_zone(city)
    season_months = SEASON_MONTHS[zone]
    
    # 判断季节
    season = None
    for s, months in season_months.items():
        if month in months:
            season = s
            break
    
    if season is None:
        season = 'spring'  # 默认
    
    season_cn_map = {
        'spring': '春季',
        'summer': '夏季',
        'autumn': '秋季',
        'winter': '冬季'
    }
    
    return {
        'season': season,
        'season_cn': season_cn_map[season],
        'zone': zone,
        'month': month
    }

def main():
    """主函数 - 命令行调用"""
    if len(sys.argv) < 2:
        print("Usage: python3 get_season.py <城市> [月份]")
        print("示例: python3 get_season.py 北京")
        print("示例: python3 get_season.py 广州 7")
        sys.exit(1)
    
    city = sys.argv[1]
    month = int(sys.argv[2]) if len(sys.argv) > 2 else None
    
    result = get_season(city, month)
    
    # JSON 输出
    import json
    print(json.dumps(result, ensure_ascii=False))

if __name__ == '__main__':
    main()