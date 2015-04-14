coll_schema = {
        "type": "object",

        "properties": {
            "type_id": {
                "type": "integer"
            },
            "title": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "address": {
                "type": "string"
            },
            "btc": {
                "type": "string"
            },
            "keywords": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "name": {
                            "type": "string"
                        }
                    },
                    "required": ["id", "name"]
                }
            },
            "documents": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "address": {
                            "type": "string"
                        },
                        "hash": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "filename": {
                            "type": "string"
                        },
                        "accesses": {
                            "type": "integer"
                        }
                    },
                    "required": ["address", "hash", "title", "description", "filename", "accesses"]

                }
            },
            "latest_broadcast_date": {
                "type": "string"
            },
            "creation_date": {
                "type": "string"
            },
            "oldest_date": {
                "type": "string"
            },
            "latest_btc_tx": {
                "type": "string"
            },
            "oldest_btc_tx": {
                "type": "string"
            },
            "accesses": {
                "type": "integer"
            },
            "votes": {
                "type": "integer"
            },
            "votes_last_checked": {
                "type": "string"
            }
        },
        "required": ["type_id", "title", "description", "documents", "keywords", "address", "btc",
                     "creation_date", "oldest_date", "latest_btc_tx", "oldest_btc_tx",
                     "latest_broadcast_date", "accesses", "votes", "votes_last_checked"]

}

fj_schema = {
    "type": "object",
    "properties": {
        "protocol": {
            "type": "string"
        },
        "type_id": {
            "type": "integer"
        },
        "original_sender": {
            "type": "string"
        },
        "signature": {
            "type": "string"
        },
        "time_created": {
            "type": "string"
        },
        "pubkey": {
            "type": "string"
        },
    },
    "required": ["protocol", "type_id", "original_sender", "signature", "time_created", "pubkey"]
}