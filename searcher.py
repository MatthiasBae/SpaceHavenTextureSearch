import xml.etree.ElementTree as ET

filepath = r'animations.xml'

def get_animation_ids_from_sprite_id(sprite_id:int) -> list:
    tree = ET.parse(filepath)
    root = tree.getroot()
    animations_root = root[0]

    animation_ids = []
    for animation_tree in animations_root.iter('ba'):
        items = animation_tree.find('items')
        for item in items.iter('assetPos'):
            id_exists = 'a' in item.attrib
            if not id_exists:
                continue
            item_id = item.attrib['a']
            if int(item_id) == sprite_id:
                animation_ids.append(animation_tree.attrib['id'])
    return animation_ids

def get_animation_names_from_sprite_id(sprite_id:int) -> list:
    tree = ET.parse(filepath)
    root = tree.getroot()
    animations_root = root[0]

    animation_names = []
    for animation_tree in animations_root.iter('ba'):
        items = animation_tree.find('items')
        for item in items.iter('assetPos'):
            id_exists = 'a' in item.attrib
            if not id_exists:
                continue
            item_id = item.attrib['a']
            if int(item_id) == sprite_id:
                animation_names.append(animation_tree.attrib['n'])
    return animation_names

def get_sprite_ids_from_animation_id(animation_id:int) -> list:
    tree = ET.parse(filepath)
    root = tree.getroot()
    animations_root = root[0]

    sprite_ids = []
    for animation_tree in animations_root.iter('ba'):
        if int(animation_tree.attrib['id']) == animation_id:
            items = animation_tree.find('items')
            for item in items.iter('assetPos'):
                id_exists = 'a' in item.attrib
                if not id_exists:
                    continue
                item_id = item.attrib['a']
                sprite_ids.append(item_id)
    return sprite_ids

def get_sprite_ids_from_animation_name(animation_name:str) -> list:
    tree = ET.parse(filepath)
    root = tree.getroot()
    animations_root = root[0]

    sprite_ids = []
    for animation_tree in animations_root.iter('ba'):
        if animation_tree.attrib['n'] == animation_name:
            items = animation_tree.find('items')
            for item in items.iter('assetPos'):
                id_exists = 'a' in item.attrib
                if not id_exists:
                    continue
                item_id = item.attrib['a']
                sprite_ids.append(item_id)
    return sprite_ids

def get_all_animations_by_namepart(start_part:str, end_part:str) -> list:
    tree = ET.parse(filepath)
    root = tree.getroot()
    animations_root = root[0]

    animation_names = []
    for animation_tree in animations_root.iter('ba'):
        name = animation_tree.attrib['n']
        if name.startswith(start_part) and name.endswith(end_part):
            animation_names.append(animation_tree.attrib['n'])
    return animation_names

print(get_all_animations_by_namepart('m','1Idle2'))