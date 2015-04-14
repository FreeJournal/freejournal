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

- **Documents** : Documents are files that are leaked to the FreeJournal network.  Documents have an associated name, description,
timestamp, and file that can be viewed.

- **Collections** : Collections are groups of documents, published together by the same user.  Collections can be updated (documents
added, removed), timestamped, and browsed together.  Nodes can blacklist or whitelist which connections they wish to mirror.


Components
~~~~~~~~~~

The FreeJournal is made up of the following several components attempting to achieve the aforementioned goals:

Backend/Library
----------------

The backend/library of freejournal provides an abstraction of the FreeJournal network into Python objects, powering all other
interfaces described below.  The backend/library includes a relational database used for caching incoming network objects.


Command-Line Interface
----------------------

The command line interface is designed to allow node operators and power users to interact with the network.  It will support
all essential network tasks, including document/collection maintenance, publication, and retrieval.  It will also provide an
easy way to launch the web interface, install dependencies, and run the uploader application.

Web Interface
-------------

The web interface is designed to allow users to view, timestamp, and otherwise interact with uploaded documents and collections
to the network.  The web interface should be familiar to users of other web services, and provide an abstraction of the underlying
FreeJournal peer-to-peer network for users.  The web interface should not support uploading for security purposes.

Uploader Application
--------------------

The uploader application is designed to provide securit to document uploaders, allowing for a relatively easy to use interface
that ensures the anonymity and integrity of the documents being submitted are protected.  The uploader application will eventually
be packaged in a virtual machine supporting the Tor anonymity network.

High-Level Goals
~~~~~~~~~~~~~~~~
This project aims to accomplish the following core goals, differentiating us from currently available projects:

**User friendliness** - Many of the other applications targeted at the secure and confidential release of documents require high 
levels of technical proficiency reserved for advanced technical actors.  We aim to allow the ordinary user to engage with 
FreeJournal, with a clear and simple user interface familiar to users of little technical proficiency.

**Modular design** - By designing both a library to support our document release protocol and a separate user interface for 
users to easily add and view documents, we allow for a variety of front-end implementations, from desktop apps and virtual 
machines to webapps.  Building an open protocol on top of the already existing open Bitmessage protocol ensures that future 
developers can easily build applications to integrate with FreeJournal.

**Deniability** - One of the central concerns of publishers of controversial material is their ability to be identified.  We aim 
to provide automatic steps to remove identifying information from source documents, and deniability of communications over the 
wire such that an eavesdropping attacker would be unable to ascertain whether a user of the system did or did not publish any 
documents (or indeed use the system at all).

**Trust** - In order to allow for curation and verification of source material usually only possible through a traditional, 
top-down editorial process, we will provide a platform for public discourse and analysis of the documents, as well as a system 
for users to rank and promote trustworthy documents to other users of the system.  We will do so by allowing users to support 
document publishers through peer to peer tokens like Bitcoin, providing both a reward for quality content and a ranking system 
that would be expensive for an adversary to attack.

**Transparency** - We aim to ensure that every aspect of our system is open in both design and implementation.  We plan on using 
unique cryptographic properties extending those used in Bitcoin and the Bitmessage protocol to provide clear and auditable 
information to the public about which documents were published together and when certain documents were published.  Through such 
an open system, we will provide an auditable process for document publishers, who can determine exactly the steps their document 
will take through the publication process (unlike in shadowy and closed organizations like newspapers).

**Inclusiveness** - By the design of the network, its participation will be open to all.  We aim to require no fees in order to 
publish or read documents, and to provide easy tools that can be used by users of all technical proficiencies.  We also plan on 
providing a protocol that is resistant to censorship or manipulation, allowing all potential users to engage with the system 
regardless of their motivation or personal views or character.

**Confidentiality** - One key usecase for FreeJournal is the ability for existing journalists to gather documents.  To address 
this usecase, we will allow groups of documents to be published only to private users or groups, so that existing journalist 
outlets need only post their FreeJournal account to have private leaks disseminated directly through them via this public 
protocol.  We will protect the confidentiality of such documents by encryption.  Furthermore, we will enforce pseudonymity as a 
requirement, ensuring that FreeJournal accounts are unlinkable to real-world identities.

**Integrity and Availability** - By building on the Bitmessage platform, we are leveraging a global peer-to-peer network that is 
designed to be robust and immune to censorship or takedown attempts.  We use the blockchain data structure to protect published 
documents and ensure they reach their intended audience without censorship.  We use the distributed node system already 
available in Bitmessage to ensure that FreeJournal cannot be taken down by targeting a specific organization or set of servers, 
as long as there are nodes in the network.  We leverage cryptography heavily to authenticate groups of documents and users 
publishing these documents, and will provide methods to check that users running the FreeJournal software are running an 
unmodified version with no tampering or backdoors.

