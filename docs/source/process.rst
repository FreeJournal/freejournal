Development Process
===================

Git Standards
~~~~~~~~~~~~~~

Generally, we followed Git model described in [this 
document](http://nvie.com/posts/a-successful-git-branching-model/). Here are some of the key concepts.

The `develop` branch
--------------------

`develop` was considered the go-to branch to start work. All changes that people make eventually get 
merged into develop.

Feature branches
----------------

When working on an issue, we created new branches off of `develop` and named it something relevant to the feature 
that was being implemented. Once done working on the issue, we mark it with the `needs-review` label. 
After another team member reviews it, it can be merged into `develop` by the branch maintainer for that iteration.

The `master` branch
-------------------

The master branch should only have finished, bug-free code that represents a complete released version. At the 
end of every sprint, we tag a commit on `master` to represent the work completed for that iteration. 
Unlike the model described in the blog post, we will not use release or hotfix branches as they're overkill 
for a project of this size.

Some helpful commands
---------------------

Start a new feature branch:

```
$ git checkout develop
$ git checkout -b myfeature
```

Merge a feature branch into `develop`:

```
$ git checkout develop
$ git merge --no-ff myfeature
```

Update `master` and tag a release:

```
$ git checkout master
$ git merge --no-ff develop
$ git tag -a iteration-3
```

Scrum Process
~~~~~~~~~~~~~~

Sprints
-------
For this project, we will use two-week sprints that correspond to each iteration meeting.

**Sprint planning meetings**

We meet for the first time at the beginning of each sprint. At these sprint planning meetings, we:

 * Create new issues for work that needs to be completed
     * Determine which issues are within the scope of the sprint
     * Give each issue a point value using Scrum ﻿Poker
     * We all choose a Fibonacci number to represent the difficulty of the issue, and keep it hidden
     * After a count to three, we all reveal the numbers
 * We discuss the point value the issue should have based on the numbers that the team revealed
 * Assign a team member to each issue

**Sprint scope**

Once we decide what issues are in a particular sprint, no more issues should be added or taken away.

Stand-ups
---------

On weeks when we're meeting and not having sprint planning meetings, we will have a "stand-up" where we 
discuss the current sprint. Each team member discusses the following:

 * What they're currently working on
 * Risks: issues or pieces of work that might not be finished by the end of the sprint
 * Blockers: work that other team members need to complete first before the team member can finish their own work


Refactoring
-----------

Refactoring is required upon an unfavorable code review, or when excessive errors are detected in a particular 
piece of functionality.  Overall, we have so far undergone several rounds of refactoring, including structural
and internal refactoring on the structure of the code.  The most recent refactoring effort was to address the
PEP8 standard, to which we have now achieved partial (almost full) compliance.


Collaborative Development
~~~~~~~~~~~~~~~~~~~~~~~~~

Team Communications
-------------------

All meeting and scheduling coordination, as long as communications for requests between individual group members
needing immediate resolution are handled by the team's GroupMe account, which uses the "FreeJournal" group name.

GitHub Issues
-------------

To keep track of work on pending user stories and use cases, we will use GitHub issues.

**Milestones**

We will use Milestones for each sprint to identify which issues need to be completed.

**Labels**

 * `front-end`: front-end issues
 * `back-end`: back-end server and cacheing issues
 * `library`: protocol and Python FreeJournal library issues
 * `N-points`: indicates the amount of work required for this issue
 * `needs-review`: this issue is done, but someone should review it before it gets merged in.

Coding Standards and Review
~~~~~~~~~~~~~~~~~~~~~~~~~~~

All code is required to follow the Python PEP8 formatting convention, as is standard for Python projects.  
Developers should not merge directly to the develop or master branches, simply creating pull requests as 
described in the Git Standards section above and allowing package maintainers / managers to update the develop 
and master branches as requested.

Testing
~~~~~~~

Throughout the project, we enforced an 80% code coverage requirement on all submitted code.  We used the 
Travis continuous integration system to run automatic unit and integration tests on all new commits and pull 
requests. For an example, `see here <https://github.com/FreeJournal/freejournal/pull/118>`_.  We also use 
coverage.py and the `FreeJournal Coveralls page 
<https://coveralls.io/r/FreeJournal/freejournal?branch=develop>`_ to track and measure changes in code 
coverage from testing our software.  We finished the project with over 80% code coverage and a passing build.


Unit tests were required for all new methods, and integration tests for all new functionality or dependencies
introduced as development proceeded.
