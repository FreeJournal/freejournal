Architecture and Design
=======================

System Architecture
~~~~~~~~~~~~~~~~~~~

The system architecture aims to implement the overall design of the application.
See the Design section of this documentation for more details.  Overall, the application
follows an MVC pattern, with a `models` and `controllers` directory, and views provided in
the `frontend` directory.

Models
------

The following are the freejournal database objects:

.. uml:: ../../models/document.py
.. uml:: ../../models/collection.py
.. uml:: ../../models/keyword.py

Each Column is a database column in our local cache.  Each file represents a type
of database table and therefore entry.  These models also form the base classes 
for the backend of the freejournal API.

Cache
------

.. uml:: ../../cache/cache.py
.. uml:: ../../cache/db.py

The cache is intended to provide an abstraction for dealing with database objects
such as the models above, simplifying application syntax.  The cache also stores
the current session to allow for session reuse.

Controllers
-----------

.. uml:: ../../backend/controller.py
.. uml:: ../../backend/fj_message.py

The controller files provide for an API for packages using the core freejournal 
library to manipulate the models.

Bitmessage Connection
---------------------

.. uml:: ../../bitmessage/bitmessage_keepalive.py
.. uml:: ../../bitmessage/bitmessage_listener.py
.. uml:: ../../bitmessage/bitmessage.py
.. uml:: ../../bitmessage/install.py

These classes are responsible for communicating with the BitMessage software, which
provides a communication channel over which freejournal nodes communicate with each other.

The listener listens for new messages coming in on the network, dispatching them to be processed
and added to the local cache if necessary.  The connection is also responsible for publishing
new messages to the network, broadcasting collections to the network at large.


Freenet Connection
------------------

Bitcoin Connection
------------------

Sequence Diagrams
-----------------

(coming next iteration)


Dependencies and Frameworks
~~~~~~~~~~~~~~~~~~~~~~~~~~~

freejournal makes use of several external dependencies, each affecting the
architecture and functionality of the project in some way.

- BitMessage
