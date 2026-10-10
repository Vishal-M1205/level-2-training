def generate_query(params: dict, seperator: str) -> list:
    fields = list(params.keys())

    query = f"{seperator}".join([f"{x} = %s" for x in fields])
    return query
