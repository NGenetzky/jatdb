# coding: utf-8

"""
    jatdb

    JSON API to DB: Fetch JSON from APIs and send to a TinyDB database.  # noqa: E501

    OpenAPI spec version: 0.0.2
    Contact: Nathan@Genetzky.us
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EverdoItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'sync_id': 'str',
        'type': 'str',
        'list': 'str',
        'note': 'str',
        'completed_on': 'int',
        'parent_id': 'str',
        'title': 'str',
        'created_on': 'int',
        'is_focused': 'int',
        'energy': 'int',
        'time': 'int',
        'due_date': 'int',
        'start_date': 'int',
        'recurrent_task_id': 'int',
        'contact_id': 'str',
        'tags': 'list[int]',
        'position_child': 'int',
        'position_parent': 'int',
        'position_focus': 'int',
        'position_global': 'int',
        'repeated_on': 'int'
    }

    attribute_map = {
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

    def __init__(self, id=None, sync_id=None, type=None, list=None, note=None, completed_on=None, parent_id=None, title=None, created_on=None, is_focused=None, energy=None, time=None, due_date=None, start_date=None, recurrent_task_id=None, contact_id=None, tags=None, position_child=None, position_parent=None, position_focus=None, position_global=None, repeated_on=None):  # noqa: E501
        """EverdoItem - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._sync_id = None
        self._type = None
        self._list = None
        self._note = None
        self._completed_on = None
        self._parent_id = None
        self._title = None
        self._created_on = None
        self._is_focused = None
        self._energy = None
        self._time = None
        self._due_date = None
        self._start_date = None
        self._recurrent_task_id = None
        self._contact_id = None
        self._tags = None
        self._position_child = None
        self._position_parent = None
        self._position_focus = None
        self._position_global = None
        self._repeated_on = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sync_id is not None:
            self.sync_id = sync_id
        if type is not None:
            self.type = type
        if list is not None:
            self.list = list
        if note is not None:
            self.note = note
        if completed_on is not None:
            self.completed_on = completed_on
        if parent_id is not None:
            self.parent_id = parent_id
        if title is not None:
            self.title = title
        if created_on is not None:
            self.created_on = created_on
        if is_focused is not None:
            self.is_focused = is_focused
        if energy is not None:
            self.energy = energy
        if time is not None:
            self.time = time
        if due_date is not None:
            self.due_date = due_date
        if start_date is not None:
            self.start_date = start_date
        if recurrent_task_id is not None:
            self.recurrent_task_id = recurrent_task_id
        if contact_id is not None:
            self.contact_id = contact_id
        if tags is not None:
            self.tags = tags
        if position_child is not None:
            self.position_child = position_child
        if position_parent is not None:
            self.position_parent = position_parent
        if position_focus is not None:
            self.position_focus = position_focus
        if position_global is not None:
            self.position_global = position_global
        if repeated_on is not None:
            self.repeated_on = repeated_on

    @property
    def id(self):
        """Gets the id of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The id of this EverdoItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EverdoItem.

        TODO  # noqa: E501

        :param id: The id of this EverdoItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sync_id(self):
        """Gets the sync_id of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The sync_id of this EverdoItem.  # noqa: E501
        :rtype: str
        """
        return self._sync_id

    @sync_id.setter
    def sync_id(self, sync_id):
        """Sets the sync_id of this EverdoItem.

        TODO  # noqa: E501

        :param sync_id: The sync_id of this EverdoItem.  # noqa: E501
        :type: str
        """

        self._sync_id = sync_id

    @property
    def type(self):
        """Gets the type of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The type of this EverdoItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EverdoItem.

        TODO  # noqa: E501

        :param type: The type of this EverdoItem.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def list(self):
        """Gets the list of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The list of this EverdoItem.  # noqa: E501
        :rtype: str
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this EverdoItem.

        TODO  # noqa: E501

        :param list: The list of this EverdoItem.  # noqa: E501
        :type: str
        """

        self._list = list

    @property
    def note(self):
        """Gets the note of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The note of this EverdoItem.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this EverdoItem.

        TODO  # noqa: E501

        :param note: The note of this EverdoItem.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def completed_on(self):
        """Gets the completed_on of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The completed_on of this EverdoItem.  # noqa: E501
        :rtype: int
        """
        return self._completed_on

    @completed_on.setter
    def completed_on(self, completed_on):
        """Sets the completed_on of this EverdoItem.

        TODO  # noqa: E501

        :param completed_on: The completed_on of this EverdoItem.  # noqa: E501
        :type: int
        """

        self._completed_on = completed_on

    @property
    def parent_id(self):
        """Gets the parent_id of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The parent_id of this EverdoItem.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this EverdoItem.

        TODO  # noqa: E501

        :param parent_id: The parent_id of this EverdoItem.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def title(self):
        """Gets the title of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The title of this EverdoItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this EverdoItem.

        TODO  # noqa: E501

        :param title: The title of this EverdoItem.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def created_on(self):
        """Gets the created_on of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The created_on of this EverdoItem.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this EverdoItem.

        TODO  # noqa: E501

        :param created_on: The created_on of this EverdoItem.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def is_focused(self):
        """Gets the is_focused of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The is_focused of this EverdoItem.  # noqa: E501
        :rtype: int
        """
        return self._is_focused

    @is_focused.setter
    def is_focused(self, is_focused):
        """Sets the is_focused of this EverdoItem.

        TODO  # noqa: E501

        :param is_focused: The is_focused of this EverdoItem.  # noqa: E501
        :type: int
        """

        self._is_focused = is_focused

    @property
    def energy(self):
        """Gets the energy of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The energy of this EverdoItem.  # noqa: E501
        :rtype: int
        """
        return self._energy

    @energy.setter
    def energy(self, energy):
        """Sets the energy of this EverdoItem.

        TODO  # noqa: E501

        :param energy: The energy of this EverdoItem.  # noqa: E501
        :type: int
        """

        self._energy = energy

    @property
    def time(self):
        """Gets the time of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The time of this EverdoItem.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this EverdoItem.

        TODO  # noqa: E501

        :param time: The time of this EverdoItem.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def due_date(self):
        """Gets the due_date of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The due_date of this EverdoItem.  # noqa: E501
        :rtype: int
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this EverdoItem.

        TODO  # noqa: E501

        :param due_date: The due_date of this EverdoItem.  # noqa: E501
        :type: int
        """

        self._due_date = due_date

    @property
    def start_date(self):
        """Gets the start_date of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The start_date of this EverdoItem.  # noqa: E501
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this EverdoItem.

        TODO  # noqa: E501

        :param start_date: The start_date of this EverdoItem.  # noqa: E501
        :type: int
        """

        self._start_date = start_date

    @property
    def recurrent_task_id(self):
        """Gets the recurrent_task_id of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The recurrent_task_id of this EverdoItem.  # noqa: E501
        :rtype: int
        """
        return self._recurrent_task_id

    @recurrent_task_id.setter
    def recurrent_task_id(self, recurrent_task_id):
        """Sets the recurrent_task_id of this EverdoItem.

        TODO  # noqa: E501

        :param recurrent_task_id: The recurrent_task_id of this EverdoItem.  # noqa: E501
        :type: int
        """

        self._recurrent_task_id = recurrent_task_id

    @property
    def contact_id(self):
        """Gets the contact_id of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The contact_id of this EverdoItem.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this EverdoItem.

        TODO  # noqa: E501

        :param contact_id: The contact_id of this EverdoItem.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def tags(self):
        """Gets the tags of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The tags of this EverdoItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EverdoItem.

        TODO  # noqa: E501

        :param tags: The tags of this EverdoItem.  # noqa: E501
        :type: list[int]
        """

        self._tags = tags

    @property
    def position_child(self):
        """Gets the position_child of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The position_child of this EverdoItem.  # noqa: E501
        :rtype: int
        """
        return self._position_child

    @position_child.setter
    def position_child(self, position_child):
        """Sets the position_child of this EverdoItem.

        TODO  # noqa: E501

        :param position_child: The position_child of this EverdoItem.  # noqa: E501
        :type: int
        """

        self._position_child = position_child

    @property
    def position_parent(self):
        """Gets the position_parent of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The position_parent of this EverdoItem.  # noqa: E501
        :rtype: int
        """
        return self._position_parent

    @position_parent.setter
    def position_parent(self, position_parent):
        """Sets the position_parent of this EverdoItem.

        TODO  # noqa: E501

        :param position_parent: The position_parent of this EverdoItem.  # noqa: E501
        :type: int
        """

        self._position_parent = position_parent

    @property
    def position_focus(self):
        """Gets the position_focus of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The position_focus of this EverdoItem.  # noqa: E501
        :rtype: int
        """
        return self._position_focus

    @position_focus.setter
    def position_focus(self, position_focus):
        """Sets the position_focus of this EverdoItem.

        TODO  # noqa: E501

        :param position_focus: The position_focus of this EverdoItem.  # noqa: E501
        :type: int
        """

        self._position_focus = position_focus

    @property
    def position_global(self):
        """Gets the position_global of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The position_global of this EverdoItem.  # noqa: E501
        :rtype: int
        """
        return self._position_global

    @position_global.setter
    def position_global(self, position_global):
        """Sets the position_global of this EverdoItem.

        TODO  # noqa: E501

        :param position_global: The position_global of this EverdoItem.  # noqa: E501
        :type: int
        """

        self._position_global = position_global

    @property
    def repeated_on(self):
        """Gets the repeated_on of this EverdoItem.  # noqa: E501

        TODO  # noqa: E501

        :return: The repeated_on of this EverdoItem.  # noqa: E501
        :rtype: int
        """
        return self._repeated_on

    @repeated_on.setter
    def repeated_on(self, repeated_on):
        """Sets the repeated_on of this EverdoItem.

        TODO  # noqa: E501

        :param repeated_on: The repeated_on of this EverdoItem.  # noqa: E501
        :type: int
        """

        self._repeated_on = repeated_on

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EverdoItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
