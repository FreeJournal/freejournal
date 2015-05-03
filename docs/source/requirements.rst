Requirements and Specifications
===============================

Use Cases
~~~~~~~~~

The most important use cases in the system that have been implemented as part of this project are described below, in
`use case brief <http://tynerblain.com/blog/2007/04/24/apr-use-case-briefs/>`_ format.

UC1
---

**As a publisher, I want to be able to upload arbitrary documents to the FreeJournal network.**

Actor: Document publisher

Description: The publisher is using a local application (the "uploader application") to upload documents to the FreeJournal 
network, mirroring them to Freenode and indexing them on the BitMessage network.  The publisher can also run the application in 
a secure virtual machine to protect their identities.

UC2
---

**As a viewer, I want to be able to view documents that are uploaded using FreeJournal using a local application or a web browser.**

Actor: Document viewer

Description: The user is using either a local application or a remotely hosted web application to view documents on the FreeJournal
network.  The user is able to download, browse, and view available documents through a friendly interface that displays document
details including date, publication time, and keywords.

UC3
---

**As a publisher, I want to be able to manage my uploaded collections and add or remove documents.**

Actor: Document publisher

Description: The document publisher is uploading a collection of documents, and is able to add or remove documents from that 
collection, modifying its state.  The document publisher is then able to publish the collection to the network, allowing for
multiple versions of the same collection.  All nodes will host the latest version of the published collection.

UC4
---

**As a network operator, I want to be able to run a node to benefit the overall health of the network and spread documents.**

Actor: Node / network operator

Description: The network operator is able to start a node that donates storage space and bandwidth to mirror documents on the
FreeJournal network.  The network operator is also able to host a web interface on their node accessible by regular users
through a variety of protocols (HTTP, HTTPS, Tor, etc.)


UC5
---

**As a viewer, I want to be able to authenticate the timestamps of documents to gain confidence as to when they were published.**

Actor: Document viewer

Description: The document viewer is able to authenticate the timestamps of documents by viewing a "root" hash that includes the
hash of the document.  The user can then use the ProofOfExistence service or manual cross referencing of the Bitcoin blockchain
to verify the authenticity of their timestamp.


Other Use Cases (Minor Use Cases)
---------------------------------

These usecases specify details about the main use cases listed above.  The briefs are not provided for brevity:


UC6 - As a publisher, I want it to be impossible to trace documents back to me personally.

UC7 - As a publisher, I want to be able to group multiple documents under a single handle, so that documents can be linked to a single anonymous user.

UC8 - As a publisher, I want to be able to submit documents with a particular keyword.

UC9 - As a viewer, I want to be able to view document information including keyword, date, or rating, sorting content appropriately.

UC10 - As a developer, I want low-level API access to the FreeJournal API to develop my own applications and verify the security of FreeJournal data.

UC11 - As a publisher, I want to be able to group documents I upload into collections and publish them together.

UC12 - As a network operator, I want to be able to host and rebroadcast documents and collections for publishers.

UC13 - As a network operator, I want to be able to remove collections that I object to from my machine.
