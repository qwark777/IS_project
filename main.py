import os
import sys
import json
import asyncio
import aiohttp
from typing import Dict, List, Union, Set
from dotenv import load_dotenv, find_dotenv


class PEBKAC(Exception):
    pass


async def fetch_comment(session: aiohttp.ClientSession, comment_id: int) -> Dict[str, str]:
    """Асинхронно получает данные комментария методом get через URL"""
    load_dotenv(find_dotenv())
    url = os.getenv('PAGE_PATH') + str(comment_id)
    try:
        async with session.get(url) as response:
            if str(response.status) == '200':
                return json.loads(str(await response.text()))
            elif str(response.status) == '404':
                return {"id": str(comment_id), "body": "[comment not found]"}
    except Exception as e:
        print(e)
    return {"id":  str(comment_id), "body": f"[error]"}


def collect_comment_ids(tree: Union[Dict, List], ids: Set[int]) -> None:
    """Рекурсивно собирает все ID комментариев из дерева"""
    if isinstance(tree, list):  # если в replies
        for item in tree:
            collect_comment_ids(item, ids)
    elif isinstance(tree, dict):
        if "id" in tree:
            ids.add(tree["id"])
        for value in tree.values():
            collect_comment_ids(value, ids)


def enrich_tree(tree: Union[Dict, List], comments_data: Dict[int, Dict[str, str]]) -> Union[Dict, List]:
    """Вставляет данные в дерево"""
    if isinstance(tree, list):  # если в replies
        return [enrich_tree(item, comments_data) for item in tree]
    elif isinstance(tree, dict):
        if "id" in tree:
            comment_id = int(tree["id"])
            if comment_id in comments_data.keys():
                return {'id': comment_id, "body": comments_data[comment_id]['body'],
                        "replies": enrich_tree(tree['replies'], comments_data)}
            return {'id': comment_id, "body": 'missing data',
                    "replies": enrich_tree(tree['replies'], comments_data)}
        else:
            raise PEBKAC
    return tree


async def main():
    input_data = json.load(sys.stdin)
    comment_ids = set()
    collect_comment_ids(input_data, comment_ids)
    comments_data = dict()
    async with aiohttp.ClientSession() as session:
        for cid in comment_ids:
            comments_data[cid] = await fetch_comment(session, cid)


    enriched_data = enrich_tree(input_data, comments_data)

    json.dump(enriched_data, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    asyncio.run(main())
