def data_processing(data: dict):
    data["email"] = data["email"].lower()
    data.name = data.name.title()

    return data