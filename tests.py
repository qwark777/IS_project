from typing import Union, Any, Coroutine


async def get_file(i: int) -> Union[tuple[Any, Any]]:
    """Получает тесты и ответы по номеру i"""
    try:
        test = globals()['test' + str(i)]
        answer = globals()['answer' + str(i)]
    except KeyError:
        return False, False
    return test, answer


test1 = {
    "id": 1,
    "replies": [
        {
            "id": 2,
            "replies": []
        },
        {
            "id": 3,
            "replies": [
                {
                    "id": 4,
                    "replies": []
                },
                {
                    "id": 5,
                    "replies": []
                }
            ]
        }
    ]
}

answer1 = {
    "id": 1,
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    "replies": [
        {
            "id": 2,
            "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla",
            "replies": []
        },
        {
            "id": 3,
            "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut",
            "replies": [
                {
                    "id": 4,
                    "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit",
                    "replies": []
                },
                {
                    "id": 5,
                    "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque",
                    "replies": []
                }
            ]
        }
    ]
}

test2 = {
    "id": 11,
    "body": "body text for comment 11",
    "author": "author11",
    "replies": [
        {
            "id": 12,
            "body": "body text for comment 12",
            "author": "author12",
            "replies": []
        },
        {
            "id": 13,
            "body": "body text for comment 13",
            "author": "author13",
            "replies": []
        },
        {
            "id": 14,
            "body": "body text for comment 14",
            "author": "author14",
            "replies": []
        },
        {
            "id": 15,
            "body": "body text for comment 15",
            "author": "author15",
            "replies": []
        },
        {
            "id": 16,
            "body": "body text for comment 16",
            "author": "author16",
            "replies": []
        }
    ]
}

answer2 = {
    "id": 11,
    "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus\naccusamus in eum beatae sit\nvel qui neque voluptates ut commodi qui incidunt\nut animi commodi",
    "replies": [
        {
            "id": 12,
            "body": "itaque id aut magnam\npraesentium quia et ea odit et ea voluptas et\nsapiente quia nihil amet occaecati quia id voluptatem\nincidunt ea est distinctio odio",
            "replies": []
        },
        {
            "id": 13,
            "body": "aut dicta possimus sint mollitia voluptas commodi quo doloremque\niste corrupti reiciendis voluptatem eius rerum\nsit cumque quod eligendi laborum minima\nperferendis recusandae assumenda consectetur porro architecto ipsum ipsam",
            "replies": []
        },
        {
            "id": 14,
            "body": "fuga et accusamus dolorum perferendis illo voluptas\nnon doloremque neque facere\nad qui dolorum molestiae beatae\nsed aut voluptas totam sit illum",
            "replies": []
        },
        {
            "id": 15,
            "body": "reprehenderit quos placeat\nvelit minima officia dolores impedit repudiandae molestiae nam\nvoluptas recusandae quis delectus\nofficiis harum fugiat vitae",
            "replies": []
        },
        {
            "id": 16,
            "body": "suscipit nam nisi quo aperiam aut\nasperiores eos fugit maiores voluptatibus quia\nvoluptatem quis ullam qui in alias quia est\nconsequatur magni mollitia accusamus ea nisi voluptate dicta",
            "replies": []
        }
    ]
}

test3 = {
    "id": 7,
    "replies": [
        {
            "id": 8,
            "replies": [
                {
                    "id": 9,
                    "replies": [
                        {
                            "id": 10,
                            "replies": []
                        }
                    ]
                }
            ]
        }
    ]
}

answer3 = {
    "id": 7,
    "body": "dolore placeat quibusdam ea quo vitae\nmagni quis enim qui quis quo nemo aut saepe\nquidem repellat excepturi ut quia\nsunt ut sequi eos ea sed quas",
    "replies": [
        {
            "id": 8,
            "body": "dignissimos aperiam dolorem qui eum\nfacilis quibusdam animi sint suscipit qui sint possimus cum\nquaerat magni maiores excepturi\nipsam ut commodi dolor voluptatum modi aut vitae",
            "replies": [
                {
                    "id": 9,
                    "body": "consectetur animi nesciunt iure dolore\nenim quia ad\nveniam autem ut quam aut nobis\net est aut quod aut provident voluptas autem voluptas",
                    "replies": [
                        {
                            "id": 10,
                            "body": "quo et expedita modi cum officia vel magni\ndoloribus qui repudiandae\nvero nisi sit\nquos veniam quod sed accusamus veritatis error",
                            "replies": []
                        }
                    ]
                }
            ]
        }
    ]
}

test4 = {
    "id": 11,
    "replies": [
        {"id": 12, "replies": []},
        {"id": 13, "replies": []},
        {"id": 14, "replies": []},
        {"id": 15, "replies": []},
        {"id": 16, "replies": []}
    ]
}

answer4 = {
    "id": 11,
    "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus\naccusamus in eum beatae sit\nvel qui neque voluptates ut commodi qui incidunt\nut animi commodi",
    "replies": [
        {
            "id": 12,
            "body": "itaque id aut magnam\npraesentium quia et ea odit et ea voluptas et\nsapiente quia nihil amet occaecati quia id voluptatem\nincidunt ea est distinctio odio",
            "replies": []
        },
        {
            "id": 13,
            "body": "aut dicta possimus sint mollitia voluptas commodi quo doloremque\niste corrupti reiciendis voluptatem eius rerum\nsit cumque quod eligendi laborum minima\nperferendis recusandae assumenda consectetur porro architecto ipsum ipsam",
            "replies": []
        },
        {
            "id": 14,
            "body": "fuga et accusamus dolorum perferendis illo voluptas\nnon doloremque neque facere\nad qui dolorum molestiae beatae\nsed aut voluptas totam sit illum",
            "replies": []
        },
        {
            "id": 15,
            "body": "reprehenderit quos placeat\nvelit minima officia dolores impedit repudiandae molestiae nam\nvoluptas recusandae quis delectus\nofficiis harum fugiat vitae",
            "replies": []
        },
        {
            "id": 16,
            "body": "suscipit nam nisi quo aperiam aut\nasperiores eos fugit maiores voluptatibus quia\nvoluptatem quis ullam qui in alias quia est\nconsequatur magni mollitia accusamus ea nisi voluptate dicta",
            "replies": []
        }
    ]
}

