
import os
from jatdb.trello.db import dump

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
            dump(j,f)

    def add_list(self, j):
        p = self.make_row('lists', j['id'])
        with open(os.path.join(p,'list.json'),'w') as f:
            dump(j,f)
        # os.symlink(
        #     os.path.join(os.pardir,os.pardir,'boards',j['idBoard']),
        #     os.path.join(p, 'board'),
        #     target_is_directory=True
        #     )

    def add_card(self, j):
        p = self.make_row('cards', j['id'])
        with open(os.path.join(p,'card.json'),'w') as f:
            dump(j,f)

def main(args=None):
    d = DataDir('_data')
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv[1:]))
