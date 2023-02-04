"https://www.mongodb.com/docs/manual/reference/operator/query/jsonSchema/"

"""
required - обязательные ключи
properties - ключи уровня
"""

get_single_user_positive = {
    "required": ["data", "support"],
    "type": "object",

    "properties":{"data":{
                    "required": ["id", "email", "first_name", "last_name", "avatar"],
                    "properties":{
                        "id":{"type": "number"},
                        "email":{"type": "string"},
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                        "avatar": {"type": "string"}},
                    },
                    
                "support":{
                    "required": ["url", "text"],
                    "properties":{
                        "url": {"type": "string"},
                        "text": {"type": "string"}},
                    }}}

get_single_user_negative = {
    "type": "object",
    "maxProperties": 0
}

get_list_users_positive = {
    "type": "object",
    "required": ["page", "per_page", "total", "total_pages", "data", "support"],
    "properties":{
        "page": {"type": "number"},
        "per_page": {"type": "number"},
        "total": {"type": "number"},
        "total_pages": {"type": "number"},
        "data": {"type": "array", "minItems": 0, "maxItems": 6},
        "support": {"type": "object"}
    }
}

get_list_users_negative = {
    "type": "object",
    "required": ["page", "per_page", "total", "total_pages", "data", "support"],
    "properties":{
        "page": {"type": "number"},
        "per_page": {"type": "number"},
        "total": {"type": "number"},
        "total_pages": {"type": "number"},
        "data": {"type": "array", "maxItems": 0},
        "support": {"type": "object"}
    }
}

register_positive = {
    "type": "object",
    "maxProperties": 2,
    "minProperties": 2,
    "required": ["id", "token"],
    "properties":{
        "id": {"type": "number"},
        "token": {"type": "string"}
    }
}

register_negative = {
    "type": "object",
    "maxProperties": 1,
    "minProperties": 1,
    "required": ["error"],
    "properties": {
        "error": {"type": "string"}
    }
}