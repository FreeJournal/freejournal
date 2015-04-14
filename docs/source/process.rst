Development Process
===================

Git Standards
~~~~~~~~~~~~~~

Generally, we should follow the Git model described in [this document](http://nvie.com/posts/a-successful-git-branching-model/). 
Here are some of the key concepts.

The `develop` branch
--------------------

`develop` should be considered the go-to branch to start work. All changes that people make eventually get merged into develop.

Feature branches
----------------

When working on an issue, create a new branch off of `develop` and name it something relevant 
to the feature that you're trying to implement. Once you're done working on the issue, mark it with the `needs-review` label. 
After another team member reviews it, you can merge it into `develop`.

The `master` branch
-------------------

The master branch should only have finished, bug-free code that represents a complete released version. At the end of every 
sprint, we can tag a commit on `master` to represent the work completed for that iteration. Unlike the model described in the 
blog post, we will not use release or hotfix branches as they're overkill for a project of this size.

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
On weeks when we're meeting and not having sprint planning meetings, we will have a "stand-up" where we discuss the current sprint. Each team member discusses the following:
 * What they're currently working on
 * Risks: issues or pieces of work that might not be finished by the end of the sprint
 * Blockers: work that other team members need to complete first before the team member can finish their own work

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

All code is required to follow the Python PEP8 formatting convention, as is standard for Python projects.  Developers should not
merge directly to the develop or master branches, simply creating pull requests as described in the Git Standards section above
and allowing package maintainers / managers to update the develop and master branches as requested.
