# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jatdb_server.models.base_model_ import Model
from jatdb_server import util


class EverdoItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id=None, sync_id=None, type=None, list=None, note=None, completed_on=None, parent_id=None, title=None, created_on=None, is_focused=None, energy=None, time=None, due_date=None, start_date=None, recurrent_task_id=None, contact_id=None, tags=None, position_child=None, position_parent=None, position_focus=None, position_global=None, repeated_on=None):  # noqa: E501
        """EverdoItem - a model defined in Swagger

        :param id: The id of this EverdoItem.  # noqa: E501
        :type id: str
        :param sync_id: The sync_id of this EverdoItem.  # noqa: E501
        :type sync_id: str
        :param type: The type of this EverdoItem.  # noqa: E501
        :type type: str
        :param list: The list of this EverdoItem.  # noqa: E501
        :type list: str
        :param note: The note of this EverdoItem.  # noqa: E501
        :type note: str
        :param completed_on: The completed_on of this EverdoItem.  # noqa: E501
        :type completed_on: int
        :param parent_id: The parent_id of this EverdoItem.  # noqa: E501
        :type parent_id: str
        :param title: The title of this EverdoItem.  # noqa: E501
        :type title: str
        :param created_on: The created_on of this EverdoItem.  # noqa: E501
        :type created_on: int
        :param is_focused: The is_focused of this EverdoItem.  # noqa: E501
        :type is_focused: int
        :param energy: The energy of this EverdoItem.  # noqa: E501
        :type energy: int
        :param time: The time of this EverdoItem.  # noqa: E501
        :type time: int
        :param due_date: The due_date of this EverdoItem.  # noqa: E501
        :type due_date: int
        :param start_date: The start_date of this EverdoItem.  # noqa: E501
        :type start_date: int
        :param recurrent_task_id: The recurrent_task_id of this EverdoItem.  # noqa: E501
        :type recurrent_task_id: int
        :param contact_id: The contact_id of this EverdoItem.  # noqa: E501
        :type contact_id: str
        :param tags: The tags of this EverdoItem.  # noqa: E501
        :type tags: List[int]
        :param position_child: The position_child of this EverdoItem.  # noqa: E501
        :type position_child: int
        :param position_parent: The position_parent of this EverdoItem.  # noqa: E501
        :type position_parent: int
        :param position_focus: The position_focus of this EverdoItem.  # noqa: E501
        :type position_focus: int
        :param position_global: The position_global of this EverdoItem.  # noqa: E501
        :type position_global: int
        :param repeated_on: The repeated_on of this EverdoItem.  # noqa: E501
        :type repeated_on: int
        """
        self.swagger_types = {
            'id': str,
            'sync_id': str,
            'type': str,
            'list': str,
            'note': str,
            'completed_on': int,
            'parent_id': str,
            'title': str,
            'created_on': int,
            'is_focused': int,
            'energy': int,
            'time': int,
            'due_date': int,
            'start_date': int,
            'recurrent_task_id': int,
            'contact_id': str,
            'tags': List[int],
            'position_child': int,
            'position_parent': int,
            'position_focus': int,
            'position_global': int,
            'repeated_on': int
        }

        self.attribute_map = {
            'id': 'id',
            'sync_id': 'sync_id',
            'type': 'type',
            'list': 'list',
            'note': 'note',
            'completed_on': 'completed_on',
            'parent_id': 'parent_id',
            'title': 'title',
            'created_on': 'created_on',
            'is_focused': 'is_focused',
            'energy': 'energy',
            'time': 'time',
            'due_date': 'due_date',
            'start_date': 'start_date',
            'recurrent_task_id': 'recurrent_task_id',
            'contact_id': 'contact_id',
            'tags': 'tags',
            'position_child': 'position_child',
            'position_parent': 'position_parent',
            'position_focus': 'position_focus',
            'position_global': 'position_global',
            'repeated_on': 'repeated_on'
        }

        self._id = id
        self._sync_id = sync_id
        self._type = type
        self._list = list
        self._note = note
        self._completed_on = completed_on
        self._parent_id = parent_id
        self._title = title
        self._created_on = created_on
        self._is_focused = is_focused
        self._energy = energy
        self._time = time
        self._due_date = due_date
        self._start_date = start_date
        self._recurrent_task_id = recurrent_task_id
        self._contact_id = contact_id
        self._tags = tags
        self._position_child = position_child
        self._position_parent = position_parent
        self._position_focus = position_focus
        self._position_global = position_global
        self._repeated_on = repeated_on

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EverdoItem of this EverdoItem.  # noqa: E501
        :rtype: EverdoItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this EverdoItem.

        TODO  # noqa: E501

        :return: The id of this EverdoItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EverdoItem.

        TODO  # noqa: E501

        :param id: The id of this EverdoItem.
        :type id: str
        """

        self._id = id

    @property
    def sync_id(self):
        """Gets the sync_id of this EverdoItem.

        TODO  # noqa: E501

        :return: The sync_id of this EverdoItem.
        :rtype: str
        """
        return self._sync_id

    @sync_id.setter
    def sync_id(self, sync_id):
        """Sets the sync_id of this EverdoItem.

        TODO  # noqa: E501

        :param sync_id: The sync_id of this EverdoItem.
        :type sync_id: str
        """

        self._sync_id = sync_id

    @property
    def type(self):
        """Gets the type of this EverdoItem.

        TODO  # noqa: E501

        :return: The type of this EverdoItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EverdoItem.

        TODO  # noqa: E501

        :param type: The type of this EverdoItem.
        :type type: str
        """

        self._type = type

    @property
    def list(self):
        """Gets the list of this EverdoItem.

        TODO  # noqa: E501

        :return: The list of this EverdoItem.
        :rtype: str
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this EverdoItem.

        TODO  # noqa: E501

        :param list: The list of this EverdoItem.
        :type list: str
        """

        self._list = list

    @property
    def note(self):
        """Gets the note of this EverdoItem.

        TODO  # noqa: E501

        :return: The note of this EverdoItem.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this EverdoItem.

        TODO  # noqa: E501

        :param note: The note of this EverdoItem.
        :type note: str
        """

        self._note = note

    @property
    def completed_on(self):
        """Gets the completed_on of this EverdoItem.

        TODO  # noqa: E501

        :return: The completed_on of this EverdoItem.
        :rtype: int
        """
        return self._completed_on

    @completed_on.setter
    def completed_on(self, completed_on):
        """Sets the completed_on of this EverdoItem.

        TODO  # noqa: E501

        :param completed_on: The completed_on of this EverdoItem.
        :type completed_on: int
        """

        self._completed_on = completed_on

    @property
    def parent_id(self):
        """Gets the parent_id of this EverdoItem.

        TODO  # noqa: E501

        :return: The parent_id of this EverdoItem.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this EverdoItem.

        TODO  # noqa: E501

        :param parent_id: The parent_id of this EverdoItem.
        :type parent_id: str
        """

        self._parent_id = parent_id

    @property
    def title(self):
        """Gets the title of this EverdoItem.

        TODO  # noqa: E501

        :return: The title of this EverdoItem.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this EverdoItem.

        TODO  # noqa: E501

        :param title: The title of this EverdoItem.
        :type title: str
        """

        self._title = title

    @property
    def created_on(self):
        """Gets the created_on of this EverdoItem.

        TODO  # noqa: E501

        :return: The created_on of this EverdoItem.
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this EverdoItem.

        TODO  # noqa: E501

        :param created_on: The created_on of this EverdoItem.
        :type created_on: int
        """

        self._created_on = created_on

    @property
    def is_focused(self):
        """Gets the is_focused of this EverdoItem.

        TODO  # noqa: E501

        :return: The is_focused of this EverdoItem.
        :rtype: int
        """
        return self._is_focused

    @is_focused.setter
    def is_focused(self, is_focused):
        """Sets the is_focused of this EverdoItem.

        TODO  # noqa: E501

        :param is_focused: The is_focused of this EverdoItem.
        :type is_focused: int
        """

        self._is_focused = is_focused

    @property
    def energy(self):
        """Gets the energy of this EverdoItem.

        TODO  # noqa: E501

        :return: The energy of this EverdoItem.
        :rtype: int
        """
        return self._energy

    @energy.setter
    def energy(self, energy):
        """Sets the energy of this EverdoItem.

        TODO  # noqa: E501

        :param energy: The energy of this EverdoItem.
        :type energy: int
        """

        self._energy = energy

    @property
    def time(self):
        """Gets the time of this EverdoItem.

        TODO  # noqa: E501

        :return: The time of this EverdoItem.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this EverdoItem.

        TODO  # noqa: E501

        :param time: The time of this EverdoItem.
        :type time: int
        """

        self._time = time

    @property
    def due_date(self):
        """Gets the due_date of this EverdoItem.

        TODO  # noqa: E501

        :return: The due_date of this EverdoItem.
        :rtype: int
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this EverdoItem.

        TODO  # noqa: E501

        :param due_date: The due_date of this EverdoItem.
        :type due_date: int
        """

        self._due_date = due_date

    @property
    def start_date(self):
        """Gets the start_date of this EverdoItem.

        TODO  # noqa: E501

        :return: The start_date of this EverdoItem.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this EverdoItem.

        TODO  # noqa: E501

        :param start_date: The start_date of this EverdoItem.
        :type start_date: int
        """

        self._start_date = start_date

    @property
    def recurrent_task_id(self):
        """Gets the recurrent_task_id of this EverdoItem.

        TODO  # noqa: E501

        :return: The recurrent_task_id of this EverdoItem.
        :rtype: int
        """
        return self._recurrent_task_id

    @recurrent_task_id.setter
    def recurrent_task_id(self, recurrent_task_id):
        """Sets the recurrent_task_id of this EverdoItem.

        TODO  # noqa: E501

        :param recurrent_task_id: The recurrent_task_id of this EverdoItem.
        :type recurrent_task_id: int
        """

        self._recurrent_task_id = recurrent_task_id

    @property
    def contact_id(self):
        """Gets the contact_id of this EverdoItem.

        TODO  # noqa: E501

        :return: The contact_id of this EverdoItem.
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this EverdoItem.

        TODO  # noqa: E501

        :param contact_id: The contact_id of this EverdoItem.
        :type contact_id: str
        """

        self._contact_id = contact_id

    @property
    def tags(self):
        """Gets the tags of this EverdoItem.

        TODO  # noqa: E501

        :return: The tags of this EverdoItem.
        :rtype: List[int]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EverdoItem.

        TODO  # noqa: E501

        :param tags: The tags of this EverdoItem.
        :type tags: List[int]
        """

        self._tags = tags

    @property
    def position_child(self):
        """Gets the position_child of this EverdoItem.

        TODO  # noqa: E501

        :return: The position_child of this EverdoItem.
        :rtype: int
        """
        return self._position_child

    @position_child.setter
    def position_child(self, position_child):
        """Sets the position_child of this EverdoItem.

        TODO  # noqa: E501

        :param position_child: The position_child of this EverdoItem.
        :type position_child: int
        """

        self._position_child = position_child

    @property
    def position_parent(self):
        """Gets the position_parent of this EverdoItem.

        TODO  # noqa: E501

        :return: The position_parent of this EverdoItem.
        :rtype: int
        """
        return self._position_parent

    @position_parent.setter
    def position_parent(self, position_parent):
        """Sets the position_parent of this EverdoItem.

        TODO  # noqa: E501

        :param position_parent: The position_parent of this EverdoItem.
        :type position_parent: int
        """

        self._position_parent = position_parent

    @property
    def position_focus(self):
        """Gets the position_focus of this EverdoItem.

        TODO  # noqa: E501

        :return: The position_focus of this EverdoItem.
        :rtype: int
        """
        return self._position_focus

    @position_focus.setter
    def position_focus(self, position_focus):
        """Sets the position_focus of this EverdoItem.

        TODO  # noqa: E501

        :param position_focus: The position_focus of this EverdoItem.
        :type position_focus: int
        """

        self._position_focus = position_focus

    @property
    def position_global(self):
        """Gets the position_global of this EverdoItem.

        TODO  # noqa: E501

        :return: The position_global of this EverdoItem.
        :rtype: int
        """
        return self._position_global

    @position_global.setter
    def position_global(self, position_global):
        """Sets the position_global of this EverdoItem.

        TODO  # noqa: E501

        :param position_global: The position_global of this EverdoItem.
        :type position_global: int
        """

        self._position_global = position_global

    @property
    def repeated_on(self):
        """Gets the repeated_on of this EverdoItem.

        TODO  # noqa: E501

        :return: The repeated_on of this EverdoItem.
        :rtype: int
        """
        return self._repeated_on

    @repeated_on.setter
    def repeated_on(self, repeated_on):
        """Sets the repeated_on of this EverdoItem.

        TODO  # noqa: E501

        :param repeated_on: The repeated_on of this EverdoItem.
        :type repeated_on: int
        """

        self._repeated_on = repeated_on