**Fine-grained control** - We believe that any protocol addressing these issues must be fundamentally document-agnostic, and 
cannot inherently censor or discriminate against any particular class of documents.  However, as some documents uploaded may be 
illegal in certain jurisdictions or controversial for other reasons, we also believe it is the choice of each individual node 
operator to be able to either whitelist or blacklist the items they store or relay, providing them fine-grained control of the 
traffic flowing through their machine and allowing them to stop relaying items passing through their node at any time.  Because 
the data structures required to maintain the integrity of the network do not depend on our individual nodes providing all 
content, any exclusions on the part of a node will be clear to any user querying that node, maintaining the transparency and 
availability requirements previously mentioned.

Comparison to Similar Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Bitmessage** - `Bitmessage <http://bitmessage.org>`_ is a peer-to-peer communications protocol intended to be distributed, 
peer-to-peer, pseudonymous, and cryptographically secure.  One of the use cases outlined initially during the design of the 
BitMessage system was the leaking or `release of documents <https://bitmessage.org/forum/index.php?topic=3.0>`_.  However, 
BitMessage only provides utility to message other users or groups, lacking utilities to evaluate and rank documents, provide for 
lasting public archival, or provide for public discourse and evaluation.  The lack of these features means a third-party 
journalistic entity like WikiLeaks or a traditional newspaper must receive these documents, opening up potential opportunities 
for the introduction of bias and violation of source integrity.  Furthermore, BitMessage has key technical problems rendering it 
unsuitable for distributed document distribution - messages in the network often have a short lifespan, sometimes only lasting 
days, and communication channels have not been shown to stand up against serious attack.  Lastly, BitMessage has no frontend 
providing for clear user explanation and interaction, rendering it unsuitable for all but the most technical users. In this 
regard, we believe BitMessage represents only a component of the ideal system we describe in our Motivation section.

**Wikileaks** - The most similar complete solution to what we are proposing is the journalistic organization `Wikileaks 
<http://wikileaks.org/>`_, an organization allowing users to view and submit documents publicliy through the Internet and 
promising for minimal discrimination.  Despite this, several high-profile failings of Wikileaks make it a poor choice for such 
purposes.  In the past, organizational insiders have destroyed documents and otherwise compromised the integrity of the 
organization (https://darkhorsenet.wordpress.com/2013/01/08/daniel-domscheit-berg-the-man-who-sold-out-wikileaks-2/).  
Furthermore, like any organization, Wikileaks’ key members are vulnerable to attack by powerful entities, weakening the 
organization and proving it to not be resilient.  Other leaking organizations like OpenSecrets attempt to maintain transparency 
through organizational practices, however we believe this is far from ideal.  If these organizations could be replaced with 
peer-to-peer protocols allowing for document and information exchange, the guarantees provided to the document publishers become 
well-defined and mathematically rigorous, guaranteeing full control of their published documents.

**Freenet** - `Freenet <https://freenetproject.org/>`_ is a distributed data store specifically designed for the publication of 
files and documents specifically intended and targetted at the publication of controversial information.  In this regard, 
Freenet is the most similar project to our intended design in its ambitions and design.  Freenet is based on a complex system of 
encrypted node-based routing and distributed hash tables which provide excellent anonymity and deniability guarantees.  Unlike 
our proposal, however, Freenet allows for minimal transparency and inclusiveness by making it difficult to achieve low-latency 
interaction between large numbers of users.  Freenet is also unable to provide the integrity guarantees available to the Bitcoin 
blockchain, in which strict timestamp guarantees resistant to even targeted adversarial attacks are provided.  Furthermore, 
Freenet is extremely slow, requiring several hours for initial synchronization and often minutes for file downloads, 
unacceptable for the real-time experience users expect from web applications today.  Freenet is far from user friendly and lacks 
good front-end software, and lastly inherently lacks the ability to create a meaningful crowd-ranking system able to filter 
content for quality and accuracy without the introduction of an additional protocol (due to its design, strict anonymity, and 
inclusiveness).  On the other hand, Freenet is a mature project that may be used in the backend of our system if we find the 
storage problem too difficult to solve with Bitmessage, sacrificing speed for project maturity.

**Tor/I2P** - We will briefly mention these projects for their ability to provide low-latency access to web services 
anonymously.  These are not really comparable to our proposed system as they only provide a means of passing messages and not a 
fully integrated platform for discussion and open publication for information.  However, both projects provide mature, 
well-tested, and strong anonymity guarantees that make them ideal for users using our system who wish to add an extra layer of 
anonymity.  We will aim to support the use of such software to offer our users an existing and secure way to interact with our 
system without the need for our own encrypted routing scheme.
