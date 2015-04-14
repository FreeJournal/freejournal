Design and Goals
================

freejournal is a document publication system intended to allow the public release of documents in a way that is resistant to
suppression or censorship.

Whistleblowers, journalists, and others need a way to anonymously publish documents to a public or private audience of their 
choosing.  Currently, they do so through complex anonymity software restricted to developers and cryptography experts, or 
through third-party institutions prone to internal politics and editorializing like Wikileaks.  Many other users sharing less 
sensitive content defer the storage and management of their information to third-party services, like LiveJournal, imgur, or any 
number of other content hosting companies.  freejournal is a protocol and accompanying user-friendly front end application 
designed to assist in the anonymous and uncensorable release of documents to a public audience in a cryptographically secure 
manner, without requiring trust in any third party services.  FreeJournal can greatly improve freedom of information worldwide 
by allowing for open, anonymous releases of documents not vulnerable to manipulation by any third party.

Participants/Actors
~~~~~~~~~~~~~~~~~~~~

There are several roles an individual can adopt when interacting with the FreeJournal software:

Document Viewers
----------------

Document viewers are individual users who are interested in browsing a document.  This could be either because they were
told to or linked to view the document, or simply out of curiosity regarding what new documents are being published. 
Such a user will have two choices: they can run their own version of the freejournal software, hosting the web interface
locally on their machine and accessing it through any browser at `localhost`.

Alternatively, these users can simply visit the web interface hosted by a "node" they trust.  This "node" is hosted by
another user or organization, and can be accessed through HTTP or any protocol supporting HTTP (like Tor, I2P, cjdns, etc.)
This will likely be the common usage pattern for most users, who desire convenience over security and who are willing to
trust a node run by a reputable organization or party to serve them accurate content.

Document Publishers
-------------------

Document publishers are those wishing to publicly release documents in a way immune to third-party manipulation or censorship.
These users often value their security and anonymity above convenience, and often wish to conceal or disguise their real
identities to the public.  For these users, we will provide a **document uploader** application.  This application will work
in a virtual machine that communicates to the Internet exclusively through the Tor anonymity network, providing the maximum
possible isolation for these users from network traffic inspection attacks.

Nodes / Infrastructure Providers
--------------------------------

In such a network, it is critical to have the infrastructure to host and serve documents to new users interested in downloading
them.  While traditional services handle this with a centralized database, freejournal is a p2p system and thus makes use of
nodes.  Nodes are instances of the freejournal project which host documents uploaded to the network and relay them to other
users.  Nodes also are responsible for the upkeep of the network, as well as its synchronization that allows all users to 
obtain the documents they are interested in.

Nodes will be run by users who are interested in supporting free speech, similar to the users running Tor relays, Freenet nodes,
or other peer-to-peer anonymity network nodes.  These users will donate disk-space, often on high powered servers, to cache
and redistribute freejournal documents.  Nodes will also often be interested in controlling the content they mirror, removing
offensive and illegal content from their machines as necessary to avoid violating laws in their jurisdictions.

Project Motivation
~~~~~~~~~~~~~~~~~~

The need for open document publishing and whistle blowing in society is a well established philosophical argument that hinges on 
the fundamental right to share and exchange information freely and without censorship.  The famous `panopticon experiment 
<https://en.wikipedia.org/wiki/Panopticon>`_ imagines a society in which the constant surveillance of all its members leads to a 
crippling of intellectual debate, arguing for a strong need for open information sharing.  Despite this, it remains 
prohibitively difficult to share such information, requiring advanced technical precautions to do so with any level of 
anonymity.  We seek to provide an open, safe and global public space for the release and discussion of any sort of documents, 
strongly resistant to being censored or attacked by any third party or group.  In doing so, our motivation is to foster 
transparency and debate on controversial primary source material.

Previously, the role of mediating document release to the public fell to journalistic organizations, both corporate (New York 
Times, The Guardian, etc.) and community-based (WikiLeaks, OpenSecrets, etc.)  An organizational approach to this fundamental 
problem, however, is fatally and deeply flawed.  Publishers of documents must trust this third-party to accurately and wholly 
publish their information.  Furthermore, publishers must coordinate the transfer of this information, often involving advanced 
technical precautions.  The involvement of third parties in any system required to provide strong security guarantees is 
considered by many security experts to be a security hole, `unacceptable in a system for open document release 
<http://szabo.best.vwh.net/ttps.html>`_.

The freejournal project attempts to bridge this gap by providing a system for public document release that is not controlled
by any particular third party, and is open to all users in a document-agnostic fashion.

Terminology
~~~~~~~~~~~

Documents and collections

Components
~~~~~~~~~~

The FreeJournal is made up of several components attempting to achieve the aforementioned goals:

Command-Line Interface
----------------------

Web Interface
-------------

Uploader Application
--------------------

High-Level Goals
~~~~~~~~~~~~~~~~

Comparison to Similar Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

