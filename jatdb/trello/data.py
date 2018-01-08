
import os
import json

def json_dump(obj, fp):
    '''Helper function for json.dump to make result diffable and readable.'''
    return json.dump(obj, fp, sort_keys=True, indent='\t')

class Data():

    def __init__(self, root):
        self.root = root
        if not os.path.exists(self.root):
            raise Exception()

        # os.makedirs(os.path.join(self.root,'boards'), exist_ok=True)
        # os.makedirs(os.path.join(self.root,'lists'), exist_ok=True)
        # os.makedirs(os.path.join(self.root,'cards'), exist_ok=True)

    def db_path(self):
        return os.path.join(self.root,'trello.json')

    def row_path(self, table, id_):
        return os.path.join(self.root,table,id_)

    def make_row(self, table, id_):
        p = self.row_path(table,id_)
        if not os.path.exists(p):
            os.makedirs(p)
        return p

    def link_alias(self, table, id_, alias):
        os.symlink(
                id_,
                self.row_path(table,alias),
                target_is_directory=True
                )

    # TODO: This needs to be designed better before I implement it.
    # def link_ref(self, table, id_, target_table, target_id):
    #     os.symlink(
    #             os.path.join(os.pardir,os.pardir,target_table,target_id),
    #             self.row_path(table,id_),
    #             target_is_directory=True
    #             )

    def add_board(self, j):
        p = self.make_row('boards', j['id'])
        with open(os.path.join(p,'board.json'),'w') as f:
            json_dump(j,f)

    def add_list(self, j):
        p = self.make_row('lists', j['id'])
        with open(os.path.join(p,'list.json'),'w') as f:
            json_dump(j,f)

        board_link = os.path.join(p, 'board')
        if os.path.exists(board_link):
            os.remove(board_link)
        os.symlink(
            os.path.join(os.pardir,os.pardir,'boards',j['idBoard']),
            board_link,
            target_is_directory=True
            )

    def add_card(self, j):
        p = self.make_row('cards', j['id'])
        with open(os.path.join(p,'card.json'),'w') as f:
            json_dump(j,f)

        board_link = os.path.join(p, 'board')
        if os.path.exists(board_link):
            os.remove(board_link)
        os.symlink(
            os.path.join(os.pardir,os.pardir,'boards',j['idBoard']),
            board_link,
            target_is_directory=True
            )

        list_link = os.path.join(p, 'list')
        if os.path.exists(list_link):
            os.remove(list_link)
        os.symlink(
            os.path.join(os.pardir,os.pardir,'lists',j['idList']),
            list_link,
            target_is_directory=True
            )

    def add_db(self, j, id_):
        p = self.make_row('dbs', id_)
        with open(os.path.join(p,'db.json'),'w') as f:
            json_dump(j,f)

def main(args=None):
    # TODO: Use a real argparser.
    root = args[0]
    d = Data(root)

    json_db = args[1]
    if not os.path.exists(json_db):
        raise Exception()

    if 2 < len(args):
        db_id = args[2]
    else:
        db_id = '0'

    j = {}
    with open(json_db, 'r') as f:
        j = json.load(f)
    d.add_db(j, db_id)

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv[1:]))
