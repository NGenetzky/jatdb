""" CLI for Joplin subpackage
"""

import argparse
import logging
import os
import sys
import copy

# This is currently a special frontmatter package that has 'joplin-support'
import frontmatter

logging.basicConfig(filename='jatdb.log', level=logging.INFO)
log = logging.getLogger(__name__)


def frontmatter_load(filename):
    with open(filename) as fd:
        return frontmatter.load(fd=fd)


def frontmatter_dump(post, filename):
    post.handler = frontmatter.YAMLHandler()
    with open(filename, 'w') as fd:
        return frontmatter.dump(post, fd)


class JoplinDb(object):

    TYPES = {
        1: 'note',
        2: 'notebook',
        4: 'resource',
        5: 'tag',
        6: 'notetag',
    }

    def __init__(self, root):
        if not os.path.isdir(os.path.join(root, '.resource')):
            raise ValueError("Directory({0}) does not appear to be sync dir")
        self.root = root
        self._data = {}
        for t in self.TYPES:
            self._data[self.TYPES[t]] = {}
        self._data['tag_of_note'] = {}

    def index(self):
        for root, dirs, files in os.walk(self.root):
            if root == os.path.join(self.root, '.resource'):
                continue
            for f in files:
                fullpath = os.path.join(root, f)
                try:
                    post = frontmatter_load(fullpath)
                except UnicodeDecodeError:
                    log.error('frontmatter_load({})'.format(fullpath))
                    continue
                typename = self.TYPES[post['type_']]
                self._data[typename][post['id']] = post.metadata
                log.debug('JoplinDb._data[{0}][{1}]'.format(
                    typename, post['id']))

        for note in self.notes:
            self._data['tag_of_note'][note] = set()
        for notetag in self.notetags:
            noteid = self._data['notetag'][notetag]['note_id']
            tagid = self._data['notetag'][notetag]['tag_id']
            self._data['tag_of_note'][noteid].add(tagid)

    def get_content(self, type_, id_):
        filepath = os.path.join(self.root, id_ + ".md")
        if not os.path.isfile(filepath):
            raise ValueError('_data[{0}][{1}]'.format(type_, id_))
        post = frontmatter_load(filepath)
        return post

    @property
    def notes(self):
        return self._data['note']

    @property
    def notetags(self):
        return self._data['notetag']

    def post_note(self, id_, outdir):
        post = self.get_content('note', id_)
        joplin_note = post.metadata

        short_name = '{0}-{1}'.format(
            joplin_note['created_time'].date().isoformat(), joplin_note["id"])
        # parentdir = os.path.join(outdir, 'post', post['parent_id'])
        notedir = os.path.join(outdir, 'post', 'joplin_note', short_name)

        if not os.path.isdir(notedir):
            os.makedirs(notedir)

        lines = post.content.splitlines()
        title = lines[0].encode('utf-8')
        log.info('{0}/index.md: {1}'.format(notedir, title))

        parent = self.get_content('notebook', post['parent_id'])
        parentname = parent.content.splitlines()[0].encode('utf-8')

        tags = set()
        for tag in self._data['tag_of_note'][id_]:
            tagpost = self.get_content('tag', tag)
            tagname = tagpost.content.splitlines()[0].encode('utf-8')
            tags.add(tagname)

        post.metadata = {
            "title": title,
            "date": copy.copy(joplin_note['created_time']),
            # "categories": [post['parent_id']],
            "categories": [parentname],
            "tags": list(tags),
            "__joplin_note__": joplin_note,
        }

        frontmatter_dump(post, os.path.join(notedir, 'index.md'))


def parse_args(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sync', type=str, help='Joplin sync directory')
    parser.add_argument('--out', type=str, help='Output directory')
    return parser.parse_args()


def main(argv=None):
    args = parse_args(argv)

    if (args.sync is not None and args.out is not None):
        db = JoplinDb(args.sync)
        db.index()
        for note in db.notes:
            db.post_note(note, args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
