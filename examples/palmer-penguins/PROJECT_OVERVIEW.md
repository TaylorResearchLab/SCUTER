# Palmer Penguins worked example

## Purpose

This directory is a real, compact SCUTER worked example intended for readers of the companion manuscript and for scientists learning the workflow. It will preserve the complete task-review-acceptance cycle in repository form so that the example can be inspected without access to the original AI chats or a Notion workspace.

## Scientific question

Among adult Palmer Archipelago penguins in the public `palmerpenguins` dataset, what is the association between flipper length and body mass, and how does that association change when species is considered?

## Dataset

The worked example uses the simplified `penguins` dataset distributed with the `palmerpenguins` package. The data were collected by Kristen Gorman and the Palmer Station Long Term Ecological Research program and are released under CC0. Package citation: Horst AM, Hill AP, Gorman KB. *palmerpenguins: Palmer Archipelago (Antarctica) penguin data*. DOI: 10.5281/zenodo.3960218. The underlying study is Gorman KB, Williams TD, Fraser WR. 2014. *Ecological sexual dimorphism and environmental variability within a community of Antarctic penguins (genus Pygoscelis).* PLOS ONE 9:e90081. DOI: 10.1371/journal.pone.0090081.

Canonical dataset source used for this example:
https://github.com/allisonhorst/palmerpenguins/blob/main/inst/extdata/penguins.csv

## Planned analysis

The lead analysis will:

1. verify the dataset structure and missingness relevant to the analysis;
2. summarize body mass and flipper length overall and by species;
3. fit an unadjusted linear model relating body mass to flipper length;
4. fit a species-adjusted model;
5. test whether species-specific slopes materially improve interpretation using an interaction model;
6. produce a figure and tabular model outputs;
7. state assumptions and limitations without treating model agreement as scientific validation.

## Acceptance criteria

The User will decide whether to accept the result after:

- the exact dataset used is preserved and its source recorded;
- the analysis is executable from a versioned script;
- missing-data handling is explicit;
- model outputs and a figure are preserved;
- execution details are recorded;
- a second AI participant reviews the actual script, outputs, and interpretation;
- any substantive review findings are repaired, retained as limitations, or adjudicated by the User;
- the accepted conclusion is written into the project record.

## SCUTER roles

- **User:** Deanne Taylor, scientific authority and acceptance authority.
- **Lead AI:** GPT, first-pass analysis and documentation.
- **Review AI:** Claude, reciprocal review after the lead analysis is committed.

Roles could be reversed in another work unit. This example uses the current SCUTER development version recorded at repository root.

## Current state

Project initialized. No scientific result has yet been accepted.
