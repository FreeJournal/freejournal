Architecture and Design
=======================

System Architecture
~~~~~~~~~~~~~~~~~~~

The system architecture aims to implement the overall design of the application.
See the Design section of this documentation for more details.  Overall, the application
follows an MVC pattern, with a `models` and `controllers` directory, and views provided in
the `frontend` directory.

Dependencies and Frameworks
~~~~~~~~~~~~~~~~~~~~~~~~~~~

freejournal makes use of several external dependencies, each affecting the
architecture and functionality of the project in some way.

**Bitmessage** : BitMessage is used as a communication channel between instances of the freejournal software.  Bitmessage's primary
purpose in the freejournal project is to maintain an *index* of all collections currently hosted by the network.  This is
accomplished by storing "DocIndex" messages in the Bitmessage network, with each one representing the state of a collection at a
particular point in time (see the Protocol section for more information).  **Consequences**: As a consequence of Bitmessage use,
the CPU usage of our application is extremely high.  This is because Bitmessage works by attempting to decrypt every message
on the network, parsing those which it is able to decrypt.  Because there are many messages on the network unrelated to freejournal,
this is an expensive operation that uses processing power needlessly.  Another consequence of the Bitmessage integration is the delay
when publishing a collection, required to perform the proof of work to be accepted by the Bitmessage network.  Both of these tradeoffs
are acceptable to us, as our users will be willing to trade CPU usage for the extra security and anti-spam features these restrictions
provide.

**Freenet** : While Bitmessage *indexes* documents, Freenet *stores* documents, providing a DHT-based model for document storage
leveraged by our application.  When downloading documents, clients request the hash of the document stored in the Bitmessage index
from the Freenet network.  Uploading procedes similarly.  **Consequences**: As a consequence of Freenet integration, document
uploading and downloading is quite slow (due to security restrictions imposed by Freenet itself).  This affects the ability of users
to easily deploy freejournal on their local machine, requiring them to wait for the software to synchronize and download the documents
they are interested in rather than having instant access.  Despite this, the security and anonymity guarantees the Freenet network
provides to its users are sufficiently strong that the trade-off is acceptable.

**Bitcoin** : Bitcoin is used to store the timestamp of a document collection after it was uploaded, anchoring its provenance to 
a specific point in real time.  For more information, see the Protocol section of this document.

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
.. uml:: ../../backend/datastructures/fj_message.py

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

The instal class is responsible for preparing dependencies associated with Bitmessage communication.

Freenet Connection
------------------

.. uml:: ../../freenet/FreenetConnection.py
.. uml:: ../../freenet/install.py

The Freenet connection is responsible for communication with the Freenet network, uploading and downloading
the document bodies synchronized in collections over the Bitmessage network.

Bitcoin Connection
------------------

.. uml:: ../../timestamp/timestampfile.py

The timestamp class is responsible for communicating with the Bitcoin network to both retreive and upload
timestamps for given collection hashes.  The timestamp library currently uses the `ProofOfExistence API 
<http://proofofexistence.com/>`_.

Sequence Diagrams
-----------------

(coming next iteration)


