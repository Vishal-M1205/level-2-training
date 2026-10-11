class QueryUtil:

    def generate_query(self, params: dict, seperator: str) -> list:
        fields = list(params.keys())

        query = f"{seperator}".join([f"{x} = %s" for x in fields])
        return query
