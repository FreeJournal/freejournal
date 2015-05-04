Future Plans
============

Our future plans include extending the functionality of FreeJournal to that of a complete
document and binary data upload and sharing platform.  The following features still need
improvement or implementation:

- Bitcoin timestamping (better frontend integration)
- Bitcoin voting / ranking algorithms
- Robustness / scalability tests with large datasets


Team Member Reflections
-----------------------

in no particular order.

Dan
~~~

Overall I had a great time working on this project and learned a good deal. I really liked the concept and 
goals of the project. I worked mostly on backend of the project with integrating a couple dependencies to help 
achieve our goals. In terms of process I had a good time working with everyone in our group and belive we 
functioned very well to complete it.


The scrum development process worked well for us as it was flexible and easy to follow. What I learned most 
during the project was about the benefits and headaches of depending on so many different libraries/softwares. 
Our project probably isn't possible without things like FreeNet and Bitmessage, however the source of most 
problems came from these dependencies.

Wenxue
~~~~~~

I am working on the back-end. It is a good experience to work on a project from ideation to research, design, 
and development. We are using a lot of libraries, such as Bitcoin blockchain, Bitmessage, Freenet and etc. One 
of the issues I am working on is using Bitcoin transactions timestamp the documentation. When I was working on 
it, I learned how to do some research on the new concepts I did not know before and use them in the project.

Walker
~~~~~~

Working on this project was a productive learning experience. It was a great chance to develop my skills 
working with Git and Python, and was the first chance I've had to work on a larger-scale project using GitHub. 
Our implementation of Scrum, which used GitHub's issue system to keep track of tickets, seemed to work pretty 
well, especially given our weekly pace for meetings. My role was primarily focused on the front-end website. 
It was implemented using Flask, which allowed us to easily integrate the web server with the FreeJournal 
command line interface. Additionally, I worked on integrating SQLAlchemy and the caching system that stores 
documents locally, as well as the Bitmessage listener routine. Initially I suggested to the group that we use 
Celery to create asynchronous jobs and repeating tasks, but it ended up being too heavy of a dependency to 
include and instead I ended up implementing the repeating tasks using Python’s threading APIs.

Brian
~~~~~

Going into choosing a project team, I was determined to find a project that reflected my ideals, challenged me 
technologically, and ultimately was something that I was proud to put on my resume and show employers what I 
could accomplish in a full year long project. After reflecting on the project from beginning to end, I 
couldn’t be happier I chose Freejournal. I worked mostly on the Freenet side of the project, focusing on 
handling the submission and retrieval of ‘documents’ that have been leaked onto the freejournal network. As 
the project went on, I quickly discovered the integration that the project required a complete knowledge of 
the architecture, in order to fully understand what was happening at any given time. I feel like one of the 
most challenging parts of this project was understanding how all the dependencies fit together to create a 
finished project. This was largely realized in the complexity of our UML diagrams. Realizing just how 
complicated the stream of execution was on more complicated projects almost necessitates the visualization of 
some sort of stream of execution. This is what separates a “coder” from a “software engineer”, and why the 
latter is so important to software projects.



Fernando
~~~~~~~~

Working with a team on the Free Journal project has been a blast! I worked on the file timestamp module as 
well as the GUI for the document uploader. I learned a lot from the ideas and skills of my teammates. 
Especially that software bugs can appear when you least expect them. Everyone had something different to 
contribute and the Scrum method helped leverage that quality. As a result, we achieved our objectives and 
gained valuable experience working together as a team.

Phil
~~~~

I had a great time with all the guys on the team, and would definitely say it was a cohesive, informative,
and fun learning experience.  My primary role was organizational, focusing on developing the core ideas of
the project through documentation, code review, process management, and other specification creation.  I
was responsible for the documentation and creation of the Protocol Specification.  In additon, I also worked
on several refactorings, unit test additions, repository reorganizations, and other maintenance tasks.  Lastly,
I co-developed the initial models / cache architecture.  I really think the Scrum process and the Github-style
development we describe in this document was a great fit for our team, and I was surprised by how robust and
usable our final project is considering its complexity.  Overall, we didn't finish everything we set out to do,
but we still managed to put out an impressive piece of peer to peer software in a single semester... so I call 
that a big win!

Drew
~~~~

It was interesting to work on a somewhat large project from start to finish with seven people.  I believe the 
scrum process and our branch organization on Github allowed for consistent progress towards our goals.  A take 
away for this project is to have all the merging for a development cycle done and tested at least a couple 
days before the deadline.  Other than that, I think the project went smoothly.
