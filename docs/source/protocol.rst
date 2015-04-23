Protocol Specification
======================

Abstract Goals
--------------

The goal of this project is to facilitate the publication of documents without providing a direct link to the source of the documents' identity, and while creating a network over which these documents can be published without censorship or removal by any single third party.

If successful, this project will fulfill the following goals:

**Deniability**: An omnipotent network observer gains no knowledge on a source publishing documents other than that they are 
using anonymity software (BitMessage, Tor, etc).  No conclusive evidence of the document publication is possible through 
exclusively network analysis.

**Transparency**: Any interested users can view all details about the operation of the network, participate in the network, 
and check the validity of network data themselves.  Developers can develop tools around these purposes.

**Inclusiveness**: Participation in the protocol will be open to all, with no financial or significant computational upstart 
requirements.

**Integrity and Availability**: Documents sent to the network will be maintained for a reasonable time period given enough 
node/user interest, allowing other users to save them for public record and archival purposes.  Documents will be accessible for 
the entire network long as they are hosted by a single node.

**Fine-grained Control**: Nodes have the right to decide how to allocate their computational resources.  By allowing for 
optional whitelisting and blacklisting policies, we allow nodes to remove resources they do not wish to support from their 
drives.  This allows the content of the overall network to be democratic and to depend on a set of nodes.

**Built-in Trust**: Users can rank and vote on the popularity of documents in a trusted way using the Bitcoin blockchain or 
other machine-verifiable tokens.  Users can sort by a variety of ranking systems to expose controversial documents and hedge 
against manipulation of this system.

Message Protocol
----------------

The message protocol is based on JSON.  Each message is stripped of extraneous whitespace to reduce the required PoW on the 
BitMessage network.  Further iterations of the protocol may take advantage of packed binary data if we find further compression 
is necessary, though this is unlikely given current space requirements.

Message Types
-------------

The FreeJournal protocol is designed to be extensible in allowing any number of message types to be passed to the inter-node 
communications channels.  Each message is JSON formatted and stripped of nonessential whitespace before being base64 encoded for 
the BitMessage network.  All messages share a common structure, with the following universal JSON elements:

.. code-block:: none

    FJ_message = {
        "protocol" : "FJ1.0", 
        "type_id" : [message type ID, see below],
        "original_sender" : [sender BitMessage address],
        "signature" : [full FJ_message payload signature by "original_sender" public key],
        "time_created" : [original message creation time, UTC, no reliability guarantees]
        ...
    }

where the remainder of the fields are specified by the individual message.  All binary data, including signatures, is 
base64-encoded.

FreeJournal messages are signed for authentication, so that only publishers can create associated collection and document 
messages.  However, any node can rebroadcast these messages unmodified with the same signature.  This is intended to keep 
popular messages alive in the BitMessage network despite the message expiry of 2-28 days inherent in the BitMessage system (see: 
BitMessage TTL).

Collection Index Message (PubCollection)
****************************************

.. code-block:: none

    PubCollection = {
        ...
        "type_id" : 1,
        "title" : [collection title],
        "description" : [collection description],
        "keywords" : [collection keywords],
        "address" : [collection channel BitMessage address (see above)],
        "documents" : [comma-separated list of (SHA256 document hash,document title,document description) triples],
        "merkle" : [Merkle root of 'documents' list above],
        "tree"   : [full Merkle tree of documents],
        "BTC" : [Bitcoin address associated with publisher],
        "version" : [index revision number]
    }


Each message can be identified by its "merkle" field, which is assumed to be unique.

Each message captures the state of a collection of documents, encapsulating the available documents and metadata around their 
publication.  Each collection can be uniquely identified by the "address" field, containing its BitMessage address.  New 
versions of indices as specified by the "version" field replace old versions automatically in all nodes, allowing for the 
retroactive editing or addition of documents to collections.  Timestamps, however, are individual to each document and cannot be 
retroactively edited as they are published as a proof of knowledge (hash) on the Bitcoin network.

When a node *subscribes* to a collection, its default behavior will be to rebroadcast the associated PubCollection message every 
two weeks or any time it sees a request (see below), for a total maximum of one rebroadcast per week.

Rebroadcast Request (Rebroadcast)
*********************************

.. code-block:: none

    Rebroadcast = {
        ...
        "type_id" : 3,
        "resource_type_id" : [type of message to rebroadcast],
        "resource_id" : [unique identifier of resource],
        "resource_channel" : [BitMessage address where the resource was originally sent]
    }


A rebroadcast request need not be uniquely identified (and if necessary can be through the BitMessage message ID).

A rebroadcast request encapsulates a node's request to retrieve any of the other message types if these messages are not found 
in the BitMessage network (have expired due to time to live).

All listening nodes will rebroadcast the relevant resource to the appropriate channel of the FreeJournal network (the 
"resource_channel") will rebroadcast if they have not seen the message broadcast in over a week, up to a maximum of once per 
week.

The "resource_channel" field must match the channel to which the rebroadcast request is sent.

Private Document Share Message (PrivDocument)
*********************************************

.. code-block:: none

    PrivDocument = {
        ...
        "type_id" : 4,
        [..., same as PubDocument]
    }

The document share message is intended to share documents between nodes, with all associated metadata intact.  All nodes 
subscribing to a collection will download all documents published to that collection, reassembling and caching these documents 
locally to be rebroadcast on request.

In order to allow for private document collections, the protocol allows for the AES encryption of the payload, description, and 
title of any document message.  These AES keys can then be shared offline/out-of-band or through BitMessage private message.

**NOTE:** this feature will not be developed in the initial FreeJournal prototype, but is intended for future growth and 
extensibility of the protocol to satisfy private publication needs with the same guarantees we provide to public publications.

Trusted Timestamping
--------------------

Trusted timestamping of each individual document is achieved by cross-referencing OP_RETURN data in the Bitcoin blockchain.  The 
Merkle root of a collection is broadcast to the Bitcoin blockchain.  Each document stored locally stores the latest 
timestamped/checkpointed Merkle tree, and timestamps are verified by checking the network for this Merkle root and providing the 
document's Merkle path.

While collections will always store only the latest data as specified by the index version, they also store old Merkle trees and 
their associated versions.  When a new timestamp comes in on the Bitcoin network, the local database is checked for any Merkle 
trees with the same root.  All documents in the Merkle tree are then updated with this timestamp and Merkle tree if they do not 
have an older timestamp associated with them.
