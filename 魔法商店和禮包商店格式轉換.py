currency_mapping={
    "candles": "蜡烛",
    "heart": "心",
    "prestige": "升华蜡",
    "season_candle": "季蜡",
    "season_heart": "季心",
    "event_candle_days_of_feast": "盛宴日活动蜡烛",
    "event_candle_days_of_competition": "竞赛日活动蜡烛",
    "event_candle_days_of_fortune": "幸运日活动蜡烛",
    "event_candle_days_of_love": "爱之日活动蜡烛",
    "event_candle_days_of_bloom": "花之日活动蜡烛",
    "event_candle_days_of_nature": "自然日活动蜡烛",
    "event_candle_days_of_music": "音乐日活动蜡烛",
    "event_candle_days_of_color": "彩虹日活动蜡烛",
    "event_candle_days_of_sunlight": "夏之日活动蜡烛",
    "event_candle_days_of_fashion": "时尚日活动蜡烛",
    "event_candle_days_of_aurora": "Aurora日活动蜡烛",
    "event_candle_days_of_fireworks": "烟火日活动蜡烛",
    "event_candle_days_of_mischief": "万圣节活动蜡烛",
    "event_candle_days_of_pastrycafe": "咖啡日活动蜡烛",
}

event_mapping = {
    "weekly_prop_rotation_01" : "第1周",
    "weekly_prop_rotation_02" : "第2周",
    "weekly_prop_rotation_03" : "第3周",
    "weekly_prop_rotation_04" : "第4周",
    "weekly_prop_rotation_05" : "第5周",
    "weekly_prop_rotation_06" : "第6周",
    "weekly_prop_rotation_07" : "第7周",
    "weekly_prop_rotation_08" : "第8周",
    "weekly_prop_rotation_09" : "第9周",
    "weekly_prop_rotation_10" : "第10周",
    "weekly_prop_rotation_11" : "第11周",
    "weekly_prop_rotation_12" : "第12周",
    "weekly_prop_rotation_13" : "第13周",
    "global_pc_launch" : "PC发行日",
    "global_weekend_shop" : "周末",
    "global_halloween" : "万圣节",
    "global_feast" : "盛宴日",
    "global_daysoffortune" : "幸运日",
    "global_daysoflove" : "爱之日",
    "global_bloom" : "花之日",
    "global_cafe" : "咖啡日",
    "global_nature_2024" : "自然日",
    "global_rainbow" : "彩虹日",
    "global_skyfest" : "周年庆",
    "global_competition" : "锦标赛日",
    "global_music" : "音乐日",
    "daysofmusic_secretnote" : "未知",
    "global_summer" : "夏之日",
    "global_violin" : "小提琴日"
}

reset_event_mapping = {
    "gen_shop_daily_reset" : "1天",
    "gen_shop_weekly_reset" : "1周",
    "gen_shop_monthly_reset" : "1个月",
    "gen_shop_yearly_reset" : "1年"
}

shop_name_mapping = {
    "SpellShop_PClaunch_Scroll" : "PC魔法商店",
    "SpellShop_MainStreet_Boat" : "云巢魔法商店",
    "PropShop_MainStreet_Quest01" : "云巢工坊任务1",
    "SpellShop_Oasis_Spell" : "遇境魔法商店1",
    "SpellShop_Oasis_Scroll" : "遇境魔法商店2",
    "SpellShop_Oasis_Potion" : "遇境魔法商店3",
    "SpellShop_SunsetVillage_Scroll" : "圆梦村魔法商店",
    "SpellShop_MischiefCrab_Spell" : "万圣节魔法商店",
    "SpellShop_Mischief_Spell" : "万圣节魔法商店2",
    "SpellShop_Feast_Spell" : "盛宴日魔法商店",
    "SpellShop_Fortune_Spell" : "幸运日魔法商店",
    "SpellShop_Firework_Spell" : "烟火日魔法商店",
    "SpellShop_Love_Spell" : "爱之日魔法商店",
    "SpellShop_FortuneSunset_Spell" : "幸运日魔法商店2",
    "EventShop_MainStreet_Cafe" : "云巢咖啡魔法商店",
    "EventShop_MainStreet_Pastry" : "云巢咖啡魔法商店",
    "SpellShop_Nature_Spell" : "自然日魔法商店",
    "SpellShop_Color_Spell" : "彩虹日魔法商店",
    "SpellShop_Sky_Spell" : "周年庆魔法商店",
    "SpellShop_Competition_Spell" : "锦标赛日魔法商店",
    "SpellShop_Music_Spell" : "音乐日魔法商店",
    "SpellShop_DoMusic_Spell" : "音乐日魔法商店2",
    "SpellShop_Sunlight_Spell" : "夏之日魔法商店",
    "PropShop_MainStreet_PropTest" : "家具商店"
}


