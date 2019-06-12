"""Interact with the graphics libraries via mouse events.

- MOUSE_CLICKED
- MOUSE_PRESSED
- MOUSE_RELEASED
- MOUSE_MOVED
- MOUSE_DRAGGED
"""
import campy.private.platform as _platform

import enum

class GMouseEvent:
    """An event generated by some mouse interaction.

    Each mouse event records its event type, its parent window, and the mouse
    coordinate of the event.



    # Each mouse event
    # This event subclass represents a mouse event.  Each mouse event
    # records the event type (MOUSE_PRESSED,
    # MOUSE_RELEASED, MOUSE_CLICKED,
    # MOUSE_MOVED, MOUSE_DRAGGED) along
    # with the coordinates of the event.  Clicking the mouse generates
    # three events in the following order: MOUSE_PRESSED,
    # MOUSE_RELEASED, MOUSE_CLICKED.

    # As an example, the following program uses mouse events to let
    # the user draw rectangles on the graphics window.  The only
    # complexity in this code is the use of the library functions
    # min and abs to ensure that the
    # dimensions of the rectangle are positive::

    #     gw = _gwindow.GWindow
    #     print("This program lets the user draw rectangles.")
    #     while(True):
    #         e = gevents.waitForEvent();
    #         if (e.getEventType() == MOUSE_PRESSED):
    #             startX = e.getX();
    #             startY = e.getY();
    #             rect = gobjects.GRect(startX, startY, 0, 0);
    #             rect.setFilled(True);
    #             gw.add(rect);
    #         elif(e.getEventType() == MOUSE_DRAGGED):
    #             x = min(e.getX(), startX);
    #             y = min(e.getY(), startY);
    #             width = abs(e.getX() - startX);
    #             height = abs(e.getY() - startY);
    #             rect.setBounds(x, y, width, height);

    # Attributes:
    #     gwindow [GWindow]: GWindow in which MouseEvent occurred.
    #     x [float]: The x-coordinate at which the event occurred.
    #     y [float]: The y-coordinate at which the event occurred.

    # Notes:
    #     The x- and y-coordinates are given relative to the window origin at
    #     the upper left corner of the window.
    """

    def __init__(self, event_type, gwindow, x, y):
        """Create a :class:`GMouseEvent` with the given arguments.

        :param event_type: Which type of mouse event this object represents.
        :param gwindow: The originating :class:`GWindow`.
        :param x: The x-coordinate of the mouse.
        :param y: The y-coordinate of the mouse.
        """
        super().__init__()
        self._type = event_type
        self._gwindow = gwindow
        self._x = x
        self._y = y

    @property
    def window(self):
        return self._gwindow

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return "GMouseEvent({}, x={}, y={})".format(self.event_type.name, self.x, self.y)


@enum.unique
class MouseEventType(enum.Enum):
    MOUSE_CLICKED = 1  # TODO(sredmond): This is really a MOUSE_PRESSED. Note that somewhere.
    MOUSE_RELEASED = 2
    MOUSE_MOVED = 3
    MOUSE_DRAGGED = 4
    # MOUSE_ENTERED = 5
    # MOUSE_EXITED = 6
    # MOUSE_DOUBLE_CLICKED = 7
    # MOUSE_TRIPLE_CLICKED = 8


def onmouseclicked(function):
    """
    Usage::

        %gui tk
        from campy.gui.events.mouse import *
        from campy.graphics.gobjects import *
        from campy.graphics.gwindow import *

        window = GWindow()

        @onmouseclicked
        def add_circle(event):
            event.window.add(GOval(100, 100, x=event.x - 50, y=event.y - 50))
    """
    _platform.Platform().event_add_mouse_handler(MouseEventType.MOUSE_CLICKED, function)


def onmousereleased(function):
    """
    Usage::

        %gui tk
        from campy.gui.events.mouse import *
        from campy.graphics.gobjects import *
        from campy.graphics.gwindow import *

        window = GWindow()

        @onmousereleased
        def add_rect(event):
            event.window.add(GRect(100, 100, x=event.x - 50, y=event.y - 50))
    """
    _platform.Platform().event_add_mouse_handler(MouseEventType.MOUSE_RELEASED, function)


def onmousemoved(function):
    """
    Usage::

        %gui tk
        from campy.gui.events.mouse import *
        from campy.graphics.gobjects import *
        from campy.graphics.gwindow import *

        window = GWindow()

        @onmousemoved
        def add_circle(event):
            event.window.add(GOval(100, 100, x=event.x - 50, y=event.y - 50))
    """
    _platform.Platform().event_add_mouse_handler(MouseEventType.MOUSE_MOVED, function)


def onmousedragged(function):
    """
    Usage::

        %gui tk
        from campy.gui.events.mouse import *
        from campy.graphics.gobjects import *
        from campy.graphics.gwindow import *

        window = GWindow()

        @onmousedragged
        def add_circle(event):
            event.window.add(GOval(100, 100, x=event.x - 50, y=event.y - 50))
    """
    _platform.Platform().event_add_mouse_handler(MouseEventType.MOUSE_DRAGGED, function)


# TODO(sredmond): Add code to generate mouse events (for mocking) too.

# Convenient testing code.
# from campy.graphics.gwindow import GWindow

# from campy.graphics.gobjects import GOval, GRect

# from campy.gui.events.mouse import *

# window = GWindow(title='Mouse Event Test')

# @onmouseclicked
# def add_rect_on_click(event):
#         event.window.add(GRect(100, 100, x=event.x - 50, y=event.y - 50))

# @onmousereleased
# def add_circle_on_release(event):
#         event.window.add(GOval(100, 100, x=event.x - 50, y=event.y - 50))

# @onmousemoved
# def add_circle_on_move(event):
#         event.window.add(GOval(50, 50, x=event.x - 25, y=event.y - 25))

# @onmousedragged
# def add_rect_on_drag(event):
#         event.window.add(GRect(50, 50, x=event.x - 25, y=event.y - 25))

