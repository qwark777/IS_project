import asyncio
from copy import deepcopy
import aiohttp
from main import collect_comment_ids, fetch_comment, enrich_tree
from tests import get_file


async def function_for_testing(i:int) -> bool:
    """Проверяет корректность работы алгоритма на тестах"""
    test, answer = await get_file(i)
    if not (test and answer):
        return False
    input_data = deepcopy(test)
    comment_ids = set()
    collect_comment_ids(input_data, comment_ids)
    comments_data = dict()
    async with aiohttp.ClientSession() as session:
        for cid in comment_ids:
            comments_data[cid] = await fetch_comment(session, cid)

    enriched_data = enrich_tree(input_data, comments_data)

    if enriched_data == answer:
        print('Функция работает корректно ✅')
    else:
        print('Функция работает некорректно ❌')
    return True

async def run_function() -> None:
    """Запускает тестовую функцию"""
    i = 1
    while await function_for_testing(i):
        i+=1




asyncio.run(run_function())


