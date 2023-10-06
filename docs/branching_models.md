# **Git branching models**
- GitFlow
- GitHub Flow
- GitLab Flow
- Trunk-based development

## GitFlow
### This branching strategy consists of the following branches:
- Master
- Develop
- Feature
- Release
- Hotfix

![gitflow strategy](../resources/gitflow-branching-strategy.png)


## GitHub Flow
simpler alternative to GitFlow ideal for smaller teams

### This branching strategy consists of the following branches:
- Master
- Feature

Unlike GitFlow, this model doesn’t have release branches. You start off with the main branch then developers create branches, feature branches that stem directly from the master, to isolate their work which are then merged back into main. The feature branch is then deleted.

![githubflow strategy](../resources/github-flow-branching-model.jpeg)


## GitLab Flow

A simpler alternative to GitFlow that combines feature-driven development and feature branching with issue tracking.

### This branching strategy consists of the following branches:
- Master
- Production
- Pre-production/staging

While GitHub Flow assumes that you can deploy into production whenever you merge a feature branch into the master, GitLab Flow seeks to resolve that issue by allowing the code to pass through internal environments before it reaches production, as seen in the image below.

![gitlabflow strategy](../resources/gitlab_flow_environment_branches.png)