with open('your file path','r', encoding='utf-8') as files:
    
    name = None
    currency = None
    cost = None
    item_count = None
    event_name = None

    for line in files:
        
        
        if '"name":'in line :
            start_index = line.find('"name":') + len('"name":')
            end_index = line.find(',', start_index)
            if end_index == -1:
                end_index = line.find('}', start_index)
            name = line[start_index:end_index].strip().strip('"')

        if '"currency_type":'  in line :
            currency_start_index = line.find('"currency_type":') + len('"currency_type":')
            currency_end_index = line.find(',', currency_start_index)
            if currency_end_index == -1:
                currency_end_index = line.find('}', currency_start_index)
            currency = line[currency_start_index:currency_end_index].strip().strip('"')

        if '"cost":'  in line :
            cost_start_index = line.find('"cost":') + len('"cost":')
            cost_end_index = line.find(',', cost_start_index)
            if cost_end_index == -1:
                cost_end_index = line.find('}', cost_start_index)
            cost = line[cost_start_index:cost_end_index].strip().strip('"')

        if '"item_count":'in line :
            item_count_start_index = line.find('"item_count":') + len('"item_count":')
            item_count_end_index = line.find(',', item_count_start_index)
            if item_count_end_index == -1:
                item_count_end_index = line.find('}', item_count_start_index)
            item_count = line[item_count_start_index:item_count_end_index].strip().strip('"')

        if '"event_name":'in line :
            event_start_index = line.find('"event_name":') + len('"event_name":')
            event_end_index = line.find(',', event_start_index)
            if event_end_index == -1:
                event_end_index = line.find('}', event_start_index)
            event_name = line[event_start_index:event_end_index].strip().strip('"')

            if not event_name:
               event_name = "未知1"
        
        if '"max_per_cycle":'in line :
            max_per_cycle_start_index = line.find('"max_per_cycle":') + len('max_per_cycle":')
            max_per_cycle_end_index = line.find(',', max_per_cycle_start_index)
            if max_per_cycle_end_index == -1:
                max_per_cycle_end_index = line.find('}', max_per_cycle_start_index)
            max_per_cycle = line[max_per_cycle_start_index:max_per_cycle_end_index].strip().strip('"')

        if '"shop_name":'in line :
            shop_start_index = line.find('"shop_name":') + len('"shop_name":')
            shop_end_index = line.find(',', shop_start_index)
            if shop_end_index == -1:
                shop_end_index = line.find('}', shop_start_index)
            shop_name = line[shop_start_index:shop_end_index].strip().strip('"')
        
        if '"reset_event":'in line :
            reset_event_start_index = line.find('"reset_event":') + len('"reset_event":')
            reset_event_end_index = line.find(',', reset_event_start_index)
            if reset_event_end_index == -1:
                reset_event_end_index = line.find('}', reset_event_start_index)
            reset_event = line[reset_event_start_index:reset_event_end_index].strip().strip('"')

        if name and currency and cost and item_count and event_name and max_per_cycle and shop_name and reset_event:
            currency_name = currency_mapping.get(currency, "未知")
            event_name = event_mapping.get(event_name, "未知")
            reset_event = reset_event_mapping.get(reset_event, "未知")
            shop_name = shop_name_mapping.get(shop_name, "未知")
            print(f"{event_name}在{shop_name}开放购买{item_count}个{name}{max_per_cycle}次，每次{currency_name}需{cost}个，刷新時間{reset_event}")
            with open('C:\\Users\\adam1\\Desktop\\Sky_data\\log\\國際服\\魔法商店數據.log','a', encoding='utf-8') as file1:
                file1.write(f"{event_name}在{shop_name}开放购买{item_count}个{name}{max_per_cycle}次，每次{currency_name}需{cost}个，刷新時間{reset_event}\n")
            name = None
            currency = None
            cost = None
            item_count = None
            event_name = None




with open('your file path','r', encoding='utf-8') as files:

    name = None
    tier = None
    id = None

    for line in files:
        
        if '"name":'in line :
            start_index = line.find('"name":') + len('"name":"commerce_item_')
            end_index = line.find(',', start_index)
            if end_index == -1:
                end_index = line.find('}', start_index)
            name = line[start_index:end_index].strip("_").strip('"')

        if '"tier":'  in line :
            tier_start_index = line.find('"tier":') + len('"tier":')
            tier_end_index = line.find(',', tier_start_index)
            if tier_end_index == -1:
                tier_end_index = line.find('}', tier_start_index)
            tier = line[tier_start_index:tier_end_index].strip().strip('"')

        if '"id":'in line :
            id_start_index = line.find('"id":') + len('"id":"')
            id_end_index = line.find(',', id_start_index)
            if id_end_index == -1:
                id_end_index = line.find('}', id_start_index)
            id = line[id_start_index:id_end_index].strip("_").strip('"')

        if name and tier and id:
            print(f"{id}{name}，需{tier}美元")

            name = None
            tier = None
            id = None