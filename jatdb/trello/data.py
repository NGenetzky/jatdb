
import os

class DataDir():

    def __init__(self, root):
        self.root = root
        if not os.path.exists(self.root):
            raise Exception()

        os.makedirs(os.path.join(self.root,'boards'), exist_ok=True)
        os.makedirs(os.path.join(self.root,'lists'), exist_ok=True)
        os.makedirs(os.path.join(self.root,'cards'), exist_ok=True)

    def db_path(self):
        return os.path.join(self.root,'trello.json')

    def row_path(self, table, id_):
        return os.path.join(self.root,table,id_)

    def make_row(self, table, id_):
        p = self.row_path(table,id_)
        if not os.path.exists(p):
            return os.mkdir(p)

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

def main(args=None):
    d = DataDir('_data')
    row_id = '5a4ec5841e3fdbb6adb79c0f'
    print(d.row_path('boards', row_id))

    d.make_row('boards', row_id)
    d.make_row('cards', '9a4ec5841e3fdbb6adb79c0f')

    d.link_alias('boards', row_id, 'GTD')

    # d.link_ref('boards', row_id, 'cards')

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv[1:]))
