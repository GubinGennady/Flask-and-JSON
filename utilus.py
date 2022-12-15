import json


def load_candidates():
    '''
    Загружает данные из JSON файла.
    :return: Возвращает данные.
    '''
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)
    

def get_all():
    '''
    Возвращает данные на всех кандидатов.
    '''
    return load_candidates()

def get_candidate_by_pk(pk):
    '''
    Возвращает кандидата по его ID = pk
    :param pk: Номер кандидата.
    :return: Возращает кандидата.
    '''
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate


def get_candidate_by_skill(skill):
    '''
    Функция выполняет поиск по кандидатам и по навыкам и умениям.
    :param skill: Поиск навыков и умений кандидата.
    :return Возвращает подходящего кандидата.
    '''
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates
