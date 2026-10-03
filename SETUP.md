# Set up your course and David AI Coach

**Course:** https://github.com/tbhrc/Course-Andre-Venter

David AI Coach is the AI tutor defined in this course's `AGENTS.md`. It runs in your chosen AI environment using David Potgieter's practical teaching method. Activating it means giving that environment the course files and startup prompt.

## Start in your browser

1. Open the course link above and [ChatGPT](https://chatgpt.com/) or your preferred capable AI assistant.
2. Paste the startup prompt below.
3. Have the coach confirm it actually read `AGENTS.md` and `LEARNER-PROFILE.md` and `course/00-start-here.md`. A link alone does not prove file access.
4. If it cannot read the repository, download the course as described below and upload those individual Markdown files, or paste their contents. Add the current lesson and your saved progress as needed. File availability and limits depend on your AI provider.
5. Answer the baseline honestly, then do one exercise at a time. Save your answers and completed work in your own course folder.

You can begin this way without installing the course or writing code.

## Download for practical work

1. Open the course on GitHub. Choose **Code → Download ZIP** and extract it into a folder you will keep, such as `Course-Andre-Venter`.
2. Install or open your preferred AI coding environment. For OpenAI's current desktop installation and folder-opening instructions, use the [official app guide](https://developers.openai.com/codex/app/), sign in with your own account, open the extracted course folder, and choose Codex for coding exercises. Product names and interfaces can change; follow the current official instructions for your operating system.
3. Start a new conversation in that folder and paste the prompt below. Confirm that the AI can read the files and save your work there.
4. The ZIP gives you the course files. The Git/GitHub module will guide Git setup and version history when you reach it. Install lab dependencies only when the relevant lab calls for them.

If Git is already installed, cloning is an alternative to ZIP. These commands download the course and move your terminal into its folder:

```sh
git clone https://github.com/tbhrc/Course-Andre-Venter.git
cd Course-Andre-Venter
```

## Activate David AI Coach

Copy this into your AI environment:

> Open and work from https://github.com/tbhrc/Course-Andre-Venter. Read the root AGENTS.md and LEARNER-PROFILE.md first. Act as David AI Coach. Confirm which files you read, start with course/00-start-here.md, and guide my baseline one question at a time. Make me do the exercises, inspect my work, help me debug, verify outcomes and explain what I learned. Resume from my saved progress when it exists.

Expect it to introduce itself as **David AI Coach**, confirm file access, and help you establish your baseline. Use `prompts/01-course-coach.md` to resume in a fresh session.

## Keep your progress

Your working copy holds `work/00-baseline.md`, your exercise artifacts and `work/progress.md`. Ask David AI Coach to save your demonstrated understanding, gaps and next step at a meaningful checkpoint. In a browser without file-writing access, save the text it provides yourself and supply it next time.

Keep personal answers, private documents and secrets in your own local copy or private repository. Public course files are the shared curriculum.

The curriculum and coach instructions are free. Your chosen AI provider's plan, limits and charges apply separately.

## Current setup sources

Provider setup verified on 4 October 2026: [OpenAI desktop guide](https://developers.openai.com/codex/app/) and [ChatGPT file uploads FAQ](https://help.openai.com/en/articles/8555545-file-uploads-faq). Recheck current official guidance if an installation screen or capability differs.
