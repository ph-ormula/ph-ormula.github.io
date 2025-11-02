---
layout: default
title: Introduction to Typst and Recommended HiMCM Collaboration Workflows
permalink: /math-talks/typst-himcm-collab-workflows/
---

# Introduction to Typst and Recommended HiMCM Collaboration Workflows

## What is Typst

### What Are Typesetting Languages?

- Typesetting languages are specialized systems that control how text appears on a page or screen
- Instead of clicking formatting buttons like in Microsoft Word, you write simple codes or commands that tell the computer how to arrange text, equations, images, and other elements
- They handle complex formatting automatically: page numbers, footnotes, citations, table of contents, mathematical equations, and consistent styling throughout your document
- Originally used for professional printing, they're now essential for creating academic papers, technical documents, and books
- The main benefit: you focus on writing content while the system handles all the visual formatting rules consistently

### Why Use Typst

#### Advantages over Microsoft Word/other office apps


- Compatibility

	![](https://img2.joyreactor.cc/pics/post/LibreOffice-ms-word-%D0%94%D0%B6%D0%B0%D0%BD%D0%BA%D0%B0%D1%80%D0%BB%D0%BE-%D0%AD%D1%81%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE-8149261.jpeg){: width="50%"}
- Full precise control over documents

	![](https://images7.memedroid.com/images/UPLOADED819/64a1d3e2c44ae.jpeg){: width="60%"}
- No leaving the keyboard (even for document settings)
- Convenient math input (also keyboard only)
- Pure text format: git tracking and AI collaboration (important features of the workflow I'll introduce)

#### Advantages over LaTeX

- Fast: Compiles documents in under 5 seconds versus minutes with LaTeX
- Easy to learn: Clean, readable syntax similar to Markdown—no confusing backslashes or brackets (including simplified math inputs)
- Clear error messages: Understandable explanations instead of cryptic technical errors that frustrate beginners
- Real-time preview: See your formatted paper instantly as you type
- Built-in citation handling: Automatic bibliography and reference management
- Modern programming features: Variables and functions make complex documents easier to automate

## Overview of Typst

- [https://typst.app](https://typst.app)

# Suggested Collaboration Workflows for HiMCM

## Basic: fully online real-time collaboration using [typst.app](https://typst.app)

Copy the file contents/download the entire project as zip and use any AI to debug/add features

## Advanced: Windsurf + git + P2P Live Share

- Requires at least 1 member in the team to have git knowledge, optimally all members, [git guide from PHGameStudio website](https://phgamestudio.github.io/resources/git-guide/)
	- All members need to know how to commit, checkout, push, and pull/fetch in git
- Install [Windsurf](https://windsurf.com/) and install the [tinymist typst](https://open-vsx.org/extension/myriad-dreamin/tinymist) plugin to edit typst with real-time preview
- You can get unlimited free trials by following the guide on [the PHGameStudio website](https://phgamestudio.github.io/)
- Use git for large edits made by 1 person
- Use the [P2P Live Share plugin](https://open-vsx.org/extension/kermanx/p2p-live-share) for meeting edits where multiple people edit the same part simultaneously
