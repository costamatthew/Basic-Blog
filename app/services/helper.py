def verify_recieved_key(data: dict):
    required_keys = ["title", "date", "contents", "author", "email"]
    keys = data.keys()

    return [key for key in required_keys if key not in keys]




def check_data(data: dict):
    if verify_recieved_key(data):
        raise KeyError(
            {
                "error": {
                    "required_keys": ["title", "date", "contents", "author", "email"],
                }
            },
        )

    return data
