
def board_to_json(b):
    d = {}
    d['id'] = b.id
    d['name'] = b.name
    d['url'] = b.url
    # d['dateLastActivity'] = b.date_last_activity # TODO
    d['desc'] = b.description
    return d

